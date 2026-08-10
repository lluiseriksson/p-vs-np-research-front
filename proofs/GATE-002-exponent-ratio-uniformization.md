# GATE-002 — Exponent-ratio uniformization lemma

**Label: PROVED**

## Statement

Let `(L_j)_{j>=1}` be a uniformly indexed family of languages. Suppose there
are positive integers `a(j), b(j)`, computable in time polynomial in unary `j`
with binary output, and one nondeterministic machine `U` such that:

1. on input `(1^j, x)`, `U` decides `x in L_j` using a witness and time at most
   `(|x|+j+2)^{a(j)}`;
2. for every `j`, `L_j` has no general Boolean circuit family of
   `O(n^{b(j)})` gates; and
3. `limsup_j b(j)/a(j) = infinity`.

Then there exists a single language `L* in NP` with
`L* notin P/poly`. Consequently `P != NP`.

### Model card

| Field | Value |
|---|---|
| Computational model | One uniformly indexed nondeterministic multitape verifier; general Boolean circuits |
| Uniform/non-uniform | Uniform construction and verifier; non-uniform lower-bound target |
| Circuit size | Source excludes `O(n^{b(j)})`; target excludes every `O(N^d)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None for verifier; arbitrary polynomial advice is represented by target circuits |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One effective family; each source lower bound holds infinitely often; ratio has infinite limsup; target is one language against every fixed `d` |
| Regime | Worst-case exact total-language decision |

## Construction

For `n=|x|`, encode a well-formed member of `L*` as

`1^j 0 1^n 0 x 0 1^p`,

where `p=(n+j+2)^{a(j)}`. The unary `n` field makes the encoding
self-delimiting; malformed strings are rejected. The total length is
`N=p+j+2n+3`.

The verifier computes `a(j)` from unary `j`, checks the padding length with
integer arithmetic capped at `N+1`, and simulates `U(1^j,x)` for at most
`p <= N` steps with a witness of the same bound. The polynomial-time
computability condition makes parsing polynomial in `N`; universal simulation
takes `N^q` time for one fixed constant `q`. Hence `L* in NP` with a verifier
exponent independent of `j`.

## Lower-bound transfer

Assume for contradiction that `L*` has circuits of size `O(N^d)` for some
fixed `d`. Fix `j`. For every source length `n`, hardwire the tag and padding
bits of the length-`N` circuit for `L*`, leaving only the `n` bits of `x` free.
This gives a circuit for `L_j` of size

`O(N^d) = O(n^{a(j)d})`,

up to a constant depending on fixed `j` and the encoding. No uniform circuit
generator is required.

By the infinite-limsup hypothesis, choose `j` with
`b(j) > a(j)d`. The derived family is then eventually of size
`O(n^{b(j)})`, contradicting hypothesis 2. Since `d` was arbitrary,
`L* notin P/poly`.

Finally, if `P=NP`, then `L* in P`, and every polynomial-time language has
polynomial-size circuits. This contradicts `L* notin P/poly`; therefore
`P != NP`.

## Audit

- The language is single and its NP verifier has one fixed exponent.
- The adversary is fully non-uniform and unrestricted in depth.
- Hardwiring uses no circuit generator or advice beyond the target family.
- The exponent loss is explicit: a target exponent `d` costs source exponent
  `a(j)d`.
- The proof does not supply the hard family; its status is `PROVED`, not a
  terminal success claim.

## Application to the audited Murray-Williams parameters

Their fixed-exponent NP consequence has `a(k)=c k^4/epsilon` and `b(k)=k`, so

`b(k)/a(k)=epsilon/(c k^3)`,

which tends to zero. Therefore this lemma cannot terminalize that bridge.

## Next gate

GATE-003 asks for an unconditional family satisfying the unbounded-ratio
hypothesis, or a different quantifier-stable route to one NP language outside
`P/poly`.
