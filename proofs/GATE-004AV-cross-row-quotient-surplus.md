# GATE-004AV — force the missing cross-row quotient surplus

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical base-tail function, let `C` be some minimum circuit, put
`Delta=K+6m-|C|`, and let `F_0,F_1` be its two designated row residuals.
Prove

`Q(C)-max(C(F_0),C(F_1)) >= m-2(Delta+K)`.

A canonical family for which every minimum circuit violates this inequality
falsifies the theorem.

## Exact bridge

LEMMA-145 gives `max(C(F_0),C(F_1))>=6m`. Therefore GATE-004AV implies

`Q(C)>=7m-2(Delta+K)`,

which is exactly GATE-004AU and yields negative diagonal loss by its audited
bridge.

The left side measures classes present in the union of the two row quotients
beyond the complexity forced by the harder single row. It is not obtained by
adding the two row sizes: GATE-004AV-SEPARATE-ROW-SIZES-ONLY records that their
intersection may contain an entire shared `W_m` computation.

The next attack must show that canonical suffix dependence forces at least
`m-O(Delta+K)` row-specific classes, or charge every missing class to a parent
gate saving or a base-size resource.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical base-tail circuits and unions of two semantic row quotients |
| Uniform/non-uniform | Uniform canonical rows; fully non-uniform minimum-circuit adversary |
| Circuit size | Target surplus `m-2(Delta+K)` above the harder single-row circuit complexity |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean semantic row cofactors and class intersections |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and some minimum circuit for each instance |
| Regime | Exact cross-row stability subgate for GATE-004AU; not a SAT lower bound or terminal result |
