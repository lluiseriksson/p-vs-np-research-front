# Cold-clone verification report — cycle 005

**Label: PROVED** (infrastructure verification only)

- Tested commit: `5ed3e2754e61d5b863d530ec5f577dcc1a629056`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; eleven reference tests
  passed
- Working tree after verification: clean

The audit reported 35 canonical claims: 20 `PROVED`, 7 `NO-GO`, 7
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
