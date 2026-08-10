# Cold-clone verification report — cycle 042

**Label: PROVED** (infrastructure verification only)

- Tested commit: `4216f2031252c273007fc6176d0010d3c7551ca2`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; forty-one reference and
  experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 138 canonical claims: 77 `PROVED`, 37 `NO-GO`, 22
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and experiment reproduction. It does not
certify the human proofs or change the 0.00% terminal-progress estimate.
