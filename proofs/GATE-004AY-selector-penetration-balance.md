# GATE-004AY — canonical selector-penetration balance

**Label: EXPLORATORY**

Use the canonical implication setup of GATE-004AX and the interpolating row
selector `a` of LEMMA-150. For a minimum circuit `C_J`, write `D_a` for the
number of selector-dependent interpolated gate functions and

`E_row=|C_J|+D_a-Q_J`.

## Falsifiable theorem

Prove that some minimum `C_J` satisfies

`D_a-E_row-b>=m-Delta-3K`.

A compatible canonical family for which every minimum circuit violates this
inequality falsifies the theorem.

## Exact bridge

LEMMA-150 proves

`Q_J=K+3m-Delta+D_a-E_row`.

Substitution shows that the displayed inequality is algebraically equivalent
to

`Q_J-b>=4m-2(Delta+K)`,

which is GATE-004AX. Thus GATE-004AY neither weakens nor silently strengthens
the required statement; it exposes its structural content.

Every proof must produce almost `m` selector-dependent gates and control two
losses: row-collapse defect and raw-input collisions. LEMMA-149 and
GATE-004AX-ARBITRARY-BASE show that this cannot follow from two nonconstant
residuals alone. The next attack must exploit the exact canonical row
transition to force selector dependence through the implication-tail
computation, or produce a canonical counterexample.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical implication circuits under a one-bit interpolation of two designated rows |
| Uniform/non-uniform | Uniform canonical row geometry and tail; fully non-uniform minimum-circuit adversary |
| Circuit size | Parent `K+3m-Delta`; target balance `D_a-E_row-b>=m-Delta-3K` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean row cofactors and semantic selector dependence; no algebraic circuit model |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and some minimum circuit for each instance |
| Regime | Exact reformulation of GATE-004AX; not a SAT lower bound or terminal result |
