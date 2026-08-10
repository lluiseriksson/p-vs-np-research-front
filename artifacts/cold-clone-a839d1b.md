# Cold-clone verification report — cycle 013

**Label: PROVED** (infrastructure verification only)

- Tested commit: `a839d1b911328b318a10e5fa5f755c281e350ba1`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; seventeen reference tests
  passed
- Working tree after verification: clean

The audit reported 60 canonical claims: 34 `PROVED`, 15 `NO-GO`, 10
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
