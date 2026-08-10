# Cold-clone verification report — cycle 010

**Label: PROVED** (infrastructure verification only)

- Tested commit: `c1017779e313210a8adf043897b851e7de545a09`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; seventeen reference tests
  passed
- Working tree after verification: clean

The audit reported 53 canonical claims: 30 `PROVED`, 12 `NO-GO`, 10
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
