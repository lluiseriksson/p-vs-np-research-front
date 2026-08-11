# LEMMA-238 — zero overhead is exactly a coordinate straight-line ordering

**Label: PROVED**

Let `A` be a finite set of admissible Boolean input signals, let `P` be a
finite Boolean vector, and let `F_A(P)` be the set of its `q=q_A(P)` distinct
coordinate functions not equal to a signal in `A`. Then

```text
C_A(P)=q
```

if and only if the functions of `F_A(P)` admit an ordering
`f_1,...,f_q` in which every `f_i` is obtained by one allowed gate operation
from signals in `A` and functions among `f_1,...,f_{i-1}`.

For AND or OR there are two operands; for NOT there is one. Repeated operands
and arbitrary fanout are allowed. Call such an ordering a coordinate
straight-line ordering.

## Proof

Suppose first that `C_A(P)=q` and choose a `q`-gate minimum circuit. By
LEMMA-236 every gate is the source of one member of `F_A(P)`, and distinct
members use distinct gates. There are exactly `q` of each, so this association
is a bijection. Topologically order the circuit gates and transfer that order
to their coordinate functions. Every gate operand is then either an
admissible input signal or the output of an earlier gate, which is an earlier
coordinate function. This gives the required ordering.

Conversely, a coordinate straight-line ordering directly constructs a
`q`-gate circuit, one gate per ordered function. LEMMA-236 supplies the
matching lower bound `C_A(P)>=q`, so equality follows.

The characterization is existential and semantic. It neither gives an
efficient procedure for finding the ordering nor makes an earlier coordinate
gate expendable: later coordinate gates may depend on it.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite constant-free multi-output AND/OR/NOT DAG over named admissible Boolean input signals |
| Uniform/non-uniform | Every finite non-uniform Boolean vector and its minimum shared DAG |
| Circuit size | Exact equality `C_A(P)=q_A(P)` iff a `q_A(P)`-step coordinate ordering exists |
| Circuit depth | Unrestricted; ordering depth equals its dependency-DAG depth |
| Fan-in | AND/OR two; NOT one; repeated operands, fanout, and output sharing unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean coordinate functions and straight-line dependencies |
| Asymptotic quantifiers | Every finite admissible signal set, vector, coordinate set, and minimum realizing DAG |
| Regime | Exact worst-case zero-overhead characterization; not an ordering algorithm, endpoint payment, SAT lower bound, or terminal result |
