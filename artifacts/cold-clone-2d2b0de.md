# Cold-clone verification report — cycle 007

**Label: PROVED** (infrastructure verification only)

- Tested commit: `2d2b0debb1e39e5e400e9174472b7c01e509563e`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; fourteen reference tests
  passed
- Working tree after verification: clean

The audit reported 43 canonical claims: 24 `PROVED`, 9 `NO-GO`, 9
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
