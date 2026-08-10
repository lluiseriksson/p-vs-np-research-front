# Cold-clone verification report — cycle 041

**Label: PROVED** (infrastructure verification only)

- Tested commit: `f5739c05b82c62315067edbc7312a2e45afb9d75`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; forty reference and
  experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 136 canonical claims: 76 `PROVED`, 36 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
