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

Collision-aware active branch:
  GATE-004I
  <- GATE-004M (open collision-aware route): stable-core collision surplus
     + LEMMA-029 (proved exact full quotient accounting)

Adjacent collision-aware active branch:
  GATE-004I
  <- GATE-004N (open adjacent route): one-bit conditioned-SAT surplus
     + ENC-013 (proved exact adjacent conditioning)
     + LEMMA-029 (proved exact full quotient accounting)
  <- GATE-004O (open parent): affine-context trace elimination
     + ENC-014 (proved parallel affine edge cube)
     + LEMMA-034 (proved context-dependent region)
  <- GATE-004P (no-go): compressed full-context shattering
     - LEMMA-038 (fresh-tail counterexample)
  <- GATE-004Q (active parent): SAT off-cube rigidity
     + ENC-015 (proved six-case one-bit halo semantics)
     + ENC-016 (proved full expanded context formula cube)
     + ENC-017 (proved exact expanded output incidence)
     + ENC-018 (proved multi-witness union columns)
     + ENC-019 (proved common-padding fixed-face geometry)
     + ENC-020 (proved coordinate-dense neutral padding)
     + ENC-021 (proved distant common clauses on ENC-020)
     + ENC-022 (proved almost pairwise-zero neutral padding)
     + ENC-023 (proved distant common triples on ENC-022)
     + ENC-024 (proved general bounded-block distant groups)
     + ENC-025 (proved general bounded-zero-run windows)
     + ENC-026 (proved tunable long-zero neutral block)
     + ENC-027 (proved balanced long-run slot product)
     + ENC-028 (proved disjoint positive-clause packing bound)
     + ENC-029 (proved linear common mixed-implication packing)
     + ENC-030 (proved implication-sparse translated-long-block slots)
     + ENC-031 (proved linear aligned common signed-triple packing)
     + ENC-032 (proved two-block full patterns on almost every distant triple)
     - GATE-004Q-NEUTRAL-HALO-ONLY (no-go by LEMMA-039)
     - GATE-004Q-RADIUS1-SCHEMA (no-go by LEMMA-040)
     - GATE-004Q-CONTEXT-CUBE-SCHEMA (no-go by LEMMA-041)
  <- GATE-004R (open alternative): radius-two SAT neighborhood rigidity
  <- GATE-004S (active parent): exact SAT expanded-cube rigidity
     - GATE-004S-OUTPUT-INCIDENCE-ONLY (no-go by LEMMA-042)
  <- GATE-004T (no-go): multi-witness column rigidity
     - LEMMA-043 (product-domain fresh-tail counterexample)
  <- GATE-004U (active smallest brick): syntax-linked DNF witness rigidity
     - GATE-004U-COMMON-PADDING-ONLY (no-go by LEMMA-044)
     - GATE-004U-RAW-COORDINATE-TAIL (no-go by LEMMA-045)
     - GATE-004U-NEUTRAL-CONTEXT-ONLY (no-go by LEMMA-046)
     - GATE-004U-TWO-BLOCK-CONTEXT-ONLY (no-go by LEMMA-048)
     - GATE-004U-BOUNDED-BLOCK-CONTEXTS (no-go by LEMMA-049)
     - GATE-004U-BOUNDED-ZERO-RUN-CONTEXTS (no-go by LEMMA-050)
     - GATE-004U-SINGLE-LONG-BLOCK-CONTEXTS (no-go by LEMMA-051/049)
  <- GATE-004V (active smallest brick): balanced long-run product rigidity
     - GATE-004V-DISJOINT-POSITIVE-CLAUSES (no-go by LEMMA-053)
     - GATE-004V-NAIVE-SIGNED-ADDITIVITY (no-go by LEMMA-054)
     - GATE-004V-NEGATIVE-UNIT-TAIL (no-go by LEMMA-055 and coordinate density)
     ! GATE-004W (active falsification audit): implication-tail minimality
       - GATE-004W-ESSENTIAL-RESTRICTION-ONLY (no-go by LEMMA-057)
       - GATE-004W-CONNECTIVITY-INVERSION-ONLY (no-go by LEMMA-058)
       - GATE-004W-FORMULA-BOUNDARY-ONLY (no-go by LEMMA-059)
  <- GATE-004X (active smallest positive brick): implication-sparse long-run rigidity
     + LEMMA-060 (proved signed-binary packing below the base floor)
     + LEMMA-061 (proved `P/4` common signed width-three packing)
     - GATE-004X-SIGNED-BINARY-ONLY (no-go by LEMMA-061)
     ! GATE-004Y (active falsification audit): signed-triple-tail minimality
       + LEMMA-062 (proved `K+3m` to `K+4m` cost bracket)
       + LEMMA-063 (proved global De Morgan compression)
       - GATE-004Y-CLAUSEWISE-MINIMALITY (no-go by LEMMA-064)
       ! GATE-004Z (active concrete audit): factorized signed-triple minimality
         + LEMMA-064 (proved `K+3m` to `K+4m` bracket and `5m` displayed classes)
         + LEMMA-065 (proved standalone exact size for `m<=4`)
         - GATE-004Z-FORMULA-BOUNDARY-ONLY (no-go by LEMMA-065)
         + LEMMA-066 (proved exact reduction to implication tails plus `m` gates)
         - GATE-004Z-STANDALONE-SEPARATE (no-go by LEMMA-066)
  <- GATE-004AA (no-go): one translated bounded block per option
     - LEMMA-067 (linear distant signed-triple packing)
  <- GATE-004AB (proved constructive brick): two-block neutral-alphabet
     sparsity for every disjoint common signed clause of width at most three
     + LEMMA-068 (proved distant partition complete except at most six triples)
     - GATE-004AB-ENC022-ALPHABET-ONLY (no-go by LEMMA-069)
     + LEMMA-070 (identifier-10/12 contexts repair interior aligned triples)
     + LEMMA-071 (proved seven-pattern universality and `78s` matching bound)
  <- GATE-004AC (active smallest positive brick): width-three-sparse rigidity

Stronger dependent-region branch:
  GATE-004I
  <- GATE-004J (active parent): loss from forced dependent region
     + ENC-009 (proved complementary columns)
     + ENC-010 (proved all-large-length padding)
     + LEMMA-021 (proved dependent-region size)
  <- GATE-004K (stronger sufficient route): compress actual dependent traces
     + LEMMA-023 (proved dependent/independent accounting)
  <- GATE-004L (stronger conservative route): labelwise disappeared-minus-split bias
     + LEMMA-024 (proved representative-free accounting)
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

## Active parent: GATE-004J

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

Raw semantic pigeonholing does not perform this transfer. With `k` boundary
signals there are `2^(2^k)-k-2` nonconstant non-coordinate functions, and
LEMMA-021 has `k=Omega(n^c)`. LEMMA-022 therefore shows that polynomially many
restricted gate occurrences occupy a negligible fraction of the possible
classes. `GATE-004J-BOUNDARY-PIGEONHOLE — NO-GO` requires the next attack to
prove a SAT-specific restriction on the trace family, not merely count its
formal inputs.

## Active parent: GATE-004K

LEMMA-023 removes the prefix-independent core from the missing inequality. If
`P` parent labels are prefix-dependent and their two restricted copies realize
`|T_j|` active functions, then

`S-q_j >= P-|T_j|`.

Thus only the actual dependent traces can create an excess over the stable
one-class-per-label baseline. GATE-004K asks for a polynomial positive average
of this exact deficit. Unlike raw pigeonholing, it is sensitive to the fact
that every trace comes from one shared minimum SAT circuit.

## Former conservative brick: GATE-004L

LEMMA-024 resolves the dependent trace set into parent-label contributions. If
`z_j` labels contribute no active residual and `t_j` contribute two, while
`kappa_j` counts cross-label collisions, then

`P-|T_j|=z_j-t_j+kappa_j`.

GATE-004L conservatively discards the helpful `kappa_j` term and asks for a
polynomial positive average of `z_j-t_j`. This is the exact survival
imbalance that a topology- or minimality-based charging argument must prove.

LEMMA-025 shows why minimality is indispensable. A removable even NOT chain
preserves every output but adds split labels under every pair, driving `z-t`
arbitrarily negative; repeated residual functions increase `kappa` and vanish
in the quotient. `GATE-004L-SEMANTICS-ONLY — NO-GO` blocks any proof that uses
only the computed function or conditioned-output distinctness. The next attack
must extract a quantitative trace restriction from minimum-circuit optimality.

Minimum size alone is still insufficient. LEMMA-026 exhibits a provably
minimum circuit with distinct active cofactors but `z=t=1`.
`GATE-004L-MINIMALITY-ONLY — NO-GO` therefore narrows the surviving proof
obligation to a genuinely SAT-specific relation across the full identifier
block; neither single-pair semantics nor generic optimality supplies a reserve.

LEMMA-027 identifies the first such SAT-specific relation, but it is adverse:
the output label splits for every identifier and contributes `-|J|` to the
aggregate. Any GATE-004L charging proof must pay this mandatory output charge,
all additional split labels, and then leave the full polynomial reserve. A
proof that omits the output label is quantitatively invalid.

Cycle 028 tests whether ENC-009 can be upgraded to a literal coordinate
subcube. `EXP-001 — NUMERICAL` exhaustively finds no one-bit-separated
equal-length `x_1`/`NOT x_1` formula pair through length 31; the first
distance-two pair occurs at length 15. This bounded result receives no
asymptotic credit. A coordinate-subcube route remains open only with a proof
or a gadget beyond the searched range.

ENC-011 replaces that bounded absence with a proof for the fixed-leaf route:
formula-code weight parity forces even Hamming distance whenever the leaf
multiset is fixed, and every identifier-1 formula has odd weight.
`GATE-004L-ONEBIT-FIXED-LEAVES — NO-GO` records the exact scope.

The failed one-bit search also reveals that a coordinate cube is unnecessary.
ENC-012 proves that the existing ENC-009 witnesses already form an
`|J|`-dimensional affine subspace with disjoint XOR directions. Conditioned SAT
restricts to the exact complementary INDEX matrix on that subspace. The next
GATE-004L attack may use this affine geometry, but no implication to labelwise
loss is currently claimed.

Cycle 030 audits that implication directly. LEMMA-028 constructs a total
fan-in-two Boolean extension of every such table using at most
`2R p+3R+p-1` gates, where `p` is the conditioned-prefix width. Here
`p=O(log R)`, so the entire table is compatible with `O(R log R)` circuit
size and, for `R=Theta(n^c)` with `c<1`, even `o(n)` size in the ambient length.
`GATE-004L-AFFINE-TABLE-ONLY — NO-GO` therefore blocks any transfer using only
the selected affine table. GATE-004L remains a valid stronger sufficient
theorem, but repeated audits show that discarding all collision terms is an
unnecessarily restrictive active strategy.

## Collision-aware route: GATE-004M

LEMMA-029 sharpens the earlier one-sided accounting. Let `A_j` be the active
residual functions from prefix-independent labels, `T_j` those from dependent
labels, `alpha_j=I-|A_j|`, and `lambda_j=|A_j intersect T_j|`. Then the full
joint quotient satisfies the exact identity

`S-q_j=alpha_j+z_j-t_j+kappa_j+lambda_j`.

The term `lambda_j` records dependent residuals that collapse onto the stable
suffix core; it was absent from GATE-004K and GATE-004L. In the minimum example
of LEMMA-026 it equals two and accounts for all quotient loss missed by `z-t`.

GATE-004M now asks for a polynomial average of
`z_j-t_j+kappa_j+lambda_j`, conservatively omitting only the nonnegative
`alpha_j`. This is sufficient for GATE-004I and is strictly weaker than the
older active proposals.

The first attempted shortcut fails exactly. LEMMA-030 constructs a circuit
whose output has two distinct active cofactors while every gate is
prefix-dependent, so `lambda=0`. `GATE-004M-OUTPUT-ONLY — NO-GO` blocks using
the mandatory output split alone. The next attack must connect minimum SAT
structure across many identifiers to stable-core collisions or to the other
terms in the exact identity.

Cycle 032 tests whether LEMMA-021's large suffix boundary supplies that
connection. It does not by counting alone: boundary signals may be raw suffix
inputs rather than prefix-independent gate functions. LEMMA-031 realizes the
entire affine complementary-INDEX matrix with distinct active non-input
cofactors, `4|J|` raw suffix-boundary nodes, and every circuit gate
prefix-dependent. Hence `I=0` and `lambda_j=0` for all pairs.
`GATE-004M-BOUNDARY-CORE — NO-GO` closes the boundary-only transfer. GATE-004M
remains active, but its next viable proof must use global minimum-circuit
factorization forced by SAT's off-table values, or extract the reserve from
`z`, `kappa`, and `alpha` rather than assuming a stable gate boundary.

## Adjacent route: GATE-004N

ENC-013 closes the auxiliary-leaf loophole left by NG-028. For every
bit-length-`L` identifier whose binary representation begins `11`, it gives
pointwise exact positive and negative literal formulas of length `6L+11`
whose encodings differ in exactly one bit. Their `AND(gadget,hole)` prefixes
have common length `6L+13`, remain exact even when the auxiliary identifier
occurs in the suffix, and form `2^(L-2)` adjacent conditioned-SAT pairs.

GATE-004N applies the full LEMMA-029 surplus to this adjacent family. The
assignment witnesses and LEMMA-021 still force a polynomial prefix-dependent
region, while the logarithmic restriction length preserves the GATE-004
recurrence. This makes adjacency a genuine added design constraint, not a
surrogate conclusion.

The first generic transfer nevertheless fails. LEMMA-032 proves that a minimum
circuit for `s XOR G` loses at most four gates under the adjacent cofactors
`G,NOT G`, regardless of the hard core's complexity.
`GATE-004N-ADJACENCY-ONLY — NO-GO` therefore requires the next attack to use
the simultaneous SAT-specific edge family and behavior on prefix rows outside
each edge.

## Context-trace route: GATE-004O

ENC-014 identifies the simultaneous geometry exactly. All supported pairs at
bit length `L` flip the same zero-based coordinate `3L+10`. After that bit is
removed, the identifier context `s` is copied into three disjoint coordinate
sets, so the entire row family is an `(L-1)`-dimensional affine subspace: one
unit edge direction and `L-2` disjoint context directions.

The common direction itself is insufficient. LEMMA-033 places influence on
every parallel edge in a four-gate `q XOR M(s,y)` shell, even when `M` realizes
the complete context INDEX table. `GATE-004N-DIRECTION-ONLY — NO-GO` records
that exact ceiling.

The context directions cannot all be compressed into that shell. LEMMA-034
fixes either polarity, substitutes the affine context parametrization into any
SAT circuit, and applies the complementary assignment columns. At least
`R=2^(L-2)` parent binary-gate traces in the resulting top region depend on
context. GATE-004O asks for a positive-power average elimination of this
specific region when the context is completely fixed. Proving it would yield
GATE-004 through the existing logarithmic-step recurrence.

Cycle 035 tests whether region size plus global minimality supplies that
elimination. LEMMA-035 gives a minimum `m`-gate chain in which every gate
depends on the context bit, but the two restricted copies have `2m-3`
distinct active classes. Its signed parent-to-quotient loss is `3-m`.
`GATE-004O-REGION-SIZE-ONLY — NO-GO` therefore rules out a generic
context-dependence charging argument. The surviving proof obligation must use
the simultaneous `2^R` SAT assignment columns across all `R` contexts to
prevent this split-heavy trace behavior.

Cycle 036 includes those shattering columns and still finds a precise generic
failure. LEMMA-036 gives a globally minimum circuit with parallel adjacent
pairs, a common branch union, every parent gate context-dependent, and all
`2^R` output columns over `R` one-hot contexts. Its exact per-pair loss is
`2R-m+2`, arbitrarily negative when the suffix tail `m` grows.
`GATE-004O-SHATTERING-ONLY — NO-GO` shows that shattering is not enough when
the context block has `R` coordinates.

## Rejected generic brick: GATE-004P

GATE-004P retains the remaining structural difference: the `R` SAT contexts
are every assignment of only `d=log_2 R` bits, embedded by ENC-014's disjoint
affine directions. It asks for polynomial average loss from global minimality,
common conditioned union, full shattering, and this compressed full-cube
context. ENC-013, ENC-014, ENC-009/010, and LEMMA-034 prove every hypothesis
for SAT and give an explicit implication to GATE-004O and then GATE-004.

Cycle 037 proves that even this compressed generic statement is false.
LEMMA-037 establishes the exact identity `C(f AND z)=C(f)+1` for a fresh
conjunctive input. LEMMA-038 appends a long fresh conjunction to
`w AND XNOR(q,y_s)`. The resulting ambient circuit is globally minimum,
satisfies the full compressed cube, common union, exact shattering, and
`U>=R`, yet every pair has loss at most `K-m`, negative for `m>K`.

## Active off-cube parent: GATE-004Q

GATE-004Q stops abstracting away the ambient language. It asks for the same
polynomial average loss only for minimum circuits computing the full total
`SAT-gamma_n` function on every prefix string. Its bridge to GATE-004 remains
the exact ENC-013 conditioned union and LEMMA-014 logarithmic recurrence.

ENC-015 classifies SAT's one-bit off-cube halo exactly. Each ENC-014 context
bit is repeated in three prefix positions, and independently flipping one
occurrence always produces another valid formula prefix. Of the six polarized
cases, two are neutral duplicates, one is neighboring negative conditioning,
one is the exact union `H_{j,0} OR H_{j',0}`, and two are positive/auxiliary
mixed unions. LEMMA-039 proves that neutral duplication alone has no generic
forcing power.

LEMMA-040 reproduces the radius-one table in an arbitrary total function.
ENC-016 then proves that all three repeated context blocks vary independently
to form a full affine formula cube, with exact closed-form SAT conditions.
LEMMA-041 reproduces that entire pointwise cube schema while retaining the
fresh-tail quotient expansion. Thus every-radius context-coordinate semantics
remain insufficient when treated only pointwise.

ENC-017 classifies the resulting output incidence exactly, including all
duplicate multiplicities. LEMMA-042 shows that the full static table still
survives a common fresh tail. ENC-018 exposes the next layer: suffix formulas
represent sets of assignments, so SAT residual columns are OR-closures of
assignment columns, with `3^R` compact ternary patterns already on the
diagonal.

LEMMA-043 realizes all ternary columns with product-domain allowance bits and
retains the exact-minimum fresh tail. GATE-004T is therefore `NO-GO`: even the
complete compact output-column family is insufficient without its input
locations.

GATE-004U is now the smallest attackable brick. It requires agreement at the
actual padded DNF suffix encodings and retains their formula-OR composition.
GATE-004S remains the exact-SAT parent and GATE-004R the non-context
radius-two alternative. No unrestricted loss bound is presently proved.

ENC-019 and LEMMA-044 show that one common growing outer padding block cannot
supply that rigidity: its fixed raw coordinates are an exact fresh tail. The
active audit now requires padding-dense DNF witnesses, including encodings
with only constant padding overhead and no growing common coordinate face.

ENC-020 supplies that density with `O(P)` neutral placements and LEMMA-045
proves that no raw-literal tail survives. The next GATE-004U attack concerns
non-coordinate predicates recognizing the dense witness language and whether
they can have an exact additive conjunction cost without circularly assuming
the desired circuit lower bound.

ENC-021 finds such a predicate without full recognition: `P/2` disjoint
distant OR clauses are one on the entire single-block ENC-020 family.
LEMMA-046 proves exact additive cost and recreates negative diagonal loss, so
ENC-020-only forcing is `NO-GO`. The active full gate now needs syntax
interactions with at least pairwise zero coverage on every large candidate
padding region; that coverage is a necessary defense against this tail, not a
sufficient lower-bound theorem.

ENC-022 composes one or two blocks from a fixed ten-block alphabet and zeros
every coordinate pair except four root-token pairs. LEMMA-047 shows those
exceptions have matching number two, so the exact disjoint paired-clause tail
cannot grow on the enlarged witness set. This repairs the cycle-045
counterexample but does not prove loss; the next GATE-004U audit concerns
overlapping or higher-width common predicates and the full DNF syntax set.

ENC-023 and LEMMA-048 immediately close the width-three audit: two localized
blocks leave `P/3` distant three-coordinate clauses common, and the general
width-`w` exact-cost identity again yields loss at most `K-m`. ENC-022-only
forcing is therefore `NO-GO`. The next syntax construction must supply
triple-zero coverage, while the broader audit must confront that every fixed
block count leaves a next-width clause predicate.

ENC-024 and LEMMA-049 close the whole sparse-block ladder. With `b` blocks,
the distant-group size `m=floor(P/(b+1))` gives an exact width-`b+1` clause
tail and loss at most `K-m` whenever `m` exceeds block length. Thus every
fixed block count, and every growing count with `m>K,D`, is `NO-GO`. The next
active audit must use unbounded sufficiently dense block count or exploit the
complete DNF syntax beyond an isolated outer-context family.

ENC-025 and LEMMA-050 close dense use of any bounded-zero-run alphabet as
well. Maximum zero run `rho` leaves `floor(P/(rho+1))` disjoint common window
clauses and loss at most `K-floor(P/(rho+1))`. The fixed ten-block alphabet
has `rho=7` even under linear block count. The next active audit must permit
zero runs on the `P/K` scale or exploit variable DNF core placement so that an
isolated outer predicate is unavailable.

ENC-026 supplies exact runs of any target length `rho` at encoding cost
`4rho` and sweeps the interior window predicates. LEMMA-051's simultaneous
audit shows that one such block re-enters the sparse-block obstruction:
half-separated width-two clauses give loss at most `K-floor(P/2)`. The next
construction must combine long runs with a dense enough independent block
count to cross both quantitative thresholds at once.

ENC-027 and LEMMA-052 build that combination. Independent slots preserve
coordinate density, allow run length `rho`, and force every LEMMA-049 cover
tail to at most `6s` clauses and the LEMMA-050 tail below `4s`. With
`s=floor((R-1)/8)` both counts lie below the unavoidable `K>=R-1` base-size
floor. GATE-004V is the new smallest sufficient brick: exact agreement on this
explicit product family must now be proved or falsified to force polynomial
diagonal loss.

ENC-028 and LEMMA-053 close GATE-004V's first counterexample class. The
all-long member has only `6s` one bits, so every disjoint common positive-
clause family has at most `6s<K` clauses and cannot make the established
`K-m` certificate negative. The next audit concerns signed clauses,
overlapping clauses, and non-clausal slot predicates.

### Smallest active brick: GATE-004U

The exact falsifiable statement, model card, and SAT bridge are in
`proofs/GATE-004U-syntax-linked-dnf-rigidity.md`.

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
