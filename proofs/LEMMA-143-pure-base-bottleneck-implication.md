# LEMMA-143 — a pure-base bottleneck implies exact base-tail additivity

**Label: CONDITIONAL**

Let `H(X)` be nonconstant with `C(H)=K`, let `Y` be disjoint fresh variables,
and put `F(X,Y)=H(X) AND W_m(Y)`. Suppose a circuit `C` for `F` contains a
gate `g` such that:

1. no `Y` input reaches `g`;
2. every directed path from every essential `X` input to the output passes
   through `g`; and
3. the gates in the transitive fanin of `g` meet the downstream output cone
   only at `g`.

Then `|C|>=K+(p+2)m`. Consequently, if a minimum circuit for the canonical
GATE-004AG conjunction has such a bottleneck, the LEMMA-107 upper circuit is
minimum and alternative 1 of GATE-004AG holds.

## Proof

The upstream subcircuit computes a nonconstant bit `z=A(X)`. Replacing it by
input `z` gives a downstream circuit `D(z,Y)` and a genuine one-bit
factorization `F(X,Y)=D(A(X),Y)`.

As `X` varies, the residual functions of `Y` are exactly `0` and `W_m`.
Therefore `A` distinguishes precisely `H=0` from `H=1`: it computes `H` or
its complement.

- If `A=H`, the upstream cost is at least `K` and the downstream function is
  `z AND W_m`, costing `(p+2)m` by LEMMA-142.
- If `A=NOT H`, appending one NOT to `A` computes `H`, so the upstream cost is
  at least `K-1`. The downstream function is `NOT z AND W_m`, costing
  `(p+2)m+1` by LEMMA-142.

Both codes therefore cost at least `K+(p+2)m` in total.

Condition 3 makes the two gate budgets disjoint, yielding the claimed sum.
The displayed LEMMA-107 circuit attains it and carries the recorded `7m`
tail quotient classes when `p=4`.

The conclusion is conditional only because no such bottleneck has been proved
for a minimum canonical circuit.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted base-tail circuits with a pure-base one-vertex functional separator |
| Uniform/non-uniform | Fully non-uniform base and circuit; uniform disjoint tail family |
| Circuit size | Conditional lower `K+(p+2)m`, matching LEMMA-107's upper bound |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and directed vertex separation; no algebraic circuit model |
| Asymptotic quantifiers | Every nonconstant finite `H`, every `m,p>=1`, and every circuit satisfying conditions 1–3 |
| Regime | Conditional base-tail direct sum; not a proof that minimum circuits have the separator, a SAT lower bound, or a terminal result |
