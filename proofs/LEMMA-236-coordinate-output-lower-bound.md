# LEMMA-236 — distinct non-input coordinates require distinct output gates

**Label: PROVED**

Let `A` be a finite named collection of admissible Boolean input signals and
let `P=(p_1,...,p_k)` be a Boolean vector. Let `q_A(P)` be the number of
distinct coordinate functions of `P` that are not equal to any signal in
`A`. Every finite AND/OR/NOT multi-output DAG computing `P` from `A` has at
least `q_A(P)` gates.

Moreover, if a circuit has exactly `q_A(P)` gates, then every gate is the
designated source of at least one non-input coordinate. In particular, an
equality circuit has no gate used only as an auxiliary shared prefix.

## Proof

Every coordinate not already equal to an admissible input signal must be
designated at the output of a gate. Two distinct coordinate functions cannot
be designated at the same gate, because one gate computes one Boolean
function. Choosing one output gate for each distinct non-input coordinate
therefore injects `q_A(P)` functions into the circuit gates.

If the total gate count equals `q_A(P)`, this injection is a bijection. Hence
every gate is a designated coordinate source. This conclusion does not say
that the gate has no fanout into other coordinate gates; it says only that no
additional, auxiliary-only gate exists.

The lemma is insensitive to duplicate coordinates: equal outputs share their
one counted function. It is a multi-output counting theorem, not a lower
bound for any single-output parent or for SAT.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite constant-free multi-output AND/OR/NOT DAG over named admissible Boolean input signals |
| Uniform/non-uniform | Every finite non-uniform vector and circuit |
| Circuit size | At least `q_A(P)` gates; equality leaves no auxiliary-only gate |
| Circuit depth | Unrestricted finite depth |
| Fan-in | AND/OR two; NOT one; fanout and output sharing unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean coordinate functions; no field computation |
| Asymptotic quantifiers | Every finite input-signal set, vector length, coordinate function, and realizing DAG |
| Regime | Exact worst-case multi-output counting theorem; not parent minimality, a SAT lower bound, or terminal result |
