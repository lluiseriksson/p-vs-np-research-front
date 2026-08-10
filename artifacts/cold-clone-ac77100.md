# Cold-clone verification report — cycle 049

**Label: PROVED** (infrastructure verification only)

- Tested commit: `ac77100a45ccd5783b749b467e565f9c63960d68`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; fifty reference and
  experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 158 canonical claims: 91 `PROVED`, 43 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
