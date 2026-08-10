# Canonical SAT encoding SAT-gamma

**Label: PROVED** for unique parsing, NP membership, NP-hardness, and the
double-negation projection stated below. The separation target remains open.

Fine-grained circuit-size exponents depend on representation. Therefore every
unqualified `SAT` claim in this repository now means the exact total binary
language `SAT-gamma` defined here.

## Integer code

For a positive integer `i`, let `bin(i)` be its ordinary binary representation
with leading bit `1`, and let `ell=|bin(i)|`. Its Elias-gamma code is

`gamma(i) = 0^(ell-1) bin(i)`.

The set of gamma codes is prefix-free. Decoding counts leading zeroes `z`, then
reads exactly `z+1` further bits beginning with `1`; the decoded binary word has
length `z+1`.

## Formula grammar

Formula encodings are prefix expressions:

```text
00 gamma(i)      variable with positive identifier i
01 enc(F) enc(G) conjunction
10 enc(F) enc(G) disjunction
11 enc(F)        negation
```

An encoding is valid only if one complete formula consumes the entire bit
string. Empty strings, truncated nodes, invalid gamma codes, and trailing bits
are malformed.

`SAT-gamma` contains exactly the valid encodings for which some assignment to
the finitely many variable identifiers occurring in the formula makes the root
evaluate to one. Malformed strings are rejected. Variable identifiers may be
large; a certificate contains one bit per distinct identifier occurring in the
input, not one bit per integer below the largest identifier.

## ENC-001 — unique parsing and NP completeness

### Model card

| Field | Value |
|---|---|
| Computational model | Deterministic multitape parser/verifier for prefix formulas |
| Uniform/non-uniform | Uniform |
| Circuit size | Not applicable to parsing/completeness theorem |
| Circuit depth | Not applicable |
| Fan-in | Formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite binary string; polynomial bounds in its bit length |
| Regime | Worst-case exact total-language decision; malformed inputs reject |

Unique parsing follows by induction over the fixed two-bit node token and the
prefix-free gamma code at variable nodes. A deterministic parser scans each bit
a constant number of times and records at most linearly many nodes and total
identifier bits.

For NP membership, guess one truth value for each distinct identifier appearing
in the parsed formula, check consistency of repeated identifiers, and evaluate
the syntax tree. The witness and deterministic verification time are
polynomial in the encoding length.

NP-hardness follows from any standard CNF-SAT instance: number its variables by
positive integers, encode literals using variable/NOT nodes, clauses using OR
trees, and the conjunction using an AND tree. If the source has bit length `s`,
all identifiers are at most `s`, so the target length is `O(s log s)` and the
translation is deterministic polynomial time. Satisfiability is preserved.

Thus `SAT-gamma` is NP-complete and `SAT-gamma notin P` is equivalent to
`P != NP`.

## ENC-002 — double-negation projection

For every binary string `x` and integer `t>=0`, define

`wrap_t(x) = (1111)^t x`.

Each `1111` is two consecutive NOT tokens. Then `wrap_t(x)` is a valid formula
iff `x` is a valid formula, and in the valid case it is satisfiable iff `x` is
satisfiable. Consequently the length-`m` SAT slice is a projection of the
length-`m+4t` slice obtained by fixing the first `4t` bits to one.

This exact self-embedding will be used in GATE-004B. It says nothing about how
many gates a circuit loses after those prefix bits are fixed.

## Reference implementation

`verification/sat_encoding.py` is an iterative reference parser and evaluator.
Its tests exercise the grammar and projections, but test success is
infrastructure evidence, not `FORMALLY VERIFIED` mathematics.
