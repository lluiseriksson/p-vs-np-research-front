# LEMMA-227 — a zero-defect binary gate is masks plus a swap

**Label: PROVED**

At one base assignment in code `10`, let the old binary-gate inputs be `a,b`,
the new inputs be `a'=a xor alpha`, `b'=b xor beta`, and suppose the binary
output defect is zero. Then the following pointwise classification is exact.

For AND:

```text
(alpha,beta) = (1,0)  implies b=0,
(alpha,beta) = (0,1)  implies a=0,
(alpha,beta) = (1,1)  implies a != b.
```

For OR:

```text
(alpha,beta) = (1,0)  implies b=1,
(alpha,beta) = (0,1)  implies a=1,
(alpha,beta) = (1,1)  implies a != b.
```

There is no restriction when `(alpha,beta)=(0,0)`. Conversely, the displayed
condition in each case is sufficient for zero output defect. On the common
support `alpha=beta=1`, the input pair therefore swaps `01<->10`; both AND
outputs are zero and both OR outputs are one.

For Boolean defect functions, this partitions the base domain into two
exclusive one-sided mask regions and one overlap swap region. The partition is
semantic and supplies no physical path separation or resource count.

## Proof

Substitute the four values of `(alpha,beta)` into LEMMA-224. For AND the defect
is `a beta xor b alpha xor alpha beta`; for OR it is that expression further
xored with `alpha xor beta`. The three nonzero cases reduce to the displayed
single-bit conditions. When both differences are one, `a'=NOT a` and
`b'=NOT b`; the condition `a!=b` makes the new ordered pair the old pair
reversed.

## Model card

| Field | Value |
|---|---|
| Computational model | One paired unrestricted AND/OR binary gate at code `10`, with arbitrary Boolean input functions |
| Uniform/non-uniform | Every finite non-uniform paired gate interface and every base assignment |
| Circuit size | One local binary gate; no global size conclusion |
| Circuit depth | One local layer inside unrestricted ambient depth |
| Fan-in | AND/OR two; fanout unrestricted outside the local interface |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean differences analyzed over `F_2` |
| Asymptotic quantifiers | Every old input pair, difference pair, assignment, and both binary operations |
| Regime | Exact worst-case local classification; not a topology theorem, SAT lower bound, or terminal result |
