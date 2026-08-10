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

## ENC-006 — complete local operator-bit square

Fix the twelve-bit prefix template

`Q_b = 01 b V 11 V`,

where `b` ranges over the four two-bit node tokens and the suffix has positive
length. Its exact SAT-gamma residuals are

| `b` | Parse/residual |
|---|---|
| `10` | `AND(OR(V,NOT(V)),y)`; residual `SAT-gamma(y)` |
| `01` | `AND(AND(V,NOT(V)),y)`; residual zero |
| `00` | the prefix already completes `AND(variable 7,V)`; nonempty `y` is trailing, so residual zero |
| `11` | the prefix already completes `AND(NOT(V),NOT(V))`; nonempty `y` is trailing, so residual zero |

Thus on this entire two-bit cofactor square the decision function is exactly

`b_1 AND NOT(b_2) AND SAT-gamma(y)`.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix parser and four coordinate cofactors |
| Uniform/non-uniform | Uniform fixed-template calculation |
| Circuit size | No lower-bound conclusion; the residual identity has a three-gate selector form |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every suffix length `m>=1` and every `m`-bit suffix |
| Regime | Exact total-language decision including malformed suffixes |

## ENC-007 — equal-length conditioned-SAT pair

Let

`A_1 = NOT(NOT(AND(V,V)))`

and

`A_0 = AND(NOT(V),NOT(V))`.

Both encodings have length 12; `A_1` is equivalent to `V` and `A_0` to
`NOT(V)`. Define the equal-length fourteen-bit prefixes

`R_b = 01 A_b`, for `b in {0,1}`.

For every suffix `y`, `R_b y` is valid iff `y` is valid. Its SAT-gamma value is
one exactly when `y` has a satisfying assignment with variable identifier 1
fixed to `b`. Denote this total residual language by `CSAT_b(y)`, with malformed
suffixes rejected. Then, for every binary string,

`SAT-gamma(y) = CSAT_0(y) OR CSAT_1(y)`.

The identity holds even when identifier 1 is absent from `y`, because any
satisfying assignment can be extended with either value; it also holds on
malformed strings because all three functions reject.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix formulas, conditioned assignments, and two equal-length coordinate restrictions |
| Uniform/non-uniform | Uniform fixed-prefix construction |
| Circuit size | No lower bound; supplies a two-output decomposition of SAT |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every suffix length and every binary suffix |
| Regime | Worst-case exact total-language decision; malformed suffixes reject |

## ENC-008 — many equal-length conditioned pairs

ENC-007 generalizes to every positive identifier `j`. If `j` has binary length
`ell`, then `enc(variable j)` has length `2ell+1`. Replacing `V` by this
variable in the two conditioned formulas gives

`A_{j,1}=NOT(NOT(AND(V_j,V_j)))`,

`A_{j,0}=AND(NOT(V_j),NOT(V_j))`.

Both have length `4ell+8`, so the prefixes `R_{j,b}=01 A_{j,b}` have common
length `4ell+10`. For every suffix `y`, their residuals are satisfiability of
`y` conditioned on identifier `j` being `b`, and their OR is exact SAT-gamma.

Consequently all `2^(ell-1)` identifiers of bit length `ell` supply distinct
conditioned pairs at the same parent and suffix lengths. This is projection
supply only; it gives no averaging or circuit-loss theorem.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix formulas and conditioned assignments for arbitrary variable identifiers |
| Uniform/non-uniform | Uniform prefix construction; later identifier choice may be non-uniform by circuit and length |
| Circuit size | No lower bound; `2^(ell-1)` candidate two-output decompositions at prefix length `4ell+10` |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None in construction; identifier may be selected non-uniformly in a gate theorem |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `ell>=1`, every identifier with that bit length, and every binary suffix |
| Regime | Worst-case exact total-language decision; malformed suffixes reject |

## ENC-009 — complementary shattering witnesses

**Label: PROVED**

Fix a bit length `ell>=1` and a nonempty set `J` of `R` distinct identifiers
of that bit length. For every bit vector `a in {0,1}^J`, form

`Phi_a = AND_{j in J} A_{j,a_j}`,

using any one fixed binary conjunction order, where the equal-length literal
gadgets `A_{j,b}` are those from ENC-008. Every `Phi_a` has the common length

`L=R(4ell+10)-2`.

Its satisfying assignments are exactly those extending `a` on `J`. Therefore,
for every `j in J` and `b in {0,1}`,

`SAT-gamma(R_{j,b} Phi_a)=1 iff b=a_j`.

As `a` varies, the vector of all `2R` conditioned outputs realizes all `2^R`
complementary patterns: in each identifier pair exactly one output is one.
Applying the same number of double negations to every `Phi_a` preserves the
statement and increases the common suffix length by any multiple of four.

### Proof

ENC-008 gives `|A_{j,0}|=|A_{j,1}|=4ell+8`. Joining `R` gadgets uses `R-1`
two-bit AND tokens, which gives the displayed length. Each gadget is
semantically the literal `x_j=a_j`; their conjunction is satisfiable exactly
under extensions of `a`. Adding the conditioned prefix conjoins the additional
literal `x_j=b`, so consistency and hence satisfiability hold exactly when
`b=a_j`. Double negation preserves parsing and semantics by ENC-002. QED.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formulas and all false/true conditioned residual outputs for an identifier block |
| Uniform/non-uniform | Uniform witness construction and evaluation statement |
| Circuit size | No lower bound; `2^R` explicitly witnessed output patterns at common suffix length `R(4ell+10)-2+4d` |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `ell>=1`, every nonempty finite identifier subset of that bit length, every assignment vector, and every integer padding count `d>=0` |
| Regime | Worst-case exact total-language decision on valid witness formulas |

## ENC-010 — all-sufficiently-large-length witness padding

**Label: PROVED**

Let `F` be a valid formula that does not contain identifier 1, and suppose any
separately forced variable also has identifier different from 1. For every
integer `d>=12`, there is a valid formula `Pad_d(F)` of length `|F|+d` such
that `Pad_d(F)` is satisfiable under the forced condition exactly when `F` is.

Write `b=d mod 4`, with `0<=b<=3`, and

`a=(d-5b)/4`.

For `d>=12`, `a` is a nonnegative integer. Apply `a` double-negation wrappers,
each adding four bits, then apply `b` wrappers of the form

`AND(V_1, hole)`,

each adding `2+|V_1|=5` bits. The total increase is `4a+5b=d`. Double
negation preserves the formula, and the new positive variable can always be
set true independently, so satisfiability under every condition on identifiers
other than 1 is unchanged. QED.

For every fixed `0<c<1`, choose
`ell=floor(c log_2 n)`, the full bit-length-`ell` block `J`, and
`R=|J|`. ENC-009's base witness length is `R(4ell+10)-2=O(n^c log n)`.
Consequently, for every sufficiently large `n`, ENC-010 pads every witness to
the exact suffix length `n-(4ell+10)`. Thus the complementary matrix exists at
every sufficiently large parent length, not only on a congruence subsequence.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formulas, double-negation padding, and conjunction with one fresh positive variable |
| Uniform/non-uniform | Uniform explicit padding construction |
| Circuit size | No circuit lower bound; exact length increase by every integer `d>=12` |
| Circuit depth | Unrestricted in later applications |
| Fan-in | Encoded AND two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every valid source avoiding identifier 1, every forced identifier other than 1, and every integer increase `d>=12`; every sufficiently large `n` in the `0<c<1` corollary |
| Regime | Worst-case exact satisfiability preservation; total-language parser remains exact |

## ENC-011 — formula-code Hamming-weight parity

**Label: PROVED**

For a valid SAT-gamma formula `F`, let `L(F)` be its number of variable leaves
and let the leaf identifiers, with multiplicity, be `j_1,...,j_L`. Then

`weight(F) = L(F)-1 + sum_i popcount(j_i) (mod 2)`,

where `weight` is the number of one bits in the complete encoding.

Indeed, a rooted unary/binary formula tree with `L` leaves has exactly `L-1`
binary nodes. Every AND token `01` and OR token `10` contributes one one-bit;
every NOT token `11` contributes two and vanishes modulo two. A variable token
`00 gamma(j)` contributes the Hamming weight of `gamma(j)`, which is exactly
the popcount of the binary representation of `j`. Summing proves the formula.

Two equal-length formula encodings with the same multiset of leaf identifiers
therefore have equal weight parity and must be at even Hamming distance. More
strongly, every formula using only identifier 1 has odd weight, because

`(L-1)+L popcount(1)=2L-1`.

Thus no two identifier-1 formulas—of any semantics or length—are at Hamming
distance one. This proves the unbounded absence suggested by EXP-001, but the
finite experiment remains separately labeled `NUMERICAL` and is not promoted.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma unary/binary parse trees and binary encodings |
| Uniform/non-uniform | Uniform combinatorial identity |
| Circuit size | Not applicable; encoding distance theorem only |
| Circuit depth | Arbitrary formula depth |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Parity arithmetic over integers modulo two only |
| Asymptotic quantifiers | Every valid finite SAT-gamma formula; every pair with the stated leaf-multiset condition |
| Regime | Exact syntax-level theorem; no circuit lower-bound implication |

## ENC-012 — the assignment witnesses are an affine subspace

**Label: PROVED**

Fix a same-bit-length identifier block `J` of size `R`, a fixed conjunction
tree, and the ENC-009 formulas `Phi_a` indexed by `a in {0,1}^J`. Let `y_0`
be the encoding for the all-zero assignment. For each `j`, define

`d_j = y_0 XOR y_{e_j}`,

where `e_j` is the unit assignment at `j`. Then

`y_a = y_0 XOR XOR_{j:a_j=1} d_j`.

The support of `d_j` lies entirely inside the fixed substring occupied by the
literal gadget `A_{j,a_j}`. These supports are pairwise disjoint, and every
`d_j` is nonzero because `A_{j,0}` and `A_{j,1}` are different encodings.
Hence the directions are linearly independent over `F_2`, and the witness set
is an exact `R`-dimensional affine subspace of the suffix cube.

ENC-010 applies the same fixed padding wrapper to every witness. The wrapper
bits cancel in every XOR difference, so the affine-subspace statement persists
at every sufficiently large exact suffix length. On this affine subspace,

`SAT-gamma(R_{j,b} y_a)=1 iff b=a_j`.

Thus the conditioned-output matrix is the exact complementary INDEX/XNOR
matrix on an affine subspace, not merely an arbitrary collection of `2^R`
witness strings.

LEMMA-028 audits the exact logical strength of this observation. The same
row/subspace values admit a total Boolean extension of size `O(R log R)`.
Consequently ENC-012 supplies structured SAT witnesses, but a circuit-loss
argument must also use SAT's behavior away from this affine table.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma assignment formulas, coordinate XOR geometry, and all conditioned identifier outputs |
| Uniform/non-uniform | Uniform explicit affine embedding |
| Circuit size | No lower bound; `R` independent affine directions inside the suffix input cube |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine geometry over `F_2` only; Boolean circuit model remains unchanged |
| Asymptotic quantifiers | Every finite same-bit-length identifier block, every assignment vector, and every common ENC-010 padding length |
| Regime | Worst-case exact total-language evaluation on an affine witness subspace |

## ENC-013 — exact one-bit conditioning gadgets

**Label: PROVED**

Let `V_j=00 gamma(j)` be the variable formula for identifier `j`. For `j=1`,
put `k=3`. More generally, let `j` have bit length `L>=2` and binary form
`11s`, where `|s|=L-2`, and let `k` have binary form `1s11`. Define

`B_{j,1}=OR(AND(V_j,NOT(V_k)),V_j)`

and

`B_{j,0}=OR(AND(V_j,NOT(V_j)),NOT(V_j))`.

These formulas are pointwise equivalent to `V_j` and `NOT(V_j)`, respectively,
for every assignment of every variable, including `k`. This follows from
absorption and contradiction:

`(x_j AND NOT x_k) OR x_j = x_j`,

`(x_j AND NOT x_j) OR NOT x_j = NOT x_j`.

The two encodings have equal length and Hamming distance exactly one. For the
general construction,

`V_j=0^(L+1) 11s`

and

`V_k=0^(L+2) 1s11`.

The gadget codes have the common initial string `10 01 V_j 11` and then
contain, respectively,

`V_k V_j`

and

`V_j 11 V_j`.

The suffix `V_j` is common. The strings
`V_k=0^(L+2)1s11` and `V_j 11=0^(L+1)11s11` differ only in the first `1`
after the common `L+1` zeros. The special pair `j=1,k=3` has the same direct
identity: `V_3=00011` and `V_1 11=00111`.

Since `|V_j|=2L+1` and `|V_k|=|V_j|+2`, each gadget has length

`3|V_j|+8=6L+11`.

Therefore the prefixes

`Q_{j,b}=01 B_{j,b}`

have common length `6L+13`, differ in exactly one bit, and satisfy for every
suffix string `y`

`SAT-gamma(Q_{j,b} y)=SAT-gamma(y with x_j forced to b)`.

The equivalence is pointwise, so this remains exact even if identifier `k`
occurs in `y`; no freshness assumption is hidden. Their OR is exact
`SAT-gamma(y)`.

For each `L>=2`, the supported identifier set

`J_L^*={j in [2^(L-1),2^L): the binary code of j begins 11}`

has size `2^(L-2)`. Thus a polynomial-size identifier block survives, every
pair has the same `O(log n)` prefix length, and each pair is an edge of the
Boolean prefix cube.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formulas, pointwise Boolean equivalence, and complete prefix restrictions |
| Uniform/non-uniform | Uniform explicit gadget construction and identifier map `j -> k` |
| Circuit size | No lower bound; exact prefix length `6L+13` and Hamming distance one |
| Circuit depth | Formula depth three inside each literal gadget; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `L>=2`, every bit-length-`L` identifier beginning `11`, both polarities, and every suffix string; plus the explicit `j=1` base case |
| Regime | Worst-case exact total-language conditioning; malformed suffixes reject and auxiliary identifiers may occur in the suffix |

## ENC-014 — the adjacent rows are one affine parallel-edge cube

**Label: PROVED**

Fix `L>=2`, put `d=L-2`, and index the supported identifiers by

`j(s)=(11s)_2` for `s in {0,1}^d`.

All `Q_{j(s),b}` have length `p=6L+13`. Their unique polarity-flip coordinate
is the same zero-based coordinate

`q_L=3L+10`

for every `s`. The positive row has zero there and the negative row has one.

Let `r_0=Q_{j(0^d),1}` and let `e` be the unit vector at coordinate `q_L`.
For each context coordinate `i`, let

`d_i=r_0 XOR Q_{j(e_i),1}`.

Each `d_i` has Hamming weight three: the corresponding bit of `s` occurs once
in the first `V_j`, once in the middle `V_k` (or aligned `V_j 11`), and once
in the final `V_j`. These supports are pairwise disjoint and avoid `q_L`.
Consequently

`Q_{j(s),b}=r_0 XOR (1-b)e XOR XOR_{i:s_i=1} d_i`.

The complete `2^(L-1)`-row family is therefore an affine subspace of the
prefix cube with `L-1` independent disjoint directions. It is a parallel
matching of all `2^(L-2)` edges in one unit coordinate, with an
`(L-2)`-dimensional repeated-coordinate affine context cube.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix strings and Hamming/XOR geometry |
| Uniform/non-uniform | Uniform explicit affine embedding of the context and polarity parameters |
| Circuit size | No lower bound; row length `6L+13`, one unit direction, and `L-2` weight-three directions |
| Circuit depth | Unrestricted in later applications |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine geometry over `F_2` only; later computing circuits remain Boolean |
| Asymptotic quantifiers | Every `L>=2`, every context `s`, and both polarities |
| Regime | Exact syntax-level geometry for worst-case total-language restrictions |

## ENC-015 — the one-bit off-cube halo has six exact SAT semantics

**Label: PROVED**

Fix `L>=3`, a supported identifier `j=(11s)_2`, and one coordinate of the
nonempty context string `s`. Let `j'` toggle that coordinate, and let `k,k'`
be the ENC-013 auxiliary identifiers for `j,j'`. A context coordinate occurs
three times in each row `Q_{j,b}`. Toggle its first, middle, or final
occurrence independently. Each resulting prefix:

- has the same length `6L+13` as `Q_{j,b}`;
- differs from `Q_{j,b}` in exactly one bit;
- remains a well-formed prefix `01 B` with one formula hole; and
- lies outside the ENC-014 affine cube, because a context direction toggles
  all three occurrences together.

Writing variables as `x_j,x_j',x_k,x_k'`, the six gadget functions are
exactly:

| Base row | Flipped occurrence | Halo gadget function |
|---|---|---|
| positive | first | `x_j OR (x_j' AND NOT x_k)` |
| positive | middle | `x_j` |
| positive | final | `x_j' OR (x_j AND NOT x_k)` |
| negative | first | `NOT x_j` |
| negative | middle | `NOT x_j OR NOT x_j'` |
| negative | final | `NOT x_j'` |

These identities follow by substituting `V_j,V_j',V_k,V_k'` into the ENC-013
syntax and applying absorption or contradiction. In particular, the positive
middle neighbor duplicates `Q_{j,1}`, and the negative first neighbor
duplicates `Q_{j,0}`. The negative final neighbor is the adjacent-context row
`Q_{j',0}` semantically, although its syntax differs from that cube row.

For an arbitrary suffix formula `phi`, write

`H_{a,b}(phi)=SAT(phi AND (x_a=b))`.

The negative-middle residual obeys the exact union identity

`SAT(phi AND (NOT x_j OR NOT x_j'))=H_{j,0}(phi) OR H_{j',0}(phi)`.

The two mixed positive residuals obey

`SAT(phi AND (x_j OR (x_j' AND NOT x_k)))`

`=H_{j,1}(phi) OR SAT(phi AND x_j' AND NOT x_k)`

and

`SAT(phi AND (x_j' OR (x_j AND NOT x_k)))`

`=H_{j',1}(phi) OR SAT(phi AND x_j AND NOT x_k)`.

These are satisfiability identities, not pointwise Boolean identities between
the disjuncts. They hold for every suffix, including suffixes that mention the
auxiliary identifiers. No freshness, promise, or distribution is assumed.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formula prefixes, pointwise gadget semantics, and complete suffix restrictions |
| Uniform/non-uniform | Uniform explicit construction for every supported identifier and context coordinate |
| Circuit size | No lower bound; every halo prefix has length `6L+13` and Hamming distance one from its base row |
| Circuit depth | Halo gadget formulas have constant depth; later computing circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Hamming/XOR geometry over `F_2` only; SAT semantics remain Boolean |
| Asymptotic quantifiers | Every `L>=3`, every `j=(11s)_2`, every context coordinate, both polarities, every suffix formula and assignment |
| Regime | Worst-case exact total-language behavior; all six halo rows are valid rather than malformed or promise inputs |

## ENC-016 — the three context occurrences form one full affine formula cube

**Label: PROVED**

Fix `L>=3`, put `d=L-2`, and for `a,b,c in {0,1}^d` define

`j(a)=(11a)_2` and `k(b)=(1b11)_2`.

Vary the three context occurrences in ENC-013 independently and define

`P^+_{a,b,c}=01 OR(AND(V_{j(a)},NOT(V_{k(b)})),V_{j(c)})`,

`P^-_{a,b,c}=01 OR(AND(V_{j(a)},NOT(V_{j(b)})),NOT(V_{j(c)}))`.

Every one of these strings is a valid one-hole formula prefix of length
`p=6L+13`. For every suffix formula `phi`, its exact SAT residual is

`SAT(phi AND ((x_{j(a)} AND NOT x_{k(b)}) OR x_{j(c)}))`

for the positive row and

`SAT(phi AND ((x_{j(a)} AND NOT x_{j(b)}) OR NOT x_{j(c)}))`

for the negative row. No involved identifier is assumed fresh in `phi`.

The `2^(3d+1)` strings form an affine subspace of `{0,1}^p`. Starting from
`P^+_{0,0,0}`, each bit of `a`, `b`, or `c` toggles one distinct prefix
coordinate, and polarity toggles the same coordinate `q_L=3L+10` as in
ENC-014. These `3d+1` unit directions have disjoint supports, so the map

`(polarity,a,b,c) -> P^{polarity}_{a,b,c}`

is an injective affine embedding.

ENC-014 is its diagonal subspace `a=b=c`. ENC-015 is exactly the set of rows
obtained from that diagonal by changing one of the three blocks in one
coordinate. Double flips of two copies of the same context bit are therefore
not new lookup locations: they are single-flip halo rows based at the
neighboring diagonal context. The full cube resolves all such collision
descriptions automatically.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formula prefixes, complete suffix restrictions, and syntax-level affine geometry |
| Uniform/non-uniform | Uniform explicit construction for all three independent context blocks and both polarities |
| Circuit size | No lower bound; `2^(3L-5)` distinct rows, each of length `6L+13` |
| Circuit depth | Encoded condition formulas have constant depth; later computing circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix geometry over `F_2`; SAT semantics remain Boolean |
| Asymptotic quantifiers | Every `L>=3`, every `a,b,c in {0,1}^{L-2}`, both polarities, and every suffix formula |
| Regime | Worst-case exact total-language behavior; every expanded-cube row is a valid formula prefix |

## ENC-017 — exact expanded-row equality classes and multiplicities

**Label: PROVED**

Write the ENC-016 conditions as

`g^+_{a,b,c}=x_c OR (x_a AND NOT u_b)`

and

`g^-_{a,b,c}=NOT x_c OR (x_a AND NOT x_b)`,

where `(x_s)_{s in [R]}` and `(u_s)_{s in [R]}` are disjoint variable
families and `R=2^(L-2)`. The positive conditions have exactly

`R^3-R^2+R`

logical-equivalence classes:

- `a=c` gives the `R` single literals `x_a`, each with multiplicity `R` as
  `b` varies;
- every ordered triple with `a!=c` gives a distinct function, each with
  multiplicity one.

The negative conditions have exactly

`R + binom(R,2) + R(R-1)(R-2)`

classes:

- `a=b` or `b=c` gives a single literal `NOT x_t`; each of the `R` literal
  classes has multiplicity `2R-1`;
- `a=c!=b` gives `NOT x_a OR NOT x_b`; one class exists for every unordered
  pair `{a,b}`, and each has multiplicity two;
- every all-distinct ordered triple gives a distinct three-variable function
  of multiplicity one.

No positive condition is equivalent to a negative condition. Thus all
`2R^3` expanded rows induce exactly

`(4R^3-7R^2+7R)/2`

logical classes.

For every sufficiently large fixed suffix length, these are also the exact
equality classes of the corresponding `SAT-gamma` residual functions. If two
conditions are inequivalent, choose an assignment on their at most six
involved identifiers where their values differ and encode the conjunction
fixing that assignment. The resulting suffix distinguishes the two SAT
residuals. Identifier 1 is fresh, so ENC-010 padding extends the witness to
every sufficiently large suffix length. Logical equivalence gives the reverse
implication immediately.

For completeness, the uniqueness claims follow from essential-variable
roles. In a nonsingle positive condition, `u_b` is the unique auxiliary
variable; setting it to one identifies the positive disjunct `x_c`, and then
`x_a` is determined. In an all-distinct negative condition, `c` is the unique
variable whose value zero forces the function to one; setting `x_c=1` leaves
the ordered term `x_a AND NOT x_b`. The remaining classes have different
essential-variable counts, except that the two orientations of a NAND pair
are deliberately equivalent.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact Boolean condition functions and their exact SAT-gamma residuals under complete expanded-cube prefix restrictions |
| Uniform/non-uniform | Uniform classification and explicit distinguishing suffix witnesses |
| Circuit size | No lower bound; exact distinct-output count `(4R^3-7R^2+7R)/2` among `2R^3` rows |
| Circuit depth | Unrestricted in later circuit applications |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; finite condition identities are Boolean |
| Asymptotic quantifiers | Every `R=2^(L-2)` with `L>=3`; exact SAT-residual classification at every sufficiently large compatible suffix length |
| Regime | Worst-case exact total-language residual functions; malformed suffixes reject |

## ENC-018 — SAT residual columns are unions of assignment columns

**Label: PROVED**

Let `g_1,...,g_M` be any finite Boolean condition family on a variable set
`V`, including the ENC-016 family. For an assignment `alpha in {0,1}^V`, let

`v_alpha=(g_i(alpha))_{i=1}^M`.

For every nonempty assignment set `A`, a DNF suffix formula whose satisfying
assignments projected to `V` are exactly `A` realizes the SAT-residual column

`OR_{alpha in A} v_alpha`.

Conversely, every suffix formula `phi` has a projected satisfying-assignment
set `A_phi`, and

`(SAT(phi AND g_i))_i = OR_{alpha in A_phi} v_alpha`,

with the empty OR giving the zero column. Thus, without a fixed-length bound,
the exact residual-column set is the union closure of the assignment columns.
Every individual finite witness can be padded to all sufficiently large
lengths by ENC-010.

There is a uniform fixed-length consequence with compact witnesses. On the
`R` diagonal literal pairs, independently prescribe for each `x_s` whether a
satisfying assignment may use only zero, only one, or both values. The
conjunction fixing the singleton choices and leaving the other variables free
has length `O(RL)` and realizes the corresponding pair of outputs. Therefore,
whenever the suffix budget dominates `O(RL)`, the diagonal family realizes
exactly `3^R` nonzero ternary patterns, plus the all-zero unsatisfiable or
malformed pattern. ENC-009's `2^R` complete-assignment columns are the special
case with no variable left free.

### Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma residual outputs under a finite family of complete formula-prefix restrictions |
| Uniform/non-uniform | Uniform DNF and partial-assignment witness construction |
| Circuit size | No lower bound; `3^R` compact nonzero diagonal output patterns from suffixes of length `O(RL)` |
| Circuit depth | Witness formulas unrestricted; later computing circuits unrestricted |
| Fan-in | Encoded witness formulas use binary AND/OR and unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; output columns form a Boolean OR-closure |
| Asymptotic quantifiers | Every finite condition family for unbounded witness length; every `R=2^(L-2)` and sufficiently large compatible suffix budget for the compact `3^R` diagonal family |
| Regime | Worst-case exact total-language satisfiability; arbitrary formulas represent sets of witnesses, not a promise distribution |

## Reference implementation

`verification/sat_encoding.py` is an iterative reference parser, evaluator,
and context constructor. Its tests exercise the grammar and projections, but test success is
infrastructure evidence, not `FORMALLY VERIFIED` mathematics.
