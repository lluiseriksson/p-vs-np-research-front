# Cold-clone verification report — cycle 035

**Label: PROVED** (infrastructure verification only)

- Tested commit: `1f914a8f6b88a0dd34a7ced6fb8b2c7d3cd8344c`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-three reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 115 canonical claims: 65 `PROVED`, 30 `NO-GO`, 18
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
