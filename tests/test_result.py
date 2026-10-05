import json, math
from pathlib import Path

p=Path("/artifacts/result.json")
assert p.exists(), "missing /artifacts/result.json"
d=json.loads(p.read_text())
expected={"beta_post": [1.35905, -0.20905], "beta_pre": [0.7737, -0.8081499999999999], "changepoint": 238, "n_observed": 392, "tail_rmse": 0.35401703559962217}

assert set(d.keys()) == set(expected.keys())
assert isinstance(d["changepoint"],int)
assert d["n_observed"] == expected["n_observed"]
assert abs(d["changepoint"]-expected["changepoint"]) <= 1

for got,key in ((d["beta_pre"],"beta_pre"),(d["beta_post"],"beta_post")):
    assert isinstance(got,list) and len(got)==2
    for a,b in zip(got,expected[key]):
        assert math.isfinite(float(a))
        assert abs(float(a)-b) <= 0.080

assert math.isfinite(float(d["tail_rmse"]))
assert abs(float(d["tail_rmse"])-expected["tail_rmse"]) <= 0.050
