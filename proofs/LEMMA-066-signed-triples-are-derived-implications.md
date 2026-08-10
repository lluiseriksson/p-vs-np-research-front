# LEMMA-066 — signed-triple tails are exactly derived implication tails

**Label: PROVED**

## Statement

Let `H(x)` be any nonconstant Boolean function, on inputs disjoint from all
variables below. For fresh pairwise-disjoint inputs define

`J=H AND AND_{i=1}^m (p_i OR NOT t_i)`

and

`F=H AND AND_{i=1}^m (p_i OR NOT(u_i AND v_i))`.

Then, for unrestricted fan-in-two AND/OR and fan-in-one NOT circuits,

`C(F)=C(J)+m`.

Moreover, take any minimum circuit for `J`, replace each raw input `t_i` by a
fresh gate `A_i=u_i AND v_i`, and retain the rest of the circuit. The result
is a minimum circuit for `F`. Under any family of restrictions involving only
the base inputs `x` for which every residual `H_e` is nonconstant, the `m`
functions `A_i` give `m` additional distinct, active, row-independent semantic
quotient classes beyond those inherited from the `J` circuit.

## Upper bound

Compute every `A_i=u_i AND v_i` with one gate and feed these functions into a
minimum circuit for `J` in place of its raw inputs `t_i`. This computes `F`
with `C(J)+m` gates.

## Lower bound

Starting from any circuit for `F`, successively restrict `v_i=1`. Before its
restriction, each `v_i` is essential: choose a base input with `H=1`, set
`p_i=0,u_i=1`, toggle `v_i`, and satisfy all other clauses. The earliest-
dependent-gate restriction argument removes at least one gate each time.

After all `m` restrictions the residual, after renaming `u_i` as `t_i`, is
exactly `J`. Therefore

`C(F)>=C(J)+m`,

matching the construction.

## Quotient transfer

A globally minimum circuit cannot contain a gate whose semantic function is
a raw input: replacing all uses of that gate by the input deletes it. Thus no
gate of the chosen minimum `J` circuit computes `t_i`.

The substitution `t_i=u_i AND v_i` is functionally injective: every assignment
to the `t_i` is realized by setting `u_i=v_i=t_i`. Hence two distinct gate
functions of `J` remain distinct after substitution, and none becomes one of
the new `A_i`. The `A_i` are pairwise distinct by essential support, remain
active, and do not depend on the restricted base row. The claimed additive
quotient transfer follows.

## Consequence for GATE-004Z

The factorized `K+4m` circuit for `F` is minimum exactly when the corresponding
`K+3m` displayed implication circuit for `J` is minimum. A minimum implication
circuit with `4m` tail classes transfers to a minimum signed-triple circuit
with `5m` tail classes. Thus the standalone and displayed-minimality parts of
GATE-004Z do not bypass the implication bottleneck of GATE-004W; they add one
exactly accounted derived-input gate per clause.

This does not prove or refute either implication minimality or the more general
representation-independent quotient alternative.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, disjoint fresh implications, derived pairwise-AND inputs, restrictions, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum implication circuit; uniform substitution and restriction maps |
| Circuit size | Exact identity `C(F)=C(J)+m`; factorized signed-triple minimality equivalent to displayed implication-tail minimality |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean functional substitution only |
| Asymptotic quantifiers | Every nonconstant finite base `H`, every `m>=1`, every disjoint fresh variable family, and every base-only row family with nonconstant residuals |
| Regime | Worst-case exact total-function identity and quotient transfer; no implication direct sum, SAT lower bound, or terminal result is proved |
