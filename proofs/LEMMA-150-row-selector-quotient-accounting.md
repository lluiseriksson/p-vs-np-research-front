# LEMMA-150 — exact row-selector quotient accounting

**Label: PROVED**

Let `C` be a circuit with `s` gates and let two restrictions `rho_0,rho_1`
fix the same set of row variables while leaving residual variables `Y` free.
Interpolate the two rows by one Boolean selector `a`: coordinates on which the
rows agree are fixed, a coordinate changing from zero to one is set to `a`,
and one changing from one to zero is set to `NOT a`.

For each gate `v`, let `g_v(a,Y)` be its function after this interpolation.
Let `D_a(C)` be the number of gates for which `g_v` depends essentially on
`a`. Let `Q(C)` be the union of the distinct active nonconstant gate-cofactor
classes at `a=0` and `a=1`. Then

`Q(C)<=s+D_a(C)`.

Equivalently, the row-collapse defect

`E_row(C)=s+D_a(C)-Q(C)`

is a nonnegative integer and

`Q(C)=s+D_a(C)-E_row(C)`.

## Proof

If `g_v` is independent of `a`, its two row cofactors are identical, so gate
`v` can contribute at most one class to the union. If `g_v` depends on `a`,
its two cofactors can contribute at most two classes. Inactivity, constants,
raw-input coincidences, and collisions between different gates only decrease
the union. Summing the per-gate maxima gives

`Q(C)<=(s-D_a)+2D_a=s+D_a`.

The asserted identity is the definition of the resulting nonnegative defect.

## Canonical implication consequence

For GATE-004AX, `s=K+3m-Delta`. Therefore its target

`Q_J-b>=4m-2(Delta+K)`

is exactly equivalent to

`D_a-E_row-b>=m-Delta-3K`.

In particular, any witnessing minimum circuit must satisfy the necessary
selector-penetration bound

`D_a>=m+b-Delta-3K`.

Since the canonical regime has `Delta<=K=o(m)`, GATE-004AX requires
`m-o(m)` gates whose interpolated functions genuinely depend on the row
selector. This is a necessary structural condition, not a proof that such a
minimum circuit exists.

## Model card

| Field | Value |
|---|---|
| Computational model | Arbitrary unrestricted circuits under two row restrictions and their one-bit interpolation |
| Uniform/non-uniform | Every individual non-uniform circuit; canonical rows only in the consequence |
| Circuit size | Exact upper `Q<=s+D_a`; canonical identity with `s=K+3m-Delta` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and a semantic one-bit row interpolation; no algebraic circuit model |
| Asymptotic quantifiers | Every finite circuit and every pair of compatible row restrictions; sufficiently large canonical instances only for the `o(m)` consequence |
| Regime | Exact worst-case quotient accounting and necessary condition; not quotient stability, a SAT lower bound, or a terminal result |
