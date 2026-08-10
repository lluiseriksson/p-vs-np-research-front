# Cold-clone verification report — cycle 036

**Label: PROVED** (infrastructure verification only)

- Tested commit: `9137e8cd80657b75ba5d8eb4cc96298235afd454`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-four reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 118 canonical claims: 66 `PROVED`, 31 `NO-GO`, 19
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
