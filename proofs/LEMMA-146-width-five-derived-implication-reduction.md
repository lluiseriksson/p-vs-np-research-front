# LEMMA-146 — the width-five tail is an exact derived implication tail

**Label: PROVED**

Let `H(X)` be nonconstant. On fresh disjoint inputs define

`J=H AND AND_i (t_i OR NOT u_i)`

and

`F=H AND AND_i (v_{i,1} OR v_{i,2} OR v_{i,3} OR v_{i,4} OR NOT u_i)`.

Then

`C(F)=C(J)+3m`.

Moreover, substituting a three-gate OR chain

`a_i=v_{i,1} OR v_{i,2}`,

`b_i=a_i OR v_{i,3}`,

`P_i=b_i OR v_{i,4}`

for every raw `t_i` in any minimum circuit for `J` produces a minimum circuit
for `F`. Under any base-only row restrictions, the `2m` prefix functions
`a_i,b_i` are distinct active quotient classes not realized by inherited
gates. The full `P_i` classes are also distinct, but may collide with an
inherited row cofactor equal to raw `t_i`.

## Exact size

Substitution gives the upper bound `C(F)<=C(J)+3m`.

For the reverse inequality, successively set
`v_{i,2}=v_{i,3}=v_{i,4}=0` for every block. Each selected variable is
essential before its restriction: choose `H=1`, satisfy all other clauses,
put `u_i=1`, and make every other remaining positive literal in its clause
zero. Earliest-dependent-gate elimination removes at least one gate per
restriction. After `3m` restrictions and renaming `v_{i,1}` as `t_i`, the
residual is exactly `J`. Hence `C(F)>=C(J)+3m`.

## Quotient transfer boundary

The substitution is functionally surjective onto the `t` inputs: every
assignment to all `t_i` is realized by setting `v_{i,1}=t_i` and the other
three positive variables to zero. Hence distinct inherited row-cofactor
functions remain distinct after substitution, so all `Q_J` inherited classes
survive.

Every inherited gate after substitution depends on the four variables of
block `i` only through their full OR `P_i`. The prefix `a_i` or `b_i` is not
constant on fibers of `P_i`: a later positive variable can make `P_i=1`
while the prefix remains zero. Thus no inherited row cofactor equals a prefix.
Essential supports separate all `2m` prefixes from one another.

The output `P_i` itself is fiber-constant and can equal an inherited gate
whose selected-row cofactor is `t_i`. Minimum global circuits contain no gate
computing raw `t_i` globally, but row restriction can erase base dependence,
so this possible collision cannot be discarded.

If `Q_J` is the inherited two-row quotient size and `b` is the number of
indices for which `t_i` occurs as an inherited cofactor on at least one row,
the substituted minimum circuit satisfies

`Q_F>=Q_J+3m-b`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted base-tail circuits, fresh implication inputs, exact OR substitutions, restrictions, and two-row semantic quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum implication circuit; uniform disjoint substitutions |
| Circuit size | Exact identity `C(F)=C(J)+3m`; quotient transfer at least `3m-b` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean functional substitution and semantic row cofactors only |
| Asymptotic quantifiers | Every nonconstant finite `H`, every `m>=1`, every qualifying disjoint input family, and every base-only row pair |
| Regime | Exact size reduction and bounded quotient-transfer loss; not implication stability, a SAT lower bound, or a terminal result |
