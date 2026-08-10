# LEMMA-087 — the symbolic identifier oracle equals literal enumeration

**Label: PROVED**

Fix a maximum identifier bit length, a representative outer length, at most
five selected coordinates, and a block-count bound. The mask set returned by
`CompleteIdentifierAuditor` is exactly the set returned by enumerating every
standard neutral block at every allowed aligned placement and applying the
ordinary nonoverlapping-interval DP.

For each identifier length the symbolic template records every fixed syntax
bit and labels each free identifier column. On selected coordinates at one
placement, it enumerates every assignment to the at most five distinct free
columns; repeated occurrences of one column in the duplicated variable copies
receive the same bit. Therefore its mask options are exactly the union over all
literal identifiers of that length.

For each mask and start, retaining the smallest block end is safe because an
earlier-ending interval weakly enlarges every set of legal continuations. The
suffix table then gives the earliest ending placement of each mask whose start
is after the previous block. Induction on the number of blocks proves that the
frontier stores the earliest end for every reachable accumulated mask, exactly
matching explicit interval DP reachability.

Regression tests compare the implementations on fixed smaller complete
alphabets and on the full length-76 obstruction. The oracle is a verifier
optimization, not a circuit result.

## Model card

| Field | Value |
|---|---|
| Computational model | Symbolic SAT-gamma block templates and nonoverlapping interval DP |
| Uniform/non-uniform | Uniform exact verifier for finite complete identifier alphabets; no circuit selected |
| Circuit size | No lower bound; verifier preserves finite mask reachability |
| Circuit depth | Not applicable; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every finite maximum identifier length, representative length, selected tuple of size at most five, and positive block bound |
| Regime | Exact verification equivalence; not a circuit, promise, average-case, or terminal result |
