# SAT and Circuit-SAT bridge audit

**Overall label: PROVED** for the literature audit and implication checks.
No bridge listed here currently reaches the terminal statement.

## BR-COOK — SAT completeness

Cook-Levin supplies uniform deterministic polynomial-time many-one reductions
from every language in `NP` to `SAT`. Therefore a uniform polynomial-time SAT
decider proves `P=NP`; and a general non-uniform polynomial-size SAT circuit
family would place all of `NP` in `P/poly` after composing the reductions.

Terminal relevance: exact and complete, but it supplies no lower bound.

## BR-W10 — general Circuit-SAT algorithm to NEXP lower bounds

Williams (2010), Theorem 1.1: for every polynomial circuit-size exponent, a
co-nondeterministic Circuit-SAT algorithm with a superpolynomial factor
improvement over exhaustive search yields `NEXP notsubseteq P/poly`.

### Model card BR-W10

| Field | Value |
|---|---|
| Computational model | Co-nondeterministic algorithm for general Boolean Circuit-SAT; non-uniform Boolean lower-bound target |
| Uniform/non-uniform | Uniform meta-algorithm; non-uniform target |
| Circuit size | Input circuits `n^k` gates for every fixed `k`; target polynomial size |
| Circuit depth | Unrestricted |
| Fan-in | Standard fan-in-two Boolean basis |
| Randomness | None; co-nondeterminism allowed by theorem |
| Advice | No algorithm advice stated; target permits polynomial non-uniformity |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One superpolynomial saving `s(n)`; algorithm for all fixed input-size exponents `k` |
| Regime | Worst-case exact Circuit-SAT/UNSAT decision |

Terminal gap: `NEXP notsubseteq P/poly` does not imply `P != NP`. No reverse
containment or collapse theorem closes this gap unconditionally.

## BR-W11 — class-specific SAT algorithms to class-specific lower bounds

Williams (2011) converts a slightly faster `C`-Circuit-SAT algorithm, under
closure and containment conditions on `C`, into non-uniform lower bounds for
larger uniform classes against `C`. Instantiating the method for `ACC0` yields
`NEXP notsubseteq ACC0`.

Terminal gap: `ACC0` has constant depth and special gates; it is a strict
syntactic subclass of general polynomial-size circuits. The hard language is in
NEXP, not established to be SAT or even a single NP language outside `P/poly`.

## BR-MW18 — fixed-exponent NP lower bounds

Murray and Williams (2018), Theorem 1.1: for a typical class `C` and fixed
`epsilon in (0,1)`, if `GAP C UNSAT` on `n`-input circuits of size
`2^(epsilon n)` has a nondeterministic `O(2^((1-epsilon)n))` algorithm, then
there is a constant `c` such that, for every `k`,

`NTIME[n^(c k^4/epsilon)] notsubseteq C-SIZE[n^k]`.

### Model card BR-MW18

| Field | Value |
|---|---|
| Computational model | Nondeterministic gap-unsatisfiability algorithm; nondeterministic multitape time target; `C` circuits |
| Uniform/non-uniform | Uniform algorithm and language class; non-uniform lower-bound target |
| Circuit size | Meta-algorithm input `2^(epsilon n)`; conclusion `n^k` |
| Circuit depth | Whatever the typical class `C` permits; must be instantiated |
| Fan-in | Whatever `C` permits; must be instantiated |
| Randomness | None required; nondeterminism allowed |
| Advice | The paper permits limited advice variants; this canonical card uses none in the premise |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Fixed `epsilon`; exists universal `c`; for every fixed `k` a class noncontainment at time exponent `c k^4/epsilon` |
| Regime | Promise/gap: unsatisfiable versus at least one quarter of assignments satisfying; worst-case over promised inputs |

Terminal gap: the conclusion is `forall k, exists L_k`, with verifier exponent
growing as `Theta(k^4)`. It is not `exists L, forall k`. Under the canonical
padding calculation the usable ratio is

`b(k)/a(k) = k/(c k^4/epsilon) = epsilon/(c k^3) -> 0`,

where terminalization via GATE-002 would require an unbounded ratio.

The underlying easy-witness Lemma 4.1 already requires the nondeterministic
time parameter to dominate a triple composition of the assumed circuit-size
function. For `s(n)=n^k`, this creates an `Omega(k^3)` exponent before the final
Theorem 1.1 parameter loss. Reindexing cannot change a bounded ratio, and
polynomial padding divides both exponents by the same factor (LEMMA-001).

## BR-KL — Karp-Lipton collapse

If `NP subseteq P/poly`, the polynomial hierarchy collapses to its second level.

Terminal gap: no unconditional non-collapse of the polynomial hierarchy is
known. Assuming that non-collapse in order to refute `NP subseteq P/poly` would
replace P versus NP with a stronger unproved separation.

## BR-SW13 — medium-uniform fixed-exponent lower bounds

For every fixed `k`, Santhanam and Williams exhibit a language `L_k in P` not
having P-uniform `O(n^k)` circuits. The language may depend on `k`, and the
lower bound is against circuits with a generation requirement.

Terminal gap: arbitrary `P/poly` circuits need not be P-uniform. The theorem is
compatible with `P=NP` and does not imply a SAT lower bound.

## Audit conclusion

The strongest audited transfers reach restricted circuit classes, high uniform
time classes, or fixed exponent lower bounds in NP. None supplies the
quantifier-stable, unrestricted, non-uniform lower bound needed for
`SAT notin P/poly`. GATE-001 records the failed attempt to treat the Williams
bridge as terminal; GATE-002 isolates the exponent-ratio requirement; GATE-003
is now rejected because satisfying that requirement is equivalent to the
terminal-sufficient non-uniform separation rather than a smaller milestone.
