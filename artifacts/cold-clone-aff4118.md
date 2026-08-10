# Cold-clone verification report — cycle 017

**Label: PROVED** (infrastructure verification only)

- Tested commit: `aff411847c9e739867a6b04e7508e566e225a71f`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; twenty reference tests
  passed
- Working tree after verification: clean

The audit reported 70 canonical claims: 40 `PROVED`, 17 `NO-GO`, 12
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
