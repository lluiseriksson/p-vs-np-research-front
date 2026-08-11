# Cycle 192 — swap-provenance cycle audit

**Label: PROVED**

LEMMA-228 proves a conditional physical dichotomy: two defect routes
coexisting in one DAG have distinct marked origins, or a common origin creates
a nonzero undirected provenance cycle.

LEMMA-229 then applies the exact plateau minor structure. Every such parent
cycle survives all three satisfying restrictions modulo contractions. Hence
GATE-004DS-CYCLE-EXISTENCE-AS-LOSS is `NO-GO` (NG-168): the common-origin
cycle cannot be paid as a destroyed coordinate. GATE-004DT separates genuine
distinct origins from marked-support exchanges on the surviving cycle.

## Classification

- LEMMA-228: `PROVED`
- LEMMA-229: `PROVED`
- GATE-004DS-CYCLE-EXISTENCE-AS-LOSS: `NO-GO`
- GATE-004DT: `EXPLORATORY`

`verification/swap_provenance_cycle_audit.py` checks 64 pairs of internally
disjoint common-origin paths and contraction rank, plus a distinct-origin
rank-zero tree. The endpoint survival statement is the exact LEMMA-174/185
consequence. Fable was not invoked; independent certification and terminal
implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite physical DAG paths and exact-plateau parent/minor output-cone multigraphs |
| Uniform/non-uniform | Every supplied finite path pair and every finite hypothetical endpoint cycle |
| Circuit size | Unrestricted path lengths; endpoint parent `K+2` and two rank-neutral losses per satisfying minor |
| Circuit depth | Unrestricted |
| Fan-in | Binary reconvergence; circuit AND/OR two and NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank, contractions, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every finite marked path pair, provenance cycle, contraction, and satisfying code |
| Regime | Exact conditional topology and cycle-survival results; not a SAT lower bound or terminal result |
