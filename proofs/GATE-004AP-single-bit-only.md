# GATE-004AP-SINGLE-BIT-ONLY — treat both theta splits as one source bit

**Label: NO-GO**

The remaining split budget cannot be collapsed to the ternary-source proof.
With two core vertices of outdegree two, either two independent source trees
inject two separately computed bits into the theta branches, or a later split
computes a value depending on the first source bit and additional attached
inputs. In neither pattern has every upstream variable been proved to reach
the output through one common Boolean node.

Therefore invoking LEMMA-121 with a single intermediary bit would assume the
factorization that must be proved. The correct interface has up to two source
bits in the parallel case and a sequential state in the nested case.

This is a method no-go only. GATE-004AP was subsequently proved by separating
parallel and nested orientations; the common-one-bit shortcut remains invalid.

## Model card

| Field | Value |
|---|---|
| Computational model | Two-binary-split theta orientations and attempted one-bit functional factorization |
| Uniform/non-uniform | Every individual non-uniform remaining theta candidate |
| Circuit size | No lower bound; a common one-bit interface is unproved and generally absent topologically |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed split topology and Boolean interfaces only |
| Asymptotic quantifiers | Every candidate in GATE-004AP |
| Regime | Structural no-go for single-bit reuse; two-bit/sequential interface remains open |
