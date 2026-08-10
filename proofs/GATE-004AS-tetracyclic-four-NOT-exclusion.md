# GATE-004AS — exclude tetracyclic four-NOT circuits for `W_9`

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing `W_9` has cycle rank four
and exactly four NOT gates. One explicit circuit with these parameters
falsifies the theorem.

LEMMA-138 proves that every deficient nine-index dependency-cone Hall set
would restrict to exactly this stratum. Proving this gate would extend local
Hall through size nine, but would not establish full Hall, a SAT circuit lower
bound, or P versus NP.

Generic path multiplicity is insufficient by
GATE-004AS-PATH-MULTIPLICITY-ONLY. The next attack is a rank-four
block-cut/2-connected source reduction extending LEMMA-135.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for fixed `W_9` with exact cycle rank four and four NOT gates |
| Uniform/non-uniform | Every individual non-uniform nine-block circuit in the exact stratum |
| Circuit size | Target exclusion of `c=4,q=4`; 48 binary and 52 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean source and articulation cofactors |
| Asymptotic quantifiers | Fixed `W_9` and every pruned circuit with `c=4,q=4` |
| Regime | Exact finite structural gate for nonet Hall; not a full family lower bound or terminal result |
