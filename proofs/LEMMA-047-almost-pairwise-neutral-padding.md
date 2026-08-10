# LEMMA-047 — two neutral blocks give almost pairwise zero coverage

**Label: PROVED**

## Statement

For `j in {1,2,4,8,16}`, let

- `A_j=01 T_j`, where `T_j=OR(V_j,NOT(V_j))`; and
- `O_j=10 F_j`, where `F_j=AND(V_j,NOT(V_j))`.

Their lengths are respectively among `12,16,20,24,28`, all divisible by
four. Fix any `P>=32` divisible by four. Let `C_P` contain every length-`P`
formula context obtained by placing one or two nonoverlapping blocks from
this set at offsets divisible by four and filling every gap with one bits.

For every coordinate pair `0<=i<=j<P` except

`E={(0,1),(0,2),(1,3),(2,3)}`,

some context in `C_P` has zero at both `i` and `j`. Every context preserves
exact formula validity and satisfiability when applied to an arbitrary source
string.

Consequently, any positive two-literal clause `z_i OR z_j` that is one on all
of `C_P` must use a pair in `E`. The graph `E` has matching number two, so the
disjoint paired-clause tail of LEMMA-046 has only constant length on this
family.

## Semantic proof

Each `A_j` is `AND(true,hole)` and each `O_j` is `OR(false,hole)`. Every run
of ones has length divisible by four and is therefore an even NOT chain.
Nonoverlap and four-divisible block lengths make every intervening run four-
divisible as well. Composition preserves validity exactly and preserves the
source Boolean function whenever valid.

## Coverage proof

ENC-020 already proves that a length-12 or length-16 block can put a zero at
any one outer coordinate. If `j-i>=32`, choose such a placement for each
coordinate. Each interval has length at most 16. Two intervals containing
points at distance at least 32 cannot overlap, so their composition belongs
to `C_P` and zeros both coordinates.

It remains to check `j-i<32`. Because every block start and length is a
multiple of four and the maximum block length is 28, coverage in this range
depends only on:

1. `i mod 4` and `j-i` when both coordinates are at least 28 positions from
   the boundary;
2. the exact left-boundary coordinates when `i<28`; or
3. the exact right-boundary distances when `P-1-j<28`.

If a pair is close to both boundaries, then `P<88`; the finite lengths

`32,36,...,84`

cover every such case. Otherwise translate an interior pair, or its single
near-boundary configuration, by a multiple of four into length 128. Direct
inspection of the ten fixed block strings at the fourteen short lengths and
at length 128 yields exactly the same uncovered set `E` in every case. The
complete deterministic inspection is implemented by
`pair_zero_neutral_padding` and its certificate test; it enumerates the
explicit zero offsets, not SAT assignments or circuit candidates.

For the four exceptions, both blocks would have to begin at zero because all
four coordinates lie before the end of the shortest block. At offset zero an
`A_j` begins `01 10`, while an `O_j` begins `10 01`. These prefixes show
directly that none of the pairs in `E` is simultaneously zero. This completes
the finite case split and the unbounded translation argument. QED.

## Scope

This lemma blocks the particular linear matching of positive two-literal
clauses used in cycle 045. It does not rule out overlapping clauses,
higher-width CNFs, arbitrary membership predicates, or a different exact
minimum-cost extension. It proves no circuit lower bound and does not prove
GATE-004U.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formula contexts, one/two nonoverlapping neutral blocks, raw-coordinate zero coverage, and the disjoint-clause tail model |
| Uniform/non-uniform | Uniform finite block alphabet, placement construction, and finite coverage certificate; later circuit adversary remains fully non-uniform |
| Circuit size | `O(P^2)` explicit contexts; any common disjoint positive two-clause tail has length at most two; no circuit lower bound |
| Circuit depth | Context depth is linear in outer NOT padding in the worst case; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Congruence and translation bookkeeping modulo four only; computation is Boolean |
| Asymptotic quantifiers | Every source string, every four-divisible `P>=32`, and every outer coordinate pair outside the fixed set `E` |
| Regime | Worst-case exact total-language syntax theorem; necessary defense against one counterexample method, not a sufficient loss theorem |
