# LEMMA-182 — one-sided masks admit exact semantic erasure

**Label: PROVED**

Use the one-sided branch of LEMMA-181. Thus the first cancellation gate `d`
has path input `p`, other input `q`, and `q_01=q_11=q`, while
`d_01=d_11`. Define an abstract replacement signal `p^dagger` by

- `p^dagger_00=p_00` and `p^dagger_10=p_10`;
- if `d` is OR, `p^dagger_01=p^dagger_11=p_01 AND p_11`;
- if `d` is AND, `p^dagger_01=p^dagger_11=p_01 OR p_11`.

Replacing only the input edge from `p` to `d` by `p^dagger` leaves all four
pair cofactors of `d` unchanged and erases the `01/11` difference on that
edge.

## Proof

The `00` and `10` cofactors are unchanged by definition.

Suppose `d` is OR. Write `a=p_01` and `b=p_11`. The cancellation equality is
`a OR q=b OR q`. Pointwise, if `q=1`, all three expressions
`a OR q`, `b OR q`, and `(a AND b) OR q` are one. If `q=0`, the equality
forces `a=b`, so `(a AND b) OR q=a OR q=b OR q`. Hence replacing both
satisfying cofactors by `a AND b` preserves `d_01=d_11`.

Suppose `d` is AND. If `q=0`, the three outputs are zero. If `q=1`, the
equality `a AND q=b AND q` forces `a=b`, and
`(a OR b) AND q=a AND q=b AND q`. Thus the AND case is also preserved.

The four cofactors determine the full Boolean function at `d`, hence every
downstream gate is semantically unchanged. This conclusion concerns an
abstract edge signal. It neither constructs `p^dagger` in the AND/OR/NOT
basis nor permits globally changing a shared gate `p`.

## Model card

| Field | Value |
|---|---|
| Computational model | Boolean cofactor functions at one binary gate; abstract edge substitution |
| Uniform/non-uniform | Every finite one-sided cancellation identity inside an individual non-uniform parent |
| Circuit size | No size claim; the truth table at `d` is preserved |
| Circuit depth | Unrestricted ambient circuit |
| Fan-in | `d` has fan-in two; `p^dagger` is an abstract signal, not a new basis gate; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice meet/join only |
| Asymptotic quantifiers | Every operational one-sided branch of GATE-004CB and every base assignment |
| Regime | Exact worst-case local semantic identity; not a same-size rewrite, SAT lower bound, or terminal result |
