# Testing Guidelines

## Running tests

- `uv run pytest` - the whole suite
- `uv run pytest tests/test_home.py` - one test file
- `uv run pytest -k <name>` - tests matching a name

All tests must pass on a clean checkout before a change is committed.

## Layout and naming

- Tests live in `tests/` and mirror the application package structure.
- Files are named `test_<module>.py`; test functions are named `test_<behaviour>`.
- Small, hand-checkable sample data goes in `tests/fixtures/`. Do not commit full annual reports or large source files.

## What to test

- **Financial indicators:** test each formula against small hand-computed inputs, including zero, negative and missing values, and missing periods.
- **Risk scoring:** test category boundaries exactly (30/31, 60/61, 80/81) and the 0-100 range. Test that weights and thresholds come from configuration.
- **Findings:** each finding carries the triggered indicator, the reason, the score impact, a High/Medium/Low confidence label and a source URL.
- **Extraction and normalization:** test units, periods (quarterly/annual, standalone/consolidated) and null handling against the data dictionary.
- **Fact vs anomaly vs interpretation:** test that extracted facts, detected anomalies and AI-generated interpretations remain distinguishable in outputs.
- **UI:** test Streamlit pages with `streamlit.testing.v1.AppTest` (for example `tests/test_home.py`). Check that pages render and show the key elements; do not assert on styling.

## Rules

- Tests must not call the network or AWS (Bedrock, Textract, SageMaker, S3, RDS). Mock or fake these at the boundary.
- Tests must be deterministic: no reliance on current date, random seeds or test order.
- Use no real credentials or secrets in tests or fixtures.
- Fix or delete a failing test; do not skip it without a linked GitHub issue.
- Add a test with every bug fix that reproduces the bug.
- Do not add test dependencies without asking (see `Agents.md`).
