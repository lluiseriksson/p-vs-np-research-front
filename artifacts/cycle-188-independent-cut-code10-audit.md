# Cycle 188 — independent-cut and code-10 audit

**Label: PROVED**

LEMMA-222 proves the noncircular graph interface: if every path from every
structurally retargeted gate to the parent crosses a disjoint set of gates
whose old/new functions are independently equal, the parent is preserved.

LEMMA-223 then localizes the exact remaining semantic obstruction. Equality
on the three satisfying codes forces every cut difference to have the form
`u AND NOT t AND d(x)` but places no restriction on `d`. Therefore
GATE-004DO-SATISFYING-CUT-ONLY is `NO-GO` (NG-164), and GATE-004DP asks to
kill each code-`10` defect or charge its first cancellation physically.

## Classification

- LEMMA-222: `PROVED`
- LEMMA-223: `PROVED`
- GATE-004DO-SATISFYING-CUT-ONLY: `NO-GO`
- GATE-004DP: `EXPLORATORY`

`verification/independent_cut_code10_audit.py` exhausts all 1,024 pairs of
three-code-equal Boolean functions on `(u,t,x)` and checks the exact defect
factorization. The cut theorem is a human DAG proof. Fable was not invoked;
independent certification and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted AND/OR/NOT DAGs, structural vertex cuts, and exact four-code Boolean functions |
| Uniform/non-uniform | Every supplied finite cut interface and all one-base-bit three-code-equal truth tables |
| Circuit size | Unrestricted; diagnostic function tables have three inputs |
| Circuit depth | Unrestricted in the theorem; finite explicit witness depth three |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors, directed reachability, and analytical differences over `F_2` |
| Asymptotic quantifiers | Every finite cut interface; all 1,024 qualifying one-base-bit table pairs and all assignments |
| Regime | Exact interface theorem and satisfying-row no-go; not a SAT lower bound or terminal result |
