# Cold-clone verification report — cycle 065

**Label: PROVED** (infrastructure verification only)

- Tested commit: `c3152a89b244deb11e1355ce8c7f018eb3adf158`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; fifty-six reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 201 canonical claims: 116 `PROVED`, 55 `NO-GO`, 28
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
