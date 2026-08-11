# Cycle 187 — canonical-frontier circularity audit

**Label: PROVED**

LEMMA-221 identifies the full semantic difference region of a proposed
rewrite. Its canonical exterior boundary is functionally sealed, but the
output lies outside the region exactly when the parent function is already
known to be preserved.

Therefore GATE-004DN-CANONICAL-DIFFERENCE-REGION-ONLY is `NO-GO`: the
canonical seal is an a posteriori audit, not a noncircular proof of parent
preservation. GATE-004DO requires an independently selected cut whose complete
four-code equality is proved without consulting the output equality.

## Classification

- LEMMA-221: `PROVED`
- GATE-004DN-CANONICAL-DIFFERENCE-REGION-ONLY: `NO-GO`
- GATE-004DO: `EXPLORATORY`

`verification/canonical_difference_frontier_audit.py` checks one rewrite
whose change is absorbed at an interior tautological frontier and one whose
difference reaches the output. The general equivalence is a human proof.
Fable was not invoked; independent certification and terminal implications
are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted constant-free AND/OR/NOT DAGs and canonical semantic difference regions |
| Uniform/non-uniform | Every finite non-uniform circuit pair; two finite diagnostic pairs |
| Circuit size | Arbitrary finite size; diagnostic circuits have at most five gates |
| Circuit depth | Unrestricted finite depth; diagnostic depth at most four |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean truth tables, DAG reachability, and directed cuts |
| Asymptotic quantifiers | Every finite circuit pair and every vertex; exhaustive diagnostic assignments |
| Regime | Exact semantic equivalence and circularity no-go; not a SAT lower bound or terminal result |
