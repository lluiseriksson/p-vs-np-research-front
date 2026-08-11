# GATE-004CG — separate three neutralization regions

**Label: EXPLORATORY**

Assume the GATE-004CF minimum shared-exit parent and no private certificate.
For a satisfying restriction, call one of its two binary gate eliminations a
**neutralization event**. An event covers a pair-signature obligation if every
directed route carrying that obligation into the surviving minimum `A` cone
passes through the eliminated gate or its contracted incidence.

Consider these three obligations:

1. the raw-`t` change adjacent to the falsifying code `10`;
2. the negative-`u` polarity through the earliest mixed surviving NOT;
3. the second `01/11` cancellation arm supplied by the shared exit.

## Falsifiable theorem

For at least one satisfying code, the three obligations admit regions
`R_t,R_n,R_s` such that no rank-neutral binary neutralization event covers two
regions. If two regions share such an event, the shared predecessor topology
instead yields either an admissible LEMMA-183 private realization certificate
or forces deletion of a non-bridge edge of `gamma`.

Three separated regions require at least three binary eliminations,
contradicting LEMMA-178. The two exceptional outcomes contradict extremality
or LEMMA-185. Hence proving this theorem establishes GATE-004CF.

The regions must be defined from actual directed paths and gate functions in
the parent, and coverage must be proved for every valid pruning to a minimum
`A` circuit. Merely counting cancellation fronts is invalid by
GATE-004CF-FRONT-COUNT-ONLY.

LEMMA-187 supplies pruning-independent carrier regions, but carrier membership
does not imply elimination. GATE-004CG-CARRIER-COVERAGE-ONLY shows that many
pair-sensitive carrier gates may survive after one upstream contraction.
GATE-004CH therefore moves the missing assertion to cross-code incompatibility
among all three minimum pruning maps.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted plateau DAG with earliest mixed NOT, shared-exit cycle, and exact pruning events |
| Uniform/non-uniform | Every individual non-uniform operational GATE-004CF parent; uniform fresh implication pair |
| Circuit size | Three event-disjoint obligations versus exactly two binary eliminations, or private/non-bridge contradiction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor obligations and undirected cycle minors over `F_2` |
| Asymptotic quantifiers | Every operational shared-exit plateau parent and every minimum satisfying pruning |
| Regime | Exact worst-case neutralization-separator gate; not a SAT lower bound or terminal result |
