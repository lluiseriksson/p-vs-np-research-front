# Cold-clone verification report — cycle 006

**Label: PROVED** (infrastructure verification only)

- Tested commit: `17cab2fe312c41a6645bb3df6a42f4558e57bf84`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py' -v`
- Results: both exit code 0; structural audit passed; thirteen reference tests
  passed
- Working tree after verification: clean

The audit reported 40 canonical claims: 23 `PROVED`, 8 `NO-GO`, 8
`EXPLORATORY`, 1 `CONDITIONAL`, and zero `FORMALLY VERIFIED` or `NUMERICAL`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, and reference-implementation behavior. It does not certify
the human proofs or change the 0.00% terminal-progress estimate.
