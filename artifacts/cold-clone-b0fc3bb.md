# Cold-clone verification report — cycle 032

**Label: PROVED** (infrastructure verification only)

- Tested commit: `b0fc3bbbdb471f36d81571516c5ac203607ec856`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; twenty-nine reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 104 canonical claims: 59 `PROVED`, 27 `NO-GO`, 16
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
