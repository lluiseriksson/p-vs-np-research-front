# GATE-004AS — exclude tetracyclic four-NOT circuits for `W_9`

**Label: PROVED**

No pruned AND/OR/NOT circuit computing `W_9` has cycle rank four and exactly
four NOT gates.

LEMMA-139 gives the rank-four lower bound

`q>=9-4+1=6`,

contradicting four. Thus the exact obstruction isolated by LEMMA-138 is empty.
Generic path multiplicity remains insufficient by
GATE-004AS-PATH-MULTIPLICITY-ONLY; the proof instead uses the structural
block-cut/source induction.

The result is subsumed by full Hall LEMMA-141 and does not establish a SAT
circuit lower bound or P versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for fixed `W_9` with exact cycle rank four and four NOT gates |
| Uniform/non-uniform | Every individual non-uniform nine-block circuit in the exact stratum |
| Circuit size | Excludes `c=4,q=4`; a candidate would have 48 binary and 52 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`; Boolean source and articulation cofactors |
| Asymptotic quantifiers | Fixed `W_9` and every pruned circuit with `c=4,q=4` |
| Regime | Exact finite structural exclusion for nonet Hall; not a full SAT family lower bound or terminal result |
