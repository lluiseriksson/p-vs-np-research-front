# Cold-clone verification report — cycle 009

**Label: PROVED** (infrastructure verification only)

- Tested commit: `f444670df07952b66fd19f09a67ce99e59939fcd`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; sixteen reference tests
  passed
- Working tree after verification: clean

The audit reported 49 canonical claims: 28 `PROVED`, 11 `NO-GO`, 9
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
