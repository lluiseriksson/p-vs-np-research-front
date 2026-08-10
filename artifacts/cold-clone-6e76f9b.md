# Cold-clone verification report — cycle 043

**Label: PROVED** (infrastructure verification only)

- Tested commit: `6e76f9b3abe258dc9907cda4ba940826f99a6b9b`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; forty-two reference and
  experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 141 canonical claims: 79 `PROVED`, 38 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
