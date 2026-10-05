You are working on a statistical modeling problem from a longitudinal research dataset.

The file `/app/data/observations.csv` contains 420 ordered observations. Columns are `t`, two continuous predictors (`x1`, `x2`), and a response `y`. Some responses are missing. The response contains a latent temporal component and a predictor relationship that changes once during the series. A small number of observations are contaminated and the observation noise varies over time.

Estimate the underlying statistical structure rather than treating this as an ordinary least-squares regression. In particular, identify the coefficient-regime changepoint, estimate the two predictor coefficients on each side of that change, and evaluate predictive error over the final observed portion while accounting for temporal state.

Produce `/app/result.json` with these required fields:
- `changepoint`: integer estimate of the coefficient-regime change time.
- `beta_pre`: two-element array containing the estimated `x1` and `x2` coefficients before the change.
- `beta_post`: two-element array containing the estimated `x1` and `x2` coefficients after the change.
- `tail_rmse`: RMSE for the final observed portion under your one-step-ahead latent-state prediction procedure.
- `n_observed`: count of non-missing response observations used.

Use a statistically defensible robust time-series approach. You may inspect the data, write Python programs, and install scientific-computing packages. Do not assume the changepoint is supplied by the file.

The verifier compares your numerical result with hidden targets derived from the independently seeded data-generating process. Small differences between reasonable numerical implementations are allowed, but incomplete or guessed outputs are not.


You have 9000 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
