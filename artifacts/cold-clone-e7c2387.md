# Cold-clone verification report — cycle 034

**Label: PROVED** (infrastructure verification only)

- Tested commit: `e7c2387e7354700f6bac2119115f20d2dd3c427c`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-two reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 113 canonical claims: 64 `PROVED`, 29 `NO-GO`, 18
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
