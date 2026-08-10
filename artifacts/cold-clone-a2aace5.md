# Cold-clone verification report — cycle 040

**Label: PROVED** (infrastructure verification only)

- Tested commit: `a2aace5a2c10346ab33bf7dea4baf28438cf119e`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-eight reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 131 canonical claims: 73 `PROVED`, 35 `NO-GO`, 21
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
