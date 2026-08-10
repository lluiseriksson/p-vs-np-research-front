# LEMMA-003 — contiguous-context coverage limit

**Label: PROVED**

## Statement

Let `n>p>=0`, let `m=n-p`, and let `P` be any family of coordinate
projections from `m` source bits to `n` target coordinates such that every
projection leaves the source bits as one contiguous interval. If `2p<n`, then
there is a target coordinate left variable by every projection in `P`.

More strongly, if `w_1,...,w_n` are arbitrary nonnegative coordinate weights,
no positive lower bound on the weight fixed by some projection can be deduced
from `sum_i w_i` alone: all weight may be supported on a coordinate left
variable by every projection.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract coordinate projections; intended application to exact SAT-gamma contexts and Boolean circuit input boundaries |
| Uniform/non-uniform | Projection family arbitrary; no uniformity assumption |
| Circuit size | No circuit-size theorem; coordinate-weight method limitation only |
| Circuit depth | Unrestricted in intended circuit application |
| Fan-in | AND/OR two and NOT one in intended circuit application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Nonnegative real weights only; no algebraic computation model |
| Asymptotic quantifiers | Every `n,p` with `2p<n`; every family of length-`m` contiguous intervals; every nonnegative weight vector |
| Regime | Deterministic finite combinatorics; method-specific worst-case obstruction |

## Proof

Index the target coordinates by `0,...,n-1`. A projection's variable interval
has length `m` and therefore begins at some integer `s` with `0<=s<=p`; it is

`I_s={s,s+1,...,s+m-1}`.

For every allowed `s`, the interval

`K={p,p+1,...,m-1}`

is contained in `I_s`: its left endpoint satisfies `p>=s`, and its right
endpoint satisfies `m-1<=s+m-1`. Because `2p<n`, `|K|=m-p=n-2p>0`.
Thus any coordinate `j in K` is variable under every projection in `P`.

Set `w_j=1` and all other weights to zero. Every projection fixes weight zero
although total weight is one. Scaling `w_j` gives the same counterexample for
any prescribed total weight. Therefore total boundary weight alone cannot
imply that one of these projections fixes a positive amount of it. QED.

## Consequence and scope

ENC-003 supplies only the special placement whose source is a suffix. The
lemma is stronger as a method audit: even if an exact construction supplied
*every* contiguous placement with `p=o(n)`, a central core of `n-2p`
coordinates would survive them all. Hence contiguous-placement averaging
cannot prove the GATE-004B gate-loss inequality from arbitrary per-coordinate
boundary weights alone.

This does not show that SAT circuits concentrate their relevant structure in
the common core. It does not refute semantic arguments about minimum SAT
circuits, non-contiguous projections, or GATE-004B itself.
