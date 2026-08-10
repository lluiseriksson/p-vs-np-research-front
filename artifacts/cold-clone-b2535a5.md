# Cold-clone verification report — cycle 037

**Label: PROVED** (infrastructure verification only)

- Tested commit: `b2535a50e64a294dd0442f29071f59c1b4783036`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; thirty-five reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 121 canonical claims: 68 `PROVED`, 32 `NO-GO`, 19
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
