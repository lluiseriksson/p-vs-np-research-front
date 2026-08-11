# Cycle 167 — rowwise cancellation audit

**Label: PROVED**

LEMMA-200 gives necessary and sufficient conditions for an AND or OR boundary
to cancel a monotone `u` difference on either fixed `t` row. It covers both
aligned masks and `u`-sensitive counterflows.

An explicit local counterflow satisfies the identities on both rows while
remaining nonconstant and preserving the three-gate `01/11` carrier. Thus
counterflow existence or reconvergence alone is `NO-GO`. GATE-004CU must use
minimum cost, exact pruning loss, a private certificate, or cycle rank.

## Classification

- LEMMA-200: `PROVED`
- GATE-004CT-COUNTERFLOW-LOCAL-ONLY: `NO-GO`
- GATE-004CU: `EXPLORATORY`
