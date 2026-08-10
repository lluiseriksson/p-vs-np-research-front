# Vertical proof map

Date: 2026-08-10

No arrow is accepted unless it has its own proved implication and model card.
Every `SAT` occurrence means the exact total `SAT-gamma` language in
`docs/sat-encoding.md`.

```text
P != NP
  <- T-UNIFORM: SAT notin P
  <- T-NONUNIFORM: SAT notin P/poly
     == V-1: NP notsubseteq P/poly
  <- all same-language rungs: for every k, SAT notin SIZE(n^k)
  <- GATE-005 (downstream, open): same-language exponent amplification
  <- GATE-004 (active): first superlinear unrestricted SAT circuit lower bound
  <- GATE-004B (active): SAT-specific amortized block restriction
  <- GATE-004C (active): semantic loss under exact prefix contexts
  <- GATE-004D (active): SAT internal residual-function collisions
  <- GATE-004E (active): collisions in one neutral-prefix family
  <- GATE-004F (open alternative): same-column residual-function collisions
     + LEMMA-002 (proved recurrence)

Alternative active route:
  GATE-004
  <- GATE-004G (active smallest brick): joint conditioned-SAT quotient
     + ENC-007 (proved conditioned union)
     + LEMMA-002 with beta=0 (proved recurrence)
```

`T-UNIFORM <- T-NONUNIFORM` is valid because every uniform polynomial-time
decider unrolls to polynomial-size Boolean circuits. `T-NONUNIFORM` and `V-1`
are equivalent through Cook-Levin reductions, provided the reduction's circuit
size blow-up is recorded.

## V-1 model card

Statement: there exists one language `L in NP` such that for every constant
`d`, every Boolean circuit family of size `O(n^d)` fails to decide `L` on at
least one input length (indeed infinitely many lengths).

| Field | Value |
|---|---|
| Computational model | NP verifier on multitape Turing machine; Boolean circuits over `{AND,OR,NOT}` |
| Uniform/non-uniform | Uniform verifier versus non-uniform circuit adversary |
| Circuit size | All polynomial sizes `O(n^d)`, every fixed `d` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice is absorbed into the circuit family |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | `exists L in NP, forall d, forall circuit families, infinitely many failure lengths` |
| Regime | Worst-case exact total-language decision |

## Rejected decomposition: GATE-003

GATE-003 asked for a uniformly indexed sequence `(L_j)` satisfying GATE-002
with unbounded exponent ratio. It is now `NO-GO` as an intermediate brick:
GATE-002 proves that it implies `NP notsubseteq P/poly`, while repeating one
language in `NP \ P/poly` with `b(j)=j` proves the converse. The proposed brick
is therefore equivalent to V-1 and not smaller than the terminal-sufficient
theorem.

LEMMA-001 also proves that reindexing and polynomial padding preserve or reduce
the exponent ratio, so those operations cannot repair the Murray-Williams
profile.

## Active lower-bound target: GATE-004

Prove that for one explicit constant `delta>0`, the fixed SAT language requires
more than `n^{1+delta}` gates in unrestricted non-uniform fan-in-two Boolean
circuits for infinitely many lengths. This would be a genuine same-language
general-circuit lower bound, but it would not itself exclude larger polynomial
circuit families.

## GATE-004 model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits computing exact `SAT-gamma` language slices |
| Uniform/non-uniform | Fully non-uniform circuit adversary |
| Circuit size | Exclude `O(n^{1+delta})` for one fixed explicit `delta>0` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice is represented by the arbitrary circuit family |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `delta>0`; infinitely many lengths; every circuit within the size bound fails on some input |
| Regime | Worst-case exact total-language decision; malformed encodings reject |

## Active block-restriction gate: GATE-004B

For every minimum circuit computing `SAT-gamma_n`, find a coordinate projection
to `SAT-gamma_m`, losing at most `A n^beta` input length but forcing at least
`B n^(beta+delta)` gates to disappear. LEMMA-002 proves that iterating this
recurrence yields the GATE-004 lower bound. ENC-002 supplies exact
double-negation projections; generic fanout counting does not supply the needed
gate loss.

## Active semantic-loss gate: GATE-004C

ENC-003 enlarges the proved prefix projection family: fixed tautologies can be
conjoined before the embedded formula while preserving exact validity and
satisfiability. The symmetric right context fails because suffix bits can
repair malformed trailing syntax. GATE-004C asks for the GATE-004B loss under
the exact prefix family only.

LEMMA-003 proves a scoped limitation: even if every sublinear contiguous
placement were available, the placements would leave a large common variable
core, so arbitrary coordinate-weight averaging cannot force any positive fixed
weight. This is recorded as
`GATE-004B-CONTEXT-AVERAGING — NO-GO`. GATE-004C remains open because a proof
could use semantic structure unique to minimum SAT circuits or propagation
beyond the input boundary.

## Active residual-collision gate: GATE-004D

LEMMA-005 defines the exact semantic quotient of a restricted circuit: merge
internal gates with identical residual functions, replace constant/input
residuals, and delete dead gates. GATE-004D asks for a nearby exact SAT prefix
restriction whose quotient loses `B n^(beta+delta)` gates.

LEMMA-004 shows why this must concern *internal SAT gate functions*. Even a
minimum circuit can have all `p` restricted inputs essential and the maximum
`2^p` distinct output residuals while every residual remains within `O(p)`
gates of the original function. A large core can be shared by all branches.
This defeats the generic semantic route but leaves the SAT-specific collision
theorem falsifiable and open.

## Active neutral-family gate: GATE-004E

ENC-004 and LEMMA-006 give an explicit family: for padding `12k`, there are
`k+1` separated prefix assignments, every one leaving the exact same
`SAT-gamma_{n-12k}` residual. GATE-004E asks for the collision surplus within
one such family, so the cross-restriction table of internal gate functions is
the concrete object under audit.

LEMMA-007 proves that neutral parser-state multiplicity does not lift
generically. Any separated neutral set can sit in front of an arbitrary shared
core with every prefix bit essential and only an `O(pr)` decoder shell. This is
`GATE-004D-PARSER-LIFT — NO-GO`; the open gate must use an internal property
specific to SAT circuits, not only the output parser states.

## Open same-column route: GATE-004F

LEMMA-008 sharpens the generic obstruction: the exact ENC-004 family is the
block language `X*W*`, so a linear-size decoder reproduces its complete output
geometry around an arbitrary core while every prefix bit remains essential.
Consequently cross-column output statistics cannot force restriction loss.

GATE-004F asks for a directly auditable internal event: in some single neutral
restriction column, at least `B n^(beta+delta)+3` gates become constant,
input-equivalent, or semantically equal to an earlier gate. LEMMA-005 converts
that count into the net gate loss required upstream.

ENC-005 supplies a constant-zero cofactor only two prefix bits from the neutral
SAT cofactor. LEMMA-009 proves that this proximity still has no generic force:
`s AND G` retains the entire `G` core when `s=1` although the other cofactor is
zero. This is `GATE-004F-ANNIHILATOR — NO-GO`; the next audit uses the complete
two-bit cofactor table rather than the hard/zero pair alone.

ENC-006 completes that audit: the four residuals are exactly one SAT column and
three zero columns. LEMMA-010 shows that this entire table is realized by a
three-gate one-hot selector around an arbitrary core. Therefore
`GATE-004F-FOUR-COFACTOR — NO-GO`; the next attack must use nonlocal prefix
residual structure rather than any constant-width operator window.

## Smallest active brick: GATE-004G

ENC-007 supplies two equal-length fourteen-bit restrictions computing SAT
conditioned on variable identifier 1 being zero or one. Their pointwise OR is
exactly the shorter SAT slice. GATE-004G asks whether the two restricted copies
of every minimum parent circuit can be semantically quotiented *jointly* to a
shared two-output circuit smaller than the parent by `B n^delta+1` gates.

Adding one OR gate would then give

`S(n)>=S(n-14)+B n^delta`,

and LEMMA-002 yields the GATE-004 superlinear bound. LEMMA-011 prevents a
generic direct-sum promotion: distinct, disjoint conditioned branches whose OR
is hard can share an arbitrary core with constant overhead. The open content
is therefore a SAT-specific constraint on internal sharing, not the output
union identity alone.

LEMMA-012 records the factor-two accounting exactly. If `ell_0,ell_1` are
individual conditioned-branch losses and `x` is additional cross-copy sharing,
then a joint improvement `L` requires

`ell_0+ell_1+x >= S(n)+L`.

The full `S(n)` term only cancels duplication of the parent circuit. Therefore
separate branch simplifications cannot be added and promoted to GATE-004G
without a proved sharing surplus; that route is
`GATE-004G-SEPARATE-LOSSES — NO-GO`.

## Downstream amplification obligation: GATE-005

To turn GATE-004 into a terminal chain, a separate same-language amplification
theorem must advance a proved SAT lower-bound exponent by a fixed positive
amount without changing the circuit model. Iterating that theorem would have to
cover every polynomial exponent. No such theorem is claimed.

## Excluded pseudo-routes

- `NEXP notsubseteq C` for a restricted class `C` has no recorded implication
  to `P != NP`.
- `for every k, there exists L_k in NP` needing more than `n^k` circuits does
  not swap to `there exists L in NP, for every k`.
- GATE-003's unbounded-ratio family is equivalent to the desired non-uniform
  separation and receives no credit as a decomposition.
- A uniform circuit-generation lower bound does not automatically give a
  non-uniform circuit lower bound.
- Average-case, promise, randomized, oracle, algebraic, proof-system, and
  communication results require separate terminal bridges.
