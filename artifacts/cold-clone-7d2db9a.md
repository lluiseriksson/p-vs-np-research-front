# Cold-clone verification report — cycle 046

**Label: PROVED** (infrastructure verification only)

- Tested commit: `7d2db9a9bcedcc803299e52d3d2aa9f088161652`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; forty-six reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 149 canonical claims: 85 `PROVED`, 40 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
