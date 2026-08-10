# No-go ledger

## NG-001 — terminal promotion of the Williams transfer

**Label: NO-GO**

Scope: the inference from a nontrivial algorithm for general Circuit-SAT to
`SAT notin P/poly` using only the currently audited Williams/Murray-Williams
transfer machinery.

Failure: known conclusions are high-class lower bounds or fixed-exponent NP
noncontainments. They do not provide one NP language hard for every polynomial
circuit exponent. Promoting them silently changes both the language quantifier
and the conclusion.

Model: uniform deterministic/co-nondeterministic Circuit-SAT algorithm;
unrestricted non-uniform fan-in-two Boolean circuits; unbounded depth; no
randomness, oracle, field, or extra advice; worst-case exact decision except the
explicit GAP-C-UNSAT promise in BR-MW18.

## NG-002 — tagged union without padding

**Label: NO-GO**

Scope: `L*={1^j0x : x in L_j}` when `L_j` has verifier time `n^{a(j)}` with
unbounded `a(j)`.

Failure: there is no fixed polynomial exponent bounding the verifier for `L*`
as `j` varies with the input. Therefore membership of `L*` in NP is unproved.

Model: one uniform nondeterministic multitape verifier; no circuits in the
failed membership step; no randomness, advice, oracle, promise, distribution,
or algebraic field; worst-case total-language verification.

## NG-003 — padding the Murray-Williams exponent ladder

**Label: NO-GO**

Scope: apply GATE-002 to BR-MW18 with `a(k)=c k^4/epsilon`, `b(k)=k`.

Failure: padding converts a target size `N^d` into source size
`n^{a(k)d}`. Contradiction needs `b(k)>a(k)d`, but
`b(k)/a(k)=epsilon/(c k^3)->0`. It cannot beat even one arbitrary target
exponent `d`, much less all of them.

Model: same as BR-MW18, instantiated to unrestricted general Boolean circuits
only if the theorem's “typical class” conditions and GAP algorithm premise are
met; non-uniform size `n^k`, unbounded depth, fan-in two, no randomness or
oracles, and an explicit gap promise in the algorithmic premise.

## NG-004 — medium-uniform lower bound promoted to P/poly

**Label: NO-GO**

Scope: infer a general non-uniform SAT lower bound from fixed-exponent lower
bounds against P-uniform or other medium-uniform circuit families.

Failure: arbitrary P/poly circuits need not have the stated generator. Removing
uniformity enlarges the adversary and invalidates the lower bound. The hard
language can also depend on the exponent.

Model: uniform language, generator-restricted circuit families, fixed
polynomial size, unrestricted depth unless the cited theorem says otherwise,
no randomness/oracle/field, worst-case exact decision.

## NG-005 — GATE-003 presented as a smaller brick

**Label: NO-GO**

Scope: use the unbounded exponent-ratio family of GATE-003 as an intermediate
milestone below `NP notsubseteq P/poly`.

Failure: GATE-002 proves the family implies `NP notsubseteq P/poly`. Conversely,
if one `L in NP` is outside `P/poly`, take `L_j=L`, a constant verifier exponent,
and lower-bound exponent `b(j)=j`. Thus the statements are equivalent. The gate
repackages the desired non-uniform separation and is not a decomposition.

Model: one uniform NP verifier family versus unrestricted non-uniform,
unbounded-depth, fan-in-two Boolean circuits; no randomness, advice on the
verifier side, oracle, field, promise, or distribution.

## NG-006 — reindex or pad the Murray-Williams family

**Label: NO-GO**

Scope: obtain the unbounded GATE-002 exponent ratio by computable reindexing or
standard polynomial padding of the BR-MW18 fixed-exponent family.

Failure: reindexing only selects existing ratios. Padding `N=n^q` divides both
the verifier-time exponent and transferable circuit exponent by `q`; their
ratio is preserved or reduced by the linear-time floor. The original ratio is
`epsilon/(c k^3)`, hence remains bounded and tends to zero along unbounded `k`.

Model: BR-MW18's uniform nondeterministic gap algorithm and time classes versus
general non-uniform circuits when instantiated to that class; unbounded depth,
fan-in two, no oracle or algebraic field, and the explicit gap promise.

## NG-007 — generic constant-substitution gate elimination for GATE-004

**Label: NO-GO**

Scope: prove the superlinear SAT lower bound in GATE-004 by the generic
gate-elimination framework whose induction step is established for all
functions/circuits using only a constant number of substitutions and constant
certified gate removal per step.

Failure: the GHKK16 limitation bounds such schemes by `c n` for a constant
depending on the local substitution budget. Summing constant certified progress
over at most `n` variable eliminations cannot yield `n^{1+delta}`. The theorem
does not exclude a SAT-specific induction step valid only for SAT and the
functions reached from SAT by the chosen substitutions.

Model: unrestricted acyclic Boolean circuits, non-uniform, unbounded depth,
bounded fan-in gate basis as instantiated, no randomness/advice/oracle/field,
worst-case exact Boolean function computation. The no-go is method-specific.

## NG-008 — double-NOT projection plus boundary fanout

**Label: NO-GO**

Scope: derive the GATE-004B gate-loss inequality solely by fixing the
`Theta(n^beta)` prefix bits supplied by ENC-002 and averaging their direct
fanout in an arbitrary size-`n^(1+delta)` circuit.

Failure: circuit size measures gates, not input-edge incidence. A large
downstream subcircuit can be reached through low-fanout buffers, so the specified
prefix coordinates can touch only `O(n^beta)` immediately removable gates even
when the total circuit is much larger. Boundary fanout does not certify
propagation through the downstream DAG. Concretely, a circuit for
`G(z) OR (AND_i x_i)` can have an arbitrarily large `G` subcircuit while every
`x_i` has fanout one; setting all `x_i=0` removes only the `O(t)`-gate AND branch.
No semantic property of a *minimum SAT circuit* was used, so the desired
`n^(beta+delta)` loss does not follow.

Model: exact `SAT-gamma` slices; unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. The no-go concerns the generic
fanout-only inference, not GATE-004B itself.

## NG-009 — right syntax context as an exact total-language projection

**Label: NO-GO**

Scope: diversify exact SAT-gamma projections by placing the source before a
fixed tautology, using `x -> AND(x,T)`.

Failure: total-language validity is not preserved. Let `V` be a valid variable
encoding and let malformed `x=V 11`, where `11` is a truncated NOT token. Then
`AND(x,T)` parses as the valid formula `AND(V,NOT(T))`. Fixed suffix bits can
repair malformed trailing syntax, so this context is not a projection of the
exact SAT-gamma slice.

Model: exact SAT-gamma prefix grammar and coordinate projections; no circuit
size, depth, uniformity, randomness, advice, oracle, field, promise, or
distributional assertion. The no-go concerns this proposed right-context
construction, not all possible non-prefix projections.

## NG-010 — contiguous placements plus coordinate-weight averaging

**Label: NO-GO**

Scope: even granting an exact family of arbitrary contiguous source placements,
derive GATE-004B loss by averaging weights assigned to fixed input coordinates.

Failure: if the padding length is `p<n/2`, every length-`n-p` contiguous source
placement contains a common core of `n-2p` target coordinates. All coordinate
weight may be concentrated on one common-core coordinate, so every placement
fixes weight zero. Thus no positive fixed-weight bound—hence no superlinear
gate-loss bound—follows from total coordinate weight alone. This is the exact
combinatorial statement proved in LEMMA-003.

Model: exact SAT-gamma context projections; unrestricted non-uniform acyclic
circuits at the input-boundary abstraction; unbounded depth; fan-in-two AND/OR
and fan-in-one NOT; no randomness, advice, oracle, field, promise, or
distribution. The no-go does not constrain semantic structure of minimum SAT
circuits, non-contiguous projections, or GATE-004B itself.

## NG-011 — minimality plus maximal input-residual diversity

**Label: NO-GO**

Scope: infer the GATE-004C superlinear block loss from circuit minimality,
essentiality of every restricted coordinate, and the fact that the `p`-bit
block induces many distinct residual output functions.

Failure: LEMMA-004 constructs

`F(x,w,u)=G(u) XOR XOR_i(x_i AND w_i)`.

Every `x_i` is essential and the `2^p` restrictions of `x` give pairwise
distinct residual functions—the maximum possible. Nevertheless every residual
has minimum circuit complexity within `5p+3` gates of `F`. A large `G(u)` core
is shared by all restrictions, while only an `O(p)` shell changes. Therefore
these generic semantic properties cannot imply the required
`p n^delta`-scale loss.

Model: exact minimum gate count for unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. This is a generic method limitation,
not a claim about SAT-gamma; SAT-specific internal residual-gate collisions
remain possible.

## NG-012 — lift neutral parser states to internal circuit collisions

**Label: NO-GO**

Scope: infer GATE-004D solely from multiple separated prefix assignments that
leave the same output residual function, together with essentiality of all
prefix coordinates and circuit minimality.

Failure: LEMMA-007 hardwires any separated neutral set `A` into a decoder and
defines

`F(a,w,z)=G(z) XOR (OUT_A(a) AND w)`.

Every assignment in `A` leaves the identical arbitrary core `G`; every prefix
coordinate remains essential; and the shell has at most `2p|A|+5` gates.
Thus the complete output-level parser-state pattern can coexist with an
arbitrarily complex core shared intact by all neutral restrictions. The
premises do not imply collisions among internal core gates or a loss scaling
with core complexity.

Model: exact minimum gate count in unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, oracle,
field, promise, or distribution. The neutral set is part of the counterexample
function definition. The no-go concerns the generic lifting inference, not the
SAT-specific GATE-004D or GATE-004E statements.

## NG-013 — neutral-family cross-table statistics

**Label: NO-GO**

Scope: infer GATE-004E from the exact neutral family’s output equality,
pairwise Hamming geometry, regular parser-state description, essentiality of
every prefix coordinate, and circuit minimality.

Failure: the ENC-004 prefixes, grouped into twelve-bit blocks, form exactly the
regular set `X*W*`. LEMMA-008 recognizes this set with at most `3p` gates and
uses the recognizer to place the whole family in front of an arbitrary shared
core `G`. Every neutral restriction is exactly `G`, every prefix coordinate is
essential, and a minimum circuit can differ from `G` by at most `3p+5` gates.
Thus these complete output-level cross-table statistics do not force
same-column collisions among core gates or any loss depending on core
complexity.

Model: exact minimum gate count in unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, oracle,
field, promise, or distribution. The no-go is generic and method-specific; it
does not refute an additional internal property special to minimum SAT-gamma
circuits.

## NG-014 — adjacent annihilating parser state

**Label: NO-GO**

Scope: use the ENC-005 constant-zero residual, only two prefix bits away from a
neutral SAT residual, to force substantial gate loss in the neutral column.

Failure: LEMMA-009 takes any nonzero core `G` and forms `F(s,z)=s AND G(z)`.
The selector is essential, the zero cofactor is constant, and the hard
cofactor is exactly `G`, but selecting the hard cofactor can remove at most one
gate from a minimum circuit. A circuit may isolate the entire core behind a
constant-size selector. Proximity and annihilation of the neighboring column
do not force collisions inside the retained column.

Model: exact minimum gate count in unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. The no-go concerns the generic
cofactor-pair inference, not a stronger SAT-specific invariant of the full
operator-bit cofactor table.

## NG-015 — complete local operator-bit cofactor square

**Label: NO-GO**

Scope: strengthen NG-014 by using all four cofactors of the two inner operator
bits in the ENC-006 twelve-bit context.

Failure: ENC-006 computes the exact table: token `10` leaves the SAT suffix
function and each of `00`, `01`, `11` leaves constant zero for every nonempty
suffix length. LEMMA-010 reproduces that complete table as

`q_1 AND NOT(q_2) AND G`.

Both selector bits are essential, but selecting the unique hard cofactor can
remove at most three gates from a minimum circuit. The whole local table is a
constant-size one-hot selector around an arbitrary core and therefore does not
force same-column collisions inside that core.

Model: exact minimum gate count in unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. The no-go is confined to this local
output-cofactor inference; longer SAT-prefix residuals remain unaudited.

## NG-016 — direct sum from conditioned-branch union

**Label: NO-GO**

Scope: infer the GATE-004G joint compression from the facts that two
conditioned residuals are distinct, disjoint, and have pointwise OR equal to
the original hard function.

Failure: LEMMA-011 takes an arbitrary nonzero core `G` and defines conditioned
branches `G AND NOT(t)` and `G AND t`. They are distinct, disjoint, and their
OR is `G`. A shared circuit computes both with only three gates beyond `G`, and
the corresponding selector parent `G AND (s XNOR t)` is within seven gates of
the minimum shared-pair complexity. Thus these output relations do not imply
an `Omega(n^delta)` joint quotient gap or any generic direct-sum surplus.

Model: exact minimum gate count for unrestricted non-uniform single- and
two-output acyclic circuits; unbounded depth; fan-in-two AND/OR and fan-in-one
NOT; no randomness, advice, oracle, field, promise, or distribution. This
no-go does not refute a SAT-specific constraint on internal sharing between
`CSAT_0` and `CSAT_1`.

## NG-017 — OR two separately simplified conditioned copies

**Label: NO-GO**

Scope: prove modest savings in each conditioned restriction separately, add
the two resulting circuits, and infer a smaller circuit for their OR.

Failure: the construction starts from two copies of an `S`-gate parent.
LEMMA-012 proves the exact identity

`q_J=2S-ell_0-ell_1-x`,

where `ell_b` is the individual loss and `x` is cross-copy sharing. To beat the
single parent by `L`, the total `ell_0+ell_1+x` must be at least `S+L`.
Separate `L`-scale branch savings do not even cancel the extra copy when
`S>>L`. ORing the branches without paying this duplication term silently
introduces a factor two and destroys the recurrence.

Model: exact gate accounting for unrestricted non-uniform acyclic circuits;
unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. The no-go does not refute a
SAT-specific proof of the full joint surplus required by GATE-004G.

## NG-018 — promote multi-output literature to the conditioned-SAT gap

**Label: NO-GO**

Scope: cite amortized circuit-complexity duality or NP-hardness of multi-output
circuit minimization as if either established GATE-004G.

Failure: RZ21 studies asymptotically many *identical* outputs on the same input;
in general circuits, arbitrary fanout makes the amortized cost per identical
copy `O(1)`. GATE-004G instead asks for a quantitative gap for two different
conditioned functions. ILO20 proves that finding a minimum circuit for an
arbitrary truth-table-given multi-output function is NP-hard under a randomized
reduction. Hardness of the minimization problem is not a circuit-size lower
bound for the explicit pair `(CSAT_0,CSAT_1)`. Neither result supplies the
required `B n^delta` surplus.

Model: general unrestricted finite-gate Boolean circuits with arbitrary
fanout; exact multi-output computation; RZ21's identical-copy amortized limit
and ILO20's randomized truth-table minimization reduction. No randomness,
advice, oracle, field, promise, or distribution is allowed in the desired
GATE-004G lower bound. This no-go is a scope audit, not a criticism of either
source theorem.

## NG-019 — condition-sensitive gate count as joint surplus

**Label: NO-GO**

Scope: count gates whose residual functions differ between `R_0` and `R_1`
and infer that many gates disappear in the joint conditioned quotient.

Failure: LEMMA-013 gives the signed identity `S-q_J=d-t`. A gate with equal
residuals cannot be a split label, but sensitivity only makes splitting
possible; it does not force disappearance or a favorable `d-t` balance.
LEMMA-011 exhibits the generic selector shell around an arbitrary core: the
conditioned outputs differ and selector gates are sensitive, yet the minimum
parent-to-shared-pair gap is at most seven. Output distinction and raw
sensitivity therefore do not yield `Omega(n^delta)` surplus.

Model: exact minimum gate count in unrestricted non-uniform single- and
two-output acyclic circuits; unbounded depth; fan-in-two AND/OR and fan-in-one
NOT; no randomness, advice, oracle, field, promise, or distribution. The no-go
does not refute a SAT-specific structural injection from split labels to a
larger set of disappeared labels.

## NG-020 — candidate multiplicity as quotient loss

**Label: NO-GO**

Scope: infer a positive, superconstant, or polynomial joint-quotient gap from
the existence of polynomially many distinct equal-length restriction pairs
whose two outputs OR back to the parent function.

Failure: LEMMA-016 takes a parent function independent of all designated
prefix inputs. Arbitrarily many distinct prefix pairs then retain the same
hard core, reconstruct it by OR, and have zero parent-to-joint gap for every
pair. LEMMA-015 shows that adding columns only helps after a positive signed
incidence total has been proved; it does not create that total.

Model: exact minimum gate count in unrestricted non-uniform acyclic circuits;
unbounded depth; fixed complete Boolean basis; no randomness, advice, oracle,
field, promise, or distribution. SAT-gamma does depend on its prefixes, so the
no-go leaves open a quantitative SAT-specific aggregate surplus theorem.

## NG-021 — essential prefix dependence as polynomial aggregate surplus

**Label: NO-GO**

Scope: repair NG-020 by additionally requiring that the parent function depend
essentially on every prefix coordinate, then infer a polynomial
parent-to-conditioned-pair gap when the prefix length is logarithmic.

Failure: LEMMA-017 places all essential prefix dependence in a parity selector
of at most `4p-4` gates around an arbitrary nonzero core. Exponentially many
odd-parity prefix pairs retain the identical core and OR back to it, while the
function-level parent-to-minimum-pair gap is at most `4p-3`. For
`p=O(log n)` this is only `O(log n)`, not `Omega(n^delta)`.

Model: exact minimum gate count in unrestricted non-uniform single- and
two-output acyclic circuits; unbounded depth; fan-in-two AND/OR and fan-in-one
NOT; no randomness, advice, oracle, field, promise, or distribution. The
result does not refute a theorem using the distinct internal structure of
SAT's conditioned residuals.
