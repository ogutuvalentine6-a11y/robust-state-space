Adversarial checks considered:
- Empty result: rejected because /app/result.json is required.
- Only observed-count: rejected because all numerical fields are checked.
- Malformed JSON: rejected.
- Approximate guesses: changepoint, coefficients, and RMSE all have bounded tolerances.
- Copying values from environment: hidden expected values are absent from environment/.
