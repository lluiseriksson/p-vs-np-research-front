# GATE-004BV-UNSPECIFIED-EXCHANGE-ONLY — invoke an unnamed normal-form exchange

**Label: NO-GO**

## Attempt

Assert that the common minimum parent can be exchanged for another minimum
representation exposing a uniformly neutral NOT or cycle path, while
preserving size and `N+r`.

## Failure

LEMMA-153 shows that `N+r` preservation follows automatically from size
preservation for a fixed function. The remaining assertion — that some
minimum representation has the desired exposure — is precisely the new
structural theorem that must be proved. Calling it an “exchange” supplies no
rewrite relation, no well-founded potential, and no reason that the exposed
representation exists.

Thus an unspecified exchange cannot be used as a proof step. This does not
refute GATE-004BV or the possibility of a normal form. It requires the normal
form to be selected by an independently defined extremal invariant and then
proved to have the exposure.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted AND/OR/NOT circuits and abstract equivalent-representation exchange |
| Uniform/non-uniform | Every individual non-uniform minimum circuit; no uniform transformation supplied |
| Circuit size | Size preservation fixes `N+r` by LEMMA-153; no gate-saving rewrite proved |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean functional equivalence |
| Asymptotic quantifiers | Every fixed finite Boolean function and all its pruned minimum representations |
| Regime | Circularity no-go for an unspecified exchange step; not a refutation of GATE-004BV, a SAT lower bound, or a terminal result |
