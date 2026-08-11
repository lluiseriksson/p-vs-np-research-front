# LEMMA-149 — minimum circuits exclude inessential-input dependence

**Label: PROVED**

Let `f` be a Boolean function and let `C` be a minimum unrestricted
AND/OR/NOT circuit computing `f`. If an input `x` is inessential for `f`, then
no gate function in `C` depends essentially on `x`.

## Proof

Assume otherwise and choose the earliest gate `v` in a topological ordering
whose computed function depends essentially on `x`. Every gate feeding `v`
computes an `x`-independent function. Therefore an `x`-dependent input of `v`
must be the raw primary input `x`; otherwise an earlier gate would already
depend on `x`.

Fix `x` to either Boolean value. A NOT gate fed by `x` becomes a constant. A
binary AND or OR gate with a raw `x` input becomes either a constant or its
other, already available input function. Thus `v` can be deleted after the
restriction, and constants can be propagated without adding gates. The
restricted circuit has at most `|C|-1` gates.

Because `x` is inessential for `f`, the restricted output is still exactly
`f` as a function of the remaining inputs. This contradicts the minimality of
`C`. Hence no gate function depends essentially on `x`.

The claim concerns semantic gate functions. It does not assert a syntactic
normal form for nonminimum circuits.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits |
| Uniform/non-uniform | Fully non-uniform, exact finite circuit complexity |
| Circuit size | Strict one-gate reduction under the contradictory premise |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and semantic essential dependence only |
| Asymptotic quantifiers | Every finite Boolean function, every minimum circuit, and every inessential primary input |
| Regime | Exact worst-case structural lemma; not a quotient lower bound, SAT lower bound, or terminal result |
