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
  <- GATE-004G (active parent): joint conditioned-SAT quotient
     + ENC-007 (proved conditioned union)
     + LEMMA-002 with beta=0 (proved recurrence)
  <- GATE-004H (active parent): choose among many identifiers
     + ENC-008 (proved equal-length pair supply)
     + LEMMA-014 (proved logarithmic-step recurrence)
  <- GATE-004I (active parent): aggregate signed identifier surplus
     + LEMMA-015 (proved incidence averaging)
     - GATE-004H-CANDIDATE-COUNT (no-go)
  <- GATE-004J (active smallest brick): loss from forced dependent region
     + ENC-009 (proved complementary columns)
     + ENC-010 (proved all-large-length padding)
     + LEMMA-021 (proved dependent-region size)
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

## Active joint-quotient gate: GATE-004G

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

The primary multi-output literature does not close the gap. RZ21 concerns
identical-copy amortization, which arbitrary fanout trivializes for general
circuits, while ILO20 proves hardness of the minimization problem rather than a
lower bound for this explicit pair. `GATE-004G-LITERATURE — NO-GO` records the
scope boundary.

LEMMA-013 gives the per-parent normal form. Assign each surviving joint
residual class to one original parent-gate label; if `d` labels represent no
class and `t` labels represent two split classes, then

`S(n)-|J_n|=d-t`.

The active surplus is therefore `d>=t+B n^delta+1`. Equal conditioned
residuals can never create the negative split term, but raw sensitivity does
not imply disappearance; `GATE-004G-SENSITIVITY — NO-GO` records that generic
selector obstruction.

## Active parent: GATE-004H

ENC-008 generalizes conditioning to every identifier. All identifiers with
binary length `ell` have prefix length `4ell+10`, so choosing
`ell=Theta(log n)` supplies polynomially many candidate joint quotients with
only logarithmic length loss. GATE-004H asks for one candidate with
`B n^delta+1` net loss.

LEMMA-014 proves that the resulting recurrence gives
`Omega(n^(1+delta)/log n)` size and hence a genuine superlinear unrestricted
SAT lower bound. Candidate multiplicity alone receives no credit: the next
audit must build a signed disappeared/split incidence matrix across identifiers
and prove a positive column surplus.

## Active parent: GATE-004I

LEMMA-015 supplies the exact incidence matrix. Its column sum is the parent
size minus that identifier's joint quotient size, and its total sum is the sum
of the row scores of the parent labels. A polynomial positive average would
force the favorable GATE-004H column.

LEMMA-016 shows why the number of columns is not evidence: a function can
ignore every prefix and retain the same shared core in every pair, giving zero
surplus throughout the matrix. `GATE-004H-CANDIDATE-COUNT — NO-GO` therefore
blocks pure counting. Merely adding essential dependence does not repair it:
LEMMA-017 confines essentiality in every prefix bit to an `O(log n)` parity
shell while exponentially many conditioned pairs retain one core.
`GATE-004I-PREFIX-ESSENTIALITY — NO-GO` records that quantitative failure.

GATE-004I therefore still asks for the missing SAT-specific row theorem:
aggregate disappearance must exceed aggregate splitting by
`|J_n|(B n^delta+1)`. The next attack must use a proved incompatibility among
the distinct conditioned-SAT residual functions, not prefix sensitivity.

ENC-009 supplies the first exact SAT-specific input to that attack. At a
common suffix length, complete-assignment formulas make the `2|J|`
conditioned outputs realize all complementary vectors. This is output-level
shattering only. It receives no circuit-loss credit until an explicit theorem
transfers it to the internal disappeared-minus-split incidence sum.

LEMMA-018 performs the first such transfer as far as support counting permits:
the columns force `R` essential suffix coordinates and hence `R-1` binary
gates. For the explicit witnesses this is only `Omega(n/log n)`, and it is an
absolute parent lower bound rather than a parent-minus-quotient inequality.
`GATE-004I-SHATTERING-SUPPORT — NO-GO` records the ceiling. Any next transfer
must compare internal traces before and after conditioning, not merely count
essential inputs.

The primary restriction/depth-reduction literature does not close this edge.
GKST17 assumes a sufficient measure drop under an allowed substitution;
GATE-004I is exactly such an unproved drop. GKW20 gives a general OR-of-16-CNF
representation, but LEMMA-019 shows that top-component counting alone has a
linear ceiling. `GATE-004-DEPTH-COUNT — NO-GO` prevents promotion of that
structural result to GATE-004 without a richer SAT-specific lower bound.

Pooling every conditioned copy also does not bypass the pairwise obligation.
LEMMA-020 writes the aggregate improvement as `|J|S-Q-X`, where `Q` is the
global quotient and `X` is cross-pair overlap. An unchanged core makes `Q`
tiny relative to duplicated copies but makes `X` cancel the entire apparent
saving. `GATE-004I-GLOBAL-POOLING — NO-GO` therefore requires any successful
trace argument to bound the actual sum of pairwise quotients, not a globally
shared multi-output circuit.

## Smallest active brick: GATE-004J

ENC-010 first ensures that ENC-009's witness matrix fits every sufficiently
large parent length for any fixed `0<c<1`, rather than only one length
congruence. LEMMA-021 then moves the shattering inside the circuit. After every
prefix-independent subcomputation is collapsed to a suffix-boundary signal,
the remaining top region still contains at least `|J|` prefix-dependent binary
gates. For `ell=Theta(log n)` this is polynomially large.

Abundance is not loss. GATE-004J asks whether conditioning across the full
identifier block removes or merges a positive power of that forced region on
average, after all split classes are charged. Its proof would imply GATE-004I;
its failure must identify a circuit architecture in which the entire large
dependent region survives or splits under essentially every pair.

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
