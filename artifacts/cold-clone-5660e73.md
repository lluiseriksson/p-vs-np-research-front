# Cold-clone verification report — cycle 064

**Label: PROVED** (infrastructure verification only)

- Tested commit: `5660e7341cf609b7b291e11232780e419cbb2a83`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; fifty-five reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 199 canonical claims: 114 `PROVED`, 55 `NO-GO`, 28
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
