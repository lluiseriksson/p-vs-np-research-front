# GATE-004CH-OVERLAP-ONLY — a common physical backbone need not align functions

**Label: NO-GO**

## Tempting inference

Use the `K-4` three-way physical survivor overlap from LEMMA-188 as though
those gates computed the same base functions in all three satisfying minors.

## Exact-table witness

Let `x,y,z,u,t` be raw inputs. Expand XOR and the multiplexer in the
AND/OR/NOT basis and define

`r=x XOR y`,

`p=(NOT u AND x) OR (u AND y)`,

`g=p OR z`, `a=g OR r`,

`i=t OR NOT u`, and `F=a AND i`.

For `u=0`, `a=(x OR z) OR (x XOR y)=x OR y OR z`. For `u=1`, the same identity
with `y` gives `a=x OR y OR z`. Therefore, with `A=x OR y OR z`,

`F_00=F_01=F_11=A`, `F_10=0`.

The same physical binary gate `g` survives all three satisfying restrictions
as essential base computation. Its cofactors are

`g_00=g_01=x OR z`, while `g_11=y OR z`,

so physical survival does not give gatewise semantic alignment.

The circuit is not claimed minimum or a two-gate plateau. It refutes only the
promotion of overlap cardinality to equal cofactor labels. GATE-004CH must use
an explicit alignment descent or expose distinct elimination classes.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite AND/OR/NOT circuit with the exact four-code implication table |
| Uniform/non-uniform | One uniform five-input witness; no minimum-parent claim |
| Circuit size | Constant-size nonminimal witness; one common surviving gate has unequal satisfying cofactors |
| Circuit depth | Constant witness; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities only; XOR basis-expanded |
| Asymptotic quantifiers | Every assignment to `x,y,z,u,t` in the displayed circuit |
| Regime | Structural no-go for overlap-only alignment; not a plateau counterexample, SAT lower bound, or terminal result |
