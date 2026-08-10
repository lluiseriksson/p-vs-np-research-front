# GATE-004C — semantic gate loss under exact prefix contexts

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `A,B>0`, `0<=beta<1`, `delta>0`, and `n0`
such that for every `n>=n0` and every minimum-size general Boolean circuit
`C_n` computing `SAT-gamma_n`, there are nonnegative integers `l,d` and

`m = n-12l-4d`,

with `n-A n^beta <= m<n`, for which substituting the fixed context bits from
ENC-003 into `C_n` and exhaustively deleting or constant-folding gates produces
a circuit `D` with

`|D| <= |C_n|-B n^(beta+delta)`.

The source bits occupy the exact suffix specified in ENC-003, and `D` computes
`SAT-gamma_m` on every `m`-bit string.

Any constants introduced by restriction are normalized to the original
constant-free basis before `|D|` is counted; LEMMA-005 bounds this by three
gates, and the stated loss is net of that cost.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted acyclic Boolean circuits for exact SAT-gamma slices; ENC-003 prefix coordinate projections |
| Uniform/non-uniform | Fully non-uniform circuit adversary and per-circuit choice of context |
| Circuit size | Certified loss `B n^(beta+delta)` under length loss at most `A n^beta` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; context choice may depend non-uniformly on the circuit |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed constants; every sufficiently large `n`; every minimum circuit; exists one `(l,d)` |
| Regime | Worst-case exact total-language computation; malformed encodings reject |

## Bridge

ENC-003 proves that the restricted circuit computes the exact length-`m`
SAT-gamma slice. Therefore the theorem gives the recurrence in LEMMA-002 and
implies GATE-004. It is a restricted, more concrete sufficient subgate of
GATE-004B, not a terminal theorem.

## Attempt and surviving obligation

The attempted right-hand analogue failed the exact-language audit: suffix
context bits can repair a malformed source ending in a truncated token. Thus
ENC-003 supplies prefix contexts only. Moreover, LEMMA-003 proves that even if
all contiguous placements were somehow available, arbitrary boundary weight
could concentrate in their common core and defeat coordinate averaging.

Accordingly, a proof of GATE-004C must use a property special to minimum
circuits for the SAT-gamma function or a downstream semantic potential; exact
projection identity and direct input-incidence weights are not enough. The next
audit tested minimality, essentiality, and input-residual diversity against
sharing and reconvergence in unrestricted circuit DAGs. LEMMA-004 proves that
even maximal diversity permits an `O(p)` shell around an arbitrarily complex
shared core. This generic route is `GATE-004C-GENERIC-SEMANTICS — NO-GO`.

The active subgate is GATE-004D: show that the exact SAT restriction forces a
superlinear surplus of constant, equivalent, or dead *internal gate residuals*
in the semantic quotient from LEMMA-005.
