# Cold-clone verification report — cycle 045

**Label: PROVED** (infrastructure verification only)

- Tested commit: `426e338fe1d11d1593edda15def314886eb2657c`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; forty-five reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 147 canonical claims: 83 `PROVED`, 40 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
