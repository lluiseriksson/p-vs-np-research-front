# Cold-clone verification report — cycle 020

**Label: PROVED** (infrastructure verification only)

- Tested commit: `1ee7a1a07b30d43d2ccd3e416b26df3eb17e0130`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; twenty reference tests
  passed
- Working tree after verification: clean

The audit reported 78 canonical claims: 45 `PROVED`, 20 `NO-GO`, 12
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
