# Vertical proof map

Date: 2026-08-10

No arrow is accepted unless it has its own proved implication and model card.

```text
P != NP
  <- T-UNIFORM: SAT notin P
  <- T-NONUNIFORM: SAT notin P/poly
  <- V-1: NP notsubseteq P/poly
  <- GATE-002: exponent-ratio uniformization lemma
  <- GATE-003: uniformly construct an unconditional hard-language family
               whose circuit-lower-bound exponent / verifier-time exponent
               is unbounded
```

`T-UNIFORM <- T-NONUNIFORM` is valid because every uniform polynomial-time
decider unrolls to polynomial-size Boolean circuits. `T-NONUNIFORM` and `V-1`
are equivalent through Cook-Levin reductions, provided the reduction's circuit
size blow-up is recorded.

## V-1 model card

Statement: there exists one language `L in NP` such that for every constant
`d`, every Boolean circuit family of size `O(n^d)` fails to decide `L` on at
least one input length (indeed infinitely many lengths).

| Field | Value |
|---|---|
| Computational model | NP verifier on multitape Turing machine; Boolean circuits over `{AND,OR,NOT}` |
| Uniform/non-uniform | Uniform verifier versus non-uniform circuit adversary |
| Circuit size | All polynomial sizes `O(n^d)`, every fixed `d` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice is absorbed into the circuit family |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | `exists L in NP, forall d, forall circuit families, infinitely many failure lengths` |
| Regime | Worst-case exact total-language decision |

## Smallest active brick: GATE-003

Construct, without assumptions, a uniformly indexed sequence `(L_j)` and
unary-polynomial-time computable exponents `a(j), b(j)` satisfying the exact hypotheses of GATE-002,
including

`limsup_j b(j)/a(j) = infinity`,

where `L_j` has a nondeterministic verifier running in `n^{a(j)}` time but no
general Boolean circuits of size `O(n^{b(j)})`.

This is terminal-relevant because GATE-002 proves that such a family yields one
language in `NP` outside `P/poly`. It is not claimed to be solved.

## GATE-003 model card

| Field | Value |
|---|---|
| Computational model | Uniformly indexed nondeterministic multitape verifiers and general Boolean circuits |
| Uniform/non-uniform | Uniform language-family generator; non-uniform lower-bound target |
| Circuit size | `O(n^{b(j)})`, with `limsup b(j)/a(j)=infinity` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None for verifiers; arbitrary polynomial advice represented by circuits on the adversary side |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One effective family; for every `j` its lower bound holds infinitely often; exponent ratio unbounded over `j` |
| Regime | Worst-case exact total-language decision |

## Excluded pseudo-routes

- `NEXP notsubseteq C` for a restricted class `C` has no recorded implication
  to `P != NP`.
- `for every k, there exists L_k in NP` needing more than `n^k` circuits does
  not swap to `there exists L in NP, for every k`.
- A uniform circuit-generation lower bound does not automatically give a
  non-uniform circuit lower bound.
- Average-case, promise, randomized, oracle, algebraic, proof-system, and
  communication results require separate terminal bridges.
