# LEMMA-224 — exact local propagation of a code-10 defect

**Label: PROVED**

At code `10`, let a gate's old input functions be `a,b`, its new input
functions be `a',b'`, and write the analytical differences

```text
alpha = a xor a',   beta = b xor b'.
```

Then the old/new output defect is exactly

```text
NOT: alpha,
AND: (a AND beta) xor (b AND alpha) xor (alpha AND beta),
OR:  alpha xor beta xor (a AND beta) xor (b AND alpha)
     xor (alpha AND beta).
```

In particular, if only the first input changes (`beta=0`), then

```text
AND defect = alpha AND b,
OR  defect = alpha AND NOT b.
```

Thus NOT cannot be the first gate that kills a nonzero defect. A binary gate
with one unchanged input kills it exactly when the common input masks its
support: `b=0` on the support of `alpha` for AND, or `b=1` there for OR. If
both inputs change, cancellation is governed by the displayed two-defect
interaction and cannot be charged as a one-sided mask without further proof.

## Proof

Over `F_2`, Boolean AND is multiplication and
`a OR b = a xor b xor (a AND b)`. Substitute
`a'=a xor alpha` and `b'=b xor beta`, expand, and cancel the two copies of
each unchanged term. Complementing both versions preserves XOR difference,
giving the NOT identity. Setting `beta=0` gives the two one-sided formulas.
The support characterizations follow pointwise.

The identities classify functions, not physical resources. They do not show
that a cancellation gate is deleted, private, a non-bridge, or available as a
host.

## Model card

| Field | Value |
|---|---|
| Computational model | One old/new unrestricted AND/OR/NOT gate at code `10`, with arbitrary Boolean input functions |
| Uniform/non-uniform | Every finite non-uniform paired gate interface and every base assignment |
| Circuit size | One local gate; no global size conclusion |
| Circuit depth | One local layer inside unrestricted ambient depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted outside the local interface |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions represented analytically over `F_2`; XOR is not an allowed extra circuit gate |
| Asymptotic quantifiers | Every old/new input-function quadruple and every assignment in the code-10 row |
| Regime | Exact worst-case local identity; not a resource theorem, SAT lower bound, or terminal result |
