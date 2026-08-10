# LEMMA-042 — exact expanded output incidence does not force loss

**Label: PROVED**

## Statement

The LEMMA-041 total-function family has exactly the ENC-017 equality classes,
multiplicities, and positive/negative noncollision across all expanded-cube
output residuals. Nevertheless, after appending `m` fresh conjuncts, every
diagonal joint quotient has signed loss at most `K_d-m`.

Therefore the exact cubic number of distinct expanded output functions and
their complete incidence table, even together with ambient global minimality
and every GATE-004P diagonal hypothesis, do not generically force positive
quotient loss.

## Proof

LEMMA-041 defines every expanded-row residual before the fresh tail as

`w AND g^+_{a,b,c}(y,a)`

or

`w AND g^-_{a,b,c}(y)`.

All ENC-017 conditions are nonconstant. For any two such conditions `g,h`,

`w AND g = w AND h`

as Boolean functions if and only if `g=h`: the forward direction follows by
setting `w=1`. Hence multiplication by `w` preserves every equality class,
multiplicity, and cross-polarity distinction counted in ENC-017.

The fresh conjunction tail multiplies every expanded output by one further
common function `Z=z_1 AND ... AND z_m`; setting `w=Z=1` again shows that it
preserves the same output equality table. LEMMA-041 already proves that the
displayed ambient circuit is globally minimum with size `K_d+m` and that each
diagonal quotient retains at least `2m` active tail classes. Its loss is at
most `K_d-m`, completing the no-go. QED.

## Boundary

This counterexample realizes only single-assignment evaluation columns on the
diagonal. It does not realize ENC-018's `3^R` compact multi-witness patterns,
where both conditioned polarities can be satisfiable for the same suffix.
GATE-004T isolates that remaining output-level property.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits, full expanded-cube output residuals, exact equality incidence, and diagonal semantic joint quotients |
| Uniform/non-uniform | Explicit uniformly described family; `K_d` is the non-uniform minimum size of its finite base |
| Circuit size | Exact parent size `K_d+m`; diagonal quotient at least `2m`; loss at most `K_d-m` despite the exact cubic output-incidence table |
| Circuit depth | Base unrestricted; fresh AND tail displayed as a chain; minimum-size statement depth unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Expanded affine geometry over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every `d>=1` and `m>=1`; negative loss for every `m>K_d` |
| Regime | Worst-case exact total-function computation; method obstruction, not SAT-gamma and not multi-witness closed |

