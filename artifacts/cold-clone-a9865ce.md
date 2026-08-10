# Cold-clone verification report

**Label: PROVED** (infrastructure verification only)

- Source repository: `C:\Users\lluis\Documents\Codex\p-vs-np-research-front`
- Tested commit: `a9865ce7800dea0e5017ee6c34f803e3895d109f`
- Date: 2026-08-10
- Clone mode: `git clone --no-local`
- Command in clone: `python verification/audit.py`
- Result: exit code 0, `AUDIT PASSED`
- Working tree after audit: clean

The audit reported 14 canonical claims, no `FORMALLY VERIFIED` claims, no
`NUMERICAL` claims, and the explicit guard `mathematical certification: NOT
PERFORMED`. This report certifies reproducibility of repository metadata and
hashes only. It does not certify the mathematical proof in GATE-002 and does not
change the terminal progress estimate.
