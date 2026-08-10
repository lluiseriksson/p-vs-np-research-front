# LEMMA-118 — a deficient quintet must duplicate at least two NOT gates

**Label: PROVED**

In the residual unicyclic three-NOT circuit forced by LEMMA-117, at least two
of the three NOT gates have two directed paths to the output. Equivalently,
unfolding the circuit into a formula duplicates at least two distinct NOT
gates.

## Proof

An undirected cycle-rank-one output cone has at most two directed paths from
any gate to the output by LEMMA-110. In the fan-out-one unfolding, a gate is
copied once for each such path. If exactly `k` of the three NOT gates have two
paths, the unfolded formula contains exactly `3+k` NOT occurrences.

The formula still computes `W_5`. LEMMA-109 gives `d(W_5)=5`, and Morizumi's
formula inversion theorem requires at least five NOT occurrences. Therefore

`3+k>=5`,

so `k>=2`.

## Boundary

The conclusion does not contradict unicyclic topology: `k=2` gives exactly
five formula NOT occurrences, and `k=3` gives six. Function-specific placement
or cofactor incidence is required to exclude both configurations.

## Model card

| Field | Value |
|---|---|
| Computational model | Unicyclic unrestricted Boolean output cones, directed path multiplicity, and formula unfolding |
| Uniform/non-uniform | Every individual non-uniform residual circuit in the LEMMA-117 stratum |
| Circuit size | Exactly three parent NOT gates; at least two are duplicated, giving at least five formula occurrences |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected binary cycle rank and Boolean-lattice inversion |
| Asymptotic quantifiers | Every unicyclic three-NOT circuit computing the five-block `W_5` |
| Regime | Exact worst-case necessary topology; not an exclusion theorem, SAT lower bound, or terminal result |
