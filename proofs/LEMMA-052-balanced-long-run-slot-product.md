# LEMMA-052 — balanced long-run slots cross all established clause thresholds

**Label: PROVED**

## Statement

Fix integers `rho>=7` and `s>=1`, and let one slot have length `4rho`. Its
option set consists of:

1. every ENC-020 coordinate-dense neutral context of length `4rho`; and
2. the ENC-026 long-run block `A_rho` of the same length.

Let `B_{rho,s}` be the product family formed by independently choosing one
option in each of `s` consecutive slots and then appending the source string.
Its outer length is `P=4rho s`. Then:

1. every member preserves exact validity and satisfiability;
2. every outer raw coordinate takes both bit values across the family;
3. every member's zero support is covered by at most `s` slot intervals of
   length `4rho`;
4. every member has maximum zero run at most `rho`;
5. for every uniform `b,D` interval cover to which LEMMA-049 applies, its
   distant-group count is at most `6s`; and
6. `floor(P/(rho+1))<4s` for LEMMA-050.

## Proof

Every slot option is an exact identity context. Concatenating identity
contexts composes them, proving item 1. ENC-020 is a subset of the slot
options and varies every slot coordinate; hold every other slot at the
all-one option to prove item 2.

Each option differs from all ones inside one block of length at most `4rho`,
so the `s` slot intervals cover every zero, proving item 3. The long block has
maximum zero run `rho`. Short ENC-020 blocks have maximum run at most four.
At a slot boundary, the long block's terminal run has length `rho-3` and the
next block's initial run has length at most one, so the combined run is at
most `rho-2`. All-one gaps only shorten it. This proves item 4.

The all-long member uses `A_rho` in every slot. Each block has exactly six one
bits, so this member has `P-6s` zero positions. Any cover by `b` intervals of
length at most `D` must satisfy

`bD>=P-6s`.

If LEMMA-049's group count `m_b=floor(P/(b+1))` also satisfies `m_b>=D`, then

`P-6s<=bD<=b m_b<=P-m_b`,

and hence `m_b<=6s`. This proves item 5 for every possible cover, not only the
slot cover. Finally,

`P/(rho+1)=4rho s/(rho+1)<4s`.

Taking floors proves item 6. QED.

## Explicit base-size floor

In the compact assignment-witness setting, every eligible total base that
matches the `R` complementary assignment directions depends essentially on at
least `R` distinct raw suffix coordinates. For direction `j`, its two endpoint
codes differ only inside the `j`th gadget support and have different output
under the corresponding row. Along any Hamming path between them, some raw
coordinate in that support is essential. The supports are disjoint over `j`.

A fan-in-two single-output circuit depending on `R` raw inputs has at least
`R-1` binary gates: in the underlying output-cone graph, each binary gate can
merge at most two previously disconnected input components. NOT gates merge
none. Thus `K>=R-1`.

Choosing

`s=floor((R-1)/8)`

gives `6s<=3(R-1)/4<=K` and
`floor(P/(rho+1))<4s<= (R-1)/2<=K` for large `R`. Therefore the exact negative
tails proved in LEMMA-045, LEMMA-049, and LEMMA-050 do not apply to this
product family. This is only an escape from those hypotheses; it proves no
positive loss.

## Scope

Other common predicates, overlapping clauses, or exact minimum-circuit
extensions may still defeat the family. The base-size floor is linear, not a
SAT lower bound beyond the explicit assignment-direction requirement. No
result is promoted to GATE-004U.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma neutral contexts, independent slot products, raw-coordinate density/run geometry, essential-input lower bounds, and unrestricted Boolean circuits |
| Uniform/non-uniform | Uniform slot family and parameter choice from `R`; fully non-uniform eligible base circuits |
| Circuit size | Eligible assignment-direction base has `K>=R-1`; every applicable sparse-cover tail has at most `6s` clauses and the run tail fewer than `4s`, so established negative conditions fail for `s=floor((R-1)/8)` |
| Circuit depth | Contexts may have linear NOT depth; base and later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Disjoint affine assignment directions over `F_2` only in the essential-input floor; computation is Boolean |
| Asymptotic quantifiers | Every `rho>=7,s>=1`; explicit asymptotic application for all sufficiently large `R` with `s=floor((R-1)/8)` |
| Regime | Worst-case exact total-language witness construction and method-boundary theorem; not a circuit lower bound for SAT |
