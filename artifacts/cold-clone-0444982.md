# Cold-clone verification report — cycle 026

**Label: PROVED** (infrastructure verification only)

- Tested commit: `0444982c1ba55ca649057c411c9125fc12d731cf`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; twenty-two reference
  tests passed
- Working tree after verification: clean

The audit reported 91 canonical claims: 52 `PROVED`, 23 `NO-GO`, 15
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
