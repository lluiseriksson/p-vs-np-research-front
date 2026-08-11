# LEMMA-142 — positive and negative enable bits have exact tail cost

**Label: PROVED**

For a fresh input `z`, define

`E_m(z,Y)=z AND W_m(Y)`.

Then, for every fixed `p>=1` and `m>=1`,

`C(E_m)=(p+2)m`.

For the opposite code

`E_m^-(z,Y)=NOT z AND W_m(Y)`, one has

`C(E_m^-)=(p+2)m+1`.

The upper bound computes `W_m` with `(p+2)m-1` gates by LEMMA-140 and adds
one AND gate with `z`.

For the lower bound, `z` is essential and `E_m` is not a raw input. In any
minimum circuit, fix `z=1` and eliminate the earliest gate depending on `z`;
constant propagation and pruning remove at least one gate. The residual
computes `W_m`, so LEMMA-140 gives

`C(E_m)-1>=C(W_m)=(p+2)m-1`.

Thus equality holds.

For `E_m^-`, view `NOT z` as one additional disjoint one-negative clause of
positive width zero. The heterogeneous exact-size corollary of LEMMA-140 has
`m+1` clauses and total positive width `pm`, giving

`pm+2(m+1)-1=(p+2)m+1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted De Morgan circuits for one fresh enable bit conjoined with `W_m` |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform explicit function family |
| Circuit size | Exact `(p+2)m` for `z AND W_m`; exact `(p+2)m+1` for `NOT z AND W_m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction and gate elimination only |
| Asymptotic quantifiers | Every fixed `p>=1` and every `m>=1` |
| Regime | Exact worst-case enabled-tail size; not external-base additivity, a SAT lower bound, or a terminal result |
