
import csv, json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.signal import savgol_filter

DATA=Path("/app/data/observations.csv")
OUT=Path("/app/result.json")
rows=list(csv.DictReader(DATA.open()))
t=np.array([int(r["t"]) for r in rows])
x=np.array([[float(r["x1"]),float(r["x2"])] for r in rows])
y=np.array([np.nan if r["y"]=="" else float(r["y"]) for r in rows])
obs=np.isfinite(y)
X=np.column_stack([np.ones(len(t)),x])
xo=X[obs]; yo=y[obs]

def huber(r,delta=1.35):
    a=np.abs(r)
    return np.where(a<=delta,.5*r*r,delta*(a-.5*delta))

def fit_loss(a,b):
    def fun(v):
        r=b-a@v
        s=1.4826*np.median(np.abs(r-np.median(r)))+1e-8
        return float(np.sum(huber(r/s,1.5))*s)
    init=np.linalg.lstsq(a,b,rcond=None)[0]
    v=minimize(fun,init,method="BFGS").x
    return float(fun(v)),v

# Initial robust fit used only to expose the latent temporal component.
_,base=fit_loss(xo,yo)
resid=np.full(len(t),np.nan)
resid[obs]=y[obs]-X[obs]@base
idx=np.arange(len(t))
rr=resid.copy()
rr[~np.isfinite(rr)]=np.interp(idx[~np.isfinite(rr)],idx[np.isfinite(rr)],rr[np.isfinite(rr)])
latent_hat=savgol_filter(rr,31,2,mode="interp")

scores=[]
for cp in range(100,321):
    m1=obs&(t<cp); m2=obs&(t>=cp)
    if m1.sum()<80 or m2.sum()<80: continue
    l1,v1=fit_loss(X[m1],y[m1]); l2,v2=fit_loss(X[m2],y[m2])
    scores.append((l1+l2,cp,v1,v2))
scores.sort(key=lambda q:q[0])
_,cp,vpre,vpost=scores[0]

pred=np.empty(len(t))
for i in range(len(t)):
    state=latent_hat[i-1] if i else 0.
    pred[i]=X[i]@(vpre if t[i]<cp else vpost)+state
tail=obs&(t>=360)
rmse=float(np.sqrt(np.mean((y[tail]-pred[tail])**2)))

OUT.write_text(json.dumps({
    "changepoint":int(cp),
    "beta_pre":[float(vpre[1]),float(vpre[2])],
    "beta_post":[float(vpost[1]),float(vpost[2])],
    "tail_rmse":rmse,
    "n_observed":int(obs.sum())
},indent=2,sort_keys=True))
