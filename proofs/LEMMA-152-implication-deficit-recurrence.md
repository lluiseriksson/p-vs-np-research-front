# LEMMA-152 — implication deficits grow by zero, one, or two

**Label: PROVED**

Let `H` have circuit complexity `K`, let two compatible row restrictions give
distinct nonconstant residuals, and define

`J_j=H AND AND_{i=1}^j(t_i OR NOT u_i)`,

`Delta_j=K+3j-C(J_j)`

for `j>=0`. Then `Delta_0=0` and

`0<=Delta_j-Delta_{j-1}<=2`.

Moreover, if `Delta_j=Delta_{j-1}`, every minimum circuit for `J_{j-1}` can
be extended by the three displayed gates for clause `j` to a minimum circuit
for `J_j`. Under the two rows this extension adds at least four new quotient
classes and introduces no new raw-input collision:

`Q_j>=Q_{j-1}+4`, `b_j=b_{j-1}`.

## Deficit recurrence

Appending `NOT u_j`, the OR gate `t_j OR NOT u_j`, and one final AND gives

`C(J_j)<=C(J_{j-1})+3`,

hence `Delta_j>=Delta_{j-1}`.

The variable `u_j` is essential in `J_j`: choose a satisfying base input,
satisfy all earlier clauses, and set `t_j=0`. Fixing `u_j=0` makes the new
clause identically true. Earliest-dependent-gate elimination therefore gives

`C(J_j)>=C(J_{j-1})+1`,

hence `Delta_j<=Delta_{j-1}+2`.

## Zero-increment extension

If the deficits are equal, the upper inequality is equality:

`C(J_j)=C(J_{j-1})+3`.

Thus the displayed three-gate extension of any minimum circuit is itself
minimum.

The new NOT and clause gates give the row-independent functions `NOT u_j`
and `t_j OR NOT u_j`. The new output AND has the two row cofactors

`J_{j-1,0} AND (t_j OR NOT u_j)`,

`J_{j-1,1} AND (t_j OR NOT u_j)`.

They are distinct because setting the new clause true leaves the distinct old
row residuals. All four functions depend essentially on fresh variables of
clause `j`, whereas inherited gates do not, so they are new quotient classes;
their support and base dependence also separate them from one another. None
is raw `t_j`, and no new gate is raw `t_i` for an earlier index. Hence the
extension adds at least four classes and leaves `b` unchanged.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for nested base–implication conjunctions and their two-row quotients |
| Uniform/non-uniform | Fully non-uniform base/minimum circuits; uniform ordered fresh clauses |
| Circuit size | `0<=Delta_j-Delta_{j-1}<=2`; exact three-gate extension at zero increment |
| Circuit depth | Unrestricted; one appended AND layer in the extension |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions, essential variables, and semantic row cofactors only |
| Asymptotic quantifiers | Every `j>=1`, every nonconstant finite `H`, and every pair of distinct nonconstant compatible row residuals |
| Regime | Exact worst-case recurrence and zero-increment stability; not a late-savings theorem, SAT lower bound, or terminal result |
