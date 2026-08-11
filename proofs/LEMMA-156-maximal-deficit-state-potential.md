# LEMMA-156 — exact NOT-state potential at maximal deficit

**Label: PROVED**

Under the hypotheses of LEMMA-155, every minimum circuit `C` for `J_m` is a
variable-read-once formula. Fix any satisfying base assignment `x*`. Starting
with all tail variables zero, raise

`u_1,t_1,u_2,t_2,...,u_m,t_m`

in that order. For a tail assignment `y`, let `D(y)` be the number of NOT
gates of the residual formula whose input evaluates to one (Morizumi's
“down” state). Then:

1. `D=0` at the initial all-zero tail assignment;
2. `D=m` at the final all-one tail assignment;
3. raising each `u_i` increases `D` by exactly one; and
4. subsequently raising `t_i` leaves `D` unchanged.

The conclusions hold for every satisfying `x*`.

## Read-once consequence

LEMMA-155 gives output-cone cycle rank zero. The connected undirected output
cone is therefore a tree. A primary input with two outgoing wires would have
two distinct paths to the output, creating an undirected cycle. Hence every
essential input has exactly one occurrence, as does every internal gate
output. Thus `C` is variable-read-once as well as fanout-one.

## Exact potential proof

After fixing `x*`, LEMMA-155 leaves the same `m` NOT gates in a formula for
`W_m`. Morizumi's lower-bound argument proves the following two facts for any
formula along any increasing input step:

- `D` never decreases; and
- if the formula output changes from one to zero, `D` increases by at least
  one.

For completeness, if `a` NOT gates change from down to up during a step, the
formula tree supplies `a` distinct upstream NOT gates changing from up to
down. When the output also falls, its monotone path supplies one additional
distinct up-to-down NOT. Thus the net change is at least zero, or at least
one at an output fall.

On the displayed tail chain, raising `u_i` makes clause `i` false and changes
`W_m` from one to zero. Raising `t_i` repairs that clause and changes the
output back to one. There are exactly `m` falling steps. Therefore

`D(final)-D(initial)>=m`.

But `0<=D<=m` because the formula has exactly `m` NOT gates. Equality is
forced throughout: `D(initial)=0`, `D(final)=m`, every falling step contributes
exactly one, and every intervening rising step contributes zero.

## Boundary

The theorem controls only the number of down-state NOTs. A zero net change
can still hide paired state changes in opposite directions. It therefore does
not match a persistent NOT gate to each clause and does not prove that a
neutral clause restriction prunes a NOT occurrence.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum rank-zero AND/OR/NOT output cones and NOT-state potential along increasing Boolean chains |
| Uniform/non-uniform | Every individual non-uniform endpoint minimum formula; uniform canonical tail chain |
| Circuit size | Exactly `m` NOT gates; potential rises exactly once at each of `m` output falls and never at repairs |
| Circuit depth | Unrestricted read-once formula depth |
| Fan-in | AND/OR two; NOT one; fanout one in the output cone |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean-lattice chains and integer state potential only |
| Asymptotic quantifiers | Every `m>=1`, every maximal-deficit instance, every endpoint minimum circuit, and every satisfying base assignment |
| Regime | Exact worst-case equality-state theorem; not persistent gate matching, clause pruning, a SAT lower bound, or a terminal result |
