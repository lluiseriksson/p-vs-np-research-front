# Cold-clone verification report — cycle 038

**Label: PROVED** (infrastructure verification only)

- Tested commit: `0ca57cb187bd95cd2b8c0231b279d816be81e345`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-six reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 124 canonical claims: 70 `PROVED`, 33 `NO-GO`, 19
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
