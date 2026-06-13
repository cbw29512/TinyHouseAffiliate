## What changed
- Improved error handling in `tests/test_schema_validation.py` in the `validate_model` function.
- Added a try/except block to provide more informative error messages when validation fails.

## Why it matters
- The previous error handling was limited to just checking for Pydantic v2 vs v1 APIs.
- With this change, if validation fails, we get more descriptive error information to aid debugging.

## How to verify
Run the test suite:
```bash
python3 -m pytest tests/test_schema_validation.py -v
```