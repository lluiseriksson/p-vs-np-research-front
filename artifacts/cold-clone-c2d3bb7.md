# Cold-clone verification report — cycle 012

**Label: PROVED** (infrastructure verification only)

- Tested commit: `c2d3bb73f03ee729de26d1ea64c5a309f130dd24`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; seventeen reference tests
  passed
- Working tree after verification: clean

The audit reported 58 canonical claims: 33 `PROVED`, 14 `NO-GO`, 10
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
