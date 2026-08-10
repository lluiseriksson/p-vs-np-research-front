# Canonical SAT encoding SAT-gamma

**Label: PROVED** for unique parsing, NP membership, NP-hardness, and the exact
context projections stated below. The separation target remains open.

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

## ENC-003 — exact prefix formula contexts

Let `V=enc(variable 1)`, so `|V|=3`, and define

`T = OR(V,NOT(V))`.

Then `|T|=10` and `T` is true under every assignment. For arbitrary bits `x`,
the context

`AND(T,x)`

adds 12 bits. It is valid exactly when `x` is valid and, when valid, has the
same satisfiability value as `x`. This remains true even if variable
identifier 1 occurs in `x`, because `T` is a tautology for both values.

For nonnegative integers `l,d`, apply `l` such contexts and then `d`
double-NOT contexts. The resulting string has length

`|x| + 12l + 4d`.

The source `x` remains a literal contiguous substring beginning at zero-based
coordinate `12l+4d` and ending at the end of the target. Hence fixing the
prefix gives an exact coordinate projection of the length-`|x|` slice into the
longer slice. Structural induction on the context proves both validity
equivalence and satisfiability equivalence.

The apparently symmetric right context is not exact for this total language.
Let `x=V 11`, a variable followed by a truncated NOT token. Although `x` is
malformed, `AND(x,T)` parses as `AND(V,NOT(T))`, a valid unsatisfiable formula.
Suffix context bits can repair malformed trailing syntax. This counterexample
is recorded as `GATE-004B-RIGHT-CONTEXT — NO-GO` and is why ENC-003 claims only
prefix contexts.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix formulas and coordinate projections |
| Uniform/non-uniform | Uniform prefix-context construction; later circuit application may choose a context non-uniformly |
| Circuit size | Projection statement only; no circuit gate-loss conclusion |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every binary string and every nonnegative integer pair `(l,d)` |
| Regime | Exact validity and satisfiability, including malformed-string rejection |

ENC-003 broadens the attainable prefix lengths but does not diversify which
source coordinates survive. LEMMA-003 separately proves that even a
hypothetical family of all contiguous placements would not support a generic
coordinate-coverage averaging argument.

## ENC-004 — equal-length neutral-prefix family

For every `k>=0` and `0<=l<=k`, let

`P_{k,l}=(1111)^{3(k-l)}(01T)^l`.

Every `P_{k,l}` has length `12k`, and prefixing it to an arbitrary string
preserves exact validity and satisfiability. For fixed `k` these are `k+1`
distinct assignments to the same prefix coordinates, with pairwise Hamming
distance `6|l-j|`. LEMMA-006 proves the exact parser-state and distance claims.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix parser and coordinate restrictions |
| Uniform/non-uniform | Uniform family construction; later circuit selection may be non-uniform |
| Circuit size | No circuit-size conclusion |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `k>=0`, all indices `0<=l,j<=k`, and every binary suffix |
| Regime | Exact total-language validity and satisfiability; malformed suffixes reject |

## ENC-005 — adjacent annihilating prefix

Let `F=AND(V,NOT(V))`, the ten-bit contradiction using `V=variable 1`, and
define the twelve-bit prefix

`Z=01F`.

For every suffix `y`, `Zy` is valid iff `y` is valid. If valid, it encodes
`AND(F,y)` and is unsatisfiable; if malformed, SAT-gamma also rejects it.
Therefore the total residual decision function under prefix `Z` is constant
zero. The neutral prefix `W=01T` from ENC-004 differs from `Z` in exactly the
two bits selecting OR versus AND inside `T` and `F`.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix parser and coordinate restrictions |
| Uniform/non-uniform | Uniform fixed-prefix construction |
| Circuit size | No circuit-size conclusion |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every binary suffix at every length |
| Regime | Exact total-language decision; the residual is zero on valid and malformed suffixes |

## Reference implementation

`verification/sat_encoding.py` is an iterative reference parser, evaluator,
and context constructor. Its tests exercise the grammar and projections, but test success is
infrastructure evidence, not `FORMALLY VERIFIED` mathematics.
