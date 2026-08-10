# Cold-clone verification report — cycle 028

**Label: PROVED** (infrastructure verification only)

- Tested commit: `b80599a85befa281b075eab61406c44b69211dc3`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Commands in clone:
  - `python verification/audit.py`
  - `python -m unittest discover -s verification -p 'test_*.py'`
- Results: both exit code 0; structural audit passed; twenty-three reference
  and experiment-reproduction tests passed
- Working tree after verification: clean

The audit reported 93 canonical claims: 53 `PROVED`, 23 `NO-GO`, 15
`EXPLORATORY`, 1 `CONDITIONAL`, 1 `NUMERICAL`, and zero `FORMALLY VERIFIED`
claims. It retained the guard `mathematical certification: NOT PERFORMED`.

This report verifies repository metadata, label consistency, local links,
manifest hashes, reference behavior, and exact reproduction of the bounded
experiment artifact. It does not certify the human proofs, promote the finite
search to an asymptotic theorem, or change the 0.00% terminal-progress estimate.
