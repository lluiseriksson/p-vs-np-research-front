# GATE-004AX-ARBITRARY-BASE — extend selector penetration to every nonconstant base

**Label: NO-GO**

The GATE-004AX inequality is false if the canonical row dependence is replaced
only by the requirement that both row residuals be nonconstant.

Let the base inputs include a row selector `a` and an independent input `z`,
and take

`H(a,z)=z`.

For the implication tail `W_m=AND_i(t_i OR NOT u_i)`, put

`J=z AND W_m`.

Choose the two rows `a=0` and `a=1`. Both residual base functions equal the
nonconstant raw input `z`. With the convention that raw inputs cost zero
gates, `K=C(H)=0`. LEMMA-142 at positive width `p=1` proves exactly

`C(J)=3m`,

so `Delta=K+3m-C(J)=0`.

The output function is independent of `a`. By LEMMA-149, every gate function
in every minimum circuit for `J` is independent of `a`. Thus the two row
cofactor sets coincide and LEMMA-150 gives `Q_J<=3m`. Since `b>=0`,

`Q_J-b<=3m<4m=4m-2(Delta+K)`.

Hence every minimum circuit violates the generalized GATE-004AX target. This
does not refute the canonical gate: it proves that a valid proof must use the
specific essential variation between the canonical rows, not merely
nonconstant row residuals or the implication tail.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for a raw positive enable input conjoined with the implication tail |
| Uniform/non-uniform | Fully non-uniform exact counterexample family |
| Circuit size | Exact `C(J)=3m`, `K=Delta=0`, and quotient upper `Q_J<=3m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and essential-variable dependence only |
| Asymptotic quantifiers | Every `m>=1`; two rows of one inessential selector; both residual bases nonconstant |
| Regime | Exact worst-case counterexample to arbitrary-base promotion; canonical GATE-004AX/AW/AV/AU/AG/AE remain open |
