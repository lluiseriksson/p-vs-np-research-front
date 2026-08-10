# LEMMA-068 — two blocks plus the long option cover almost every distant triple

**Label: PROVED**

## Statement

Fix `rho>=24`, slot length `N=4rho`, and `D=floor(N/3)`. For
`0<=i<D`, let

`T_i=(i,i+D,i+2D)`.

Take the all-one option, every one/two-block ENC-022 neutral context, and the
tunable option `A_rho`. On at least `D-6` of the disjoint triples `T_i`, these
options realize all eight three-bit patterns.

Consequently no non-tautological signed clause supported exactly on any of
those `D-6` triples is common to the option family. In particular, the
distant-triple packing from LEMMA-067 does not survive the two-block repair
except possibly on six triples per slot.

## Pattern witnesses

The three coordinates of `T_i` are pairwise separated by at least `D>=32`.

- The all-one option realizes `111`.
- For each chosen coordinate, ENC-020 coordinate density supplies a bounded
  neutral block that makes that coordinate zero. Its length is at most 16,
  so the other two distant coordinates remain one. This realizes the three
  patterns with exactly one zero.
- For each chosen pair, LEMMA-047 supplies one or two nonoverlapping neutral
  blocks making both coordinates zero. Every selected block has length at
  most 28, so the unused distant coordinate remains one. This realizes the
  three patterns with exactly two zeros.
- `A_rho` realizes `000` whenever none of the triple coordinates is among its
  six one bits.

The triples are disjoint, and `A_rho` has exactly six ones. Hence at most six
triples meet a one bit of `A_rho`; all eight patterns occur on every remaining
triple.

The deterministic reference certificate is
`two_block_long_run_complete_distant_triples` and its test. It constructs the
seven bounded/all-one witnesses explicitly and checks the `A_rho` pattern.

## Scope

This proves pattern completeness only for the canonical distant partition.
It does not bound an arbitrary matching of local or intermediate-span common
triples. Such triples remain the active content of GATE-004AB. Test success is
not formal verification.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact one/two-block SAT-gamma neutral contexts, one tunable long option, three-coordinate pattern incidence, and disjoint triples |
| Uniform/non-uniform | Uniform ten-block ENC-022 alphabet, placements, tunable option, and distant partition; no circuit selected |
| Circuit size | No lower bound; at least `floor(4rho/3)-6` distant triples realize all eight patterns |
| Circuit depth | Fixed blocks have bounded depth; tunable option may have linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded AND/OR two and NOT one; later circuits use the same basis |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean pattern incidence only |
| Asymptotic quantifiers | Every `rho>=24`; every triple in the explicit partition except at most six meeting an `A_rho` one bit |
| Regime | Worst-case exact witness-family theorem for one packing geometry; not a general matching bound, circuit lower bound, or terminal result |
