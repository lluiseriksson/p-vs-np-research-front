# LEMMA-192 — a plateau switching carrier has at least three gates

**Label: PROVED**

Assume the hypothetical minimum two-gate implication plateau and the active
switching branch. Let `n=NOT h` be the earliest `u`-sensitive NOT and let
`H=H_{01,11}` be the canonical difference carrier. Then

`|H|>=3`.

Consequently, in the conditional `W=1` case of LEMMA-190,

`3<=|H|<=7`.

## Proof

Switching gives `n_01!=n_11`. Negation is injective, so
`h_01!=h_11`; hence the two distinct gates `h,n` lie in `H`.

By LEMMA-187, `h` has a directed carrier path from a raw input on which codes
`01` and `11` differ. Those codes fix the same base inputs and both have
`t=1`; their only differing raw input is `u`.

If `H` contained only `h,n`, the carrier path from raw `u` to `h` could have
no intervening noninput gate. Thus an input wire of `h` would come directly
from raw `u`. LEMMA-179 proves that in a minimum two-gate plateau neither
input wire of this mixed binary `h` can come directly from raw `u` or raw
`t`, because a satisfying restriction would make `h` and then the surviving
NOT `n` constant. This contradiction proves `|H|>=3`.

The upper bound seven is exactly LEMMA-190 and remains conditional on `W=1`.
The lemma does not classify carriers of sizes three through seven.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT two-gate implication plateau in the satisfying-signature switching branch |
| Uniform/non-uniform | Every individual finite non-uniform hypothetical plateau parent; uniform fresh implication pair |
| Circuit size | Canonical `01/11` carrier has at least three gates; at `W=1` it has three through seven |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor inequality and directed carrier reachability only |
| Asymptotic quantifiers | Every nonconstant finite base and every hypothetical minimum plateau parent in the switching branch |
| Regime | Exact worst-case minimum-carrier exclusion; not a plateau exclusion, SAT lower bound, or terminal result |
