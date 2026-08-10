# GATE-001 — Can a Williams-style SAT transfer be terminalized directly?

**Label: NO-GO**

## Falsifiable proposed theorem

> If general Boolean Circuit-SAT on `n` inputs and `n^k` gates, for every fixed
> `k`, admits a uniform deterministic or co-nondeterministic
> `2^n / n^omega(1)`-time algorithm, then `SAT notin P/poly`.

### Model card

| Field | Value |
|---|---|
| Computational model | Multitape meta-algorithm for general Boolean Circuit-SAT; general Boolean circuit lower-bound conclusion |
| Uniform/non-uniform | Uniform algorithm premise; non-uniform conclusion |
| Circuit size | Premise `n^k` for every fixed `k`; conclusion excludes all polynomial sizes |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None; co-nondeterminism optionally allowed in the premise |
| Advice | None in premise; polynomial advice represented by conclusion circuits |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One superpolynomial saving; all fixed input-circuit exponents; one SAT language against all conclusion exponents |
| Regime | Worst-case exact Circuit-SAT; worst-case exact SAT lower bound |

## Attempt

The Williams 2010 proof assumes small circuits for a high uniform class, uses
succinct computation encodings and an easy-witness argument, and contradicts a
nondeterministic time hierarchy. Replacing the high class by NP would need to
turn the resulting fixed-exponent lower bounds into one language outside every
polynomial circuit size.

Murray-Williams 2018 moves the hard language down to NP only in the form

`forall k, NTIME[n^(c k^4/epsilon)] notsubseteq SIZE(n^k)`.

The attempted terminal step swaps `forall k, exists L_k` to
`exists L, forall k`. No theorem justifies this swap. A tagged disjoint union
does not remain in NP with one fixed verifier exponent unless it is padded; the
padding then consumes the circuit exponent.

There is also a logical stress test. If `P=NP`, general Circuit-SAT has a
polynomial-time algorithm as a function of its explicit input length, so for
appropriate size parameters the premise can be easier than the desired
conclusion. Thus the missing terminal implication cannot be treated as generic
bookkeeping: proving it in the needed generality would itself have to contain a
nonrelativizing separation mechanism.

## Exact no-go

The known transfer is not terminal because its conclusion has the wrong
language class/quantifier pattern. The bridge may be used only with its actual
NEXP, `E^NP`, NQP, restricted-class, or fixed-exponent NP conclusion.

This does not prove that every possible SAT-algorithm route fails. It rules out
the unproved direct promotion of the existing transfer to `SAT notin P/poly`.

## Next gate

GATE-002 quantifies the padding loss needed to combine a family of hard
languages into one NP language.
