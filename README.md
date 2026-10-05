# Robust latent-state changepoint inference

## Difficulty

This is a longitudinal statistical inference workflow rather than a classroom exercise. The solver must inspect an imperfect time series, handle missing responses and contamination, estimate a latent temporal component, identify an unknown coefficient-regime change, and quantify predictive error. The dataset is synthetic and reproducibly seeded; the hidden grading targets come from the independently defined data-generating process rather than from the reference solver.

## Reference solution

`solution/solve.sh` runs a robust regression, latent-state smoothing, candidate changepoint search, and tail prediction evaluation. The reference is used only during the oracle run and is not copied into the agent environment.

## Verification

`tests/test.sh` runs in a separate offline verifier image. It checks `/app/result.json` for the required schema and compares its changepoint, coefficient estimates, prediction RMSE, and observed-count against hidden values derived independently from the seeded generator. Numerical tolerances allow reasonable estimator variation while rejecting guesses and malformed output.
