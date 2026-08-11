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

## NG-022 — complementary shattering via essential-coordinate counting

**Label: NO-GO**

Scope: transfer ENC-009's `2^R` complementary output columns to GATE-004I by
counting the suffix coordinates on which the parent function depends and then
counting the gates needed to connect those inputs.

Failure: LEMMA-018 proves the strongest direct conclusion of this argument:
at least `R` essential suffix coordinates and `R-1` binary gates. With the
explicit ENC-009 witnesses, total input length is `Theta(R log R)`, so the
result is only `Omega(n/log n)` on the constructed lengths. More decisively,
it is an absolute lower bound on the parent and contains no term comparing
parent size with any joint quotient `q_j`. It therefore supplies neither the
superlinear GATE-004 bound nor the signed aggregate loss required by GATE-004I.

Model: exact unrestricted non-uniform acyclic circuits; unbounded depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, field,
promise, or distribution. The no-go is specific to support/connectedness
counting and does not exclude a stronger SAT-specific internal trace theorem.

## NG-023 — unrestricted depth reduction plus component count

**Label: NO-GO**

Scope: use GKW20's representation of every size-`s` unrestricted circuit as
an OR of `2^(s/3.9)` width-16 CNFs, prove that SAT needs many such components,
and infer a superlinear circuit lower bound solely from the component count.

Failure: LEMMA-019 gives every `n`-bit Boolean function an exact OR cover by at
most `2^n` width-one CNFs, one per accepting input. Hence the logarithm of any
valid minimum-component lower bound is at most `n`. Inserted into the GKW20
reduction, component count can certify at most `3.9n`, never `n^(1+delta)`.

The related GKST17 substitution framework likewise does not supply the open
GATE-004I measure drop: sufficient loss under an allowed substitution is the
framework's technical input, not its output.

Model: exact unrestricted non-uniform Boolean circuits and exact ORs of
bounded-width CNFs; unbounded parent depth; no randomness, advice, oracle,
field, promise, or distribution. The no-go leaves open methods using richer
component structure or a separately proved SAT-specific quotient theorem.

## NG-024 — globally pooling all conditioned copies

**Label: NO-GO**

Scope: quotient all `2|J|` conditioned copies at once, observe extensive
cross-identifier sharing, and promote the small global class count to an
average improvement for one identifier pair.

Failure: LEMMA-020 gives the exact identity

`sum_j(S-q_j)=|J|S-Q-X`,

where `Q` is the global quotient size and `X` counts repeat appearances of a
global class in different pairwise quotients. The unchanged-core example has
`Q=S`, an apparent saving of `(|J|-1)S` against duplicated copies, but
`X=(|J|-1)S` and every `q_j=S`. All global sharing is cross-candidate reuse and
produces zero pairwise improvement.

Model: exact unrestricted non-uniform multi-output acyclic circuits; unbounded
depth; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle,
field, promise, or distribution. The no-go does not exclude a SAT-specific
upper bound on the full quantity `Q+X=sum_j q_j`.

## NG-025 — pigeonholing dependent-region residual functions

**Label: NO-GO**

Scope: use LEMMA-021's polynomially large prefix-dependent region, observe that
every restricted gate becomes a function of the suffix-boundary signals, and
infer many semantic collisions merely because there are many gate occurrences.

Failure: LEMMA-022 counts `2^(2^k)-k-2` possible nonconstant, non-coordinate
functions of `k` boundary bits. LEMMA-021 gives `k=Omega(n^c)`, so this class
universe is double-exponential in a polynomial of `n`. Two copies of any
polynomial-size region contain only polynomially many gate occurrences and do
not trigger the pigeonhole principle. “Many dependent gates” is therefore not
quantitatively close to “more gates than residual functions.”

Model: exact unrestricted non-uniform semantic residual classes; unbounded
depth; fan-in-two AND/OR and fan-in-one NOT in the parent; no randomness,
advice, oracle, field, promise, or distribution. The no-go leaves open a
SAT-specific theorem placing actual residual traces in a far smaller family.

## NG-026 — deriving labelwise bias from output semantics alone

**Label: NO-GO**

Scope: infer a positive disappeared-minus-split score `z_j-t_j` from exact SAT
semantics, conditioned-output distinctness, or the existence of a large
prefix-dependent region, without quantitatively invoking parent-circuit
minimality or cross-label collisions.

Failure: LEMMA-025 appends arbitrarily long even NOT chains without changing
the function. Every new label splits into two active conditioned residuals, so
`z_j-t_j` falls by the chain length for every identifier. The exact trace
deficit is not harmed because the repeated output/complement functions create
an offsetting cross-label collision surplus and vanish in the semantic
quotient.

Model: exact unrestricted non-uniform circuits and semantic paired quotients;
unbounded depth; fan-in-one NOT with the parent AND/OR basis; no randomness,
advice, oracle, field, promise, or distribution. The construction is
deliberately nonminimum and therefore leaves GATE-004L open only as a
minimality-sensitive theorem.

## NG-027 — minimum size plus distinct active cofactors

**Label: NO-GO**

Scope: repair NG-026 by assuming the parent circuit is globally minimum, then
infer a strictly positive disappeared-minus-split label score from minimum
size, prefix dependence, and two distinct active cofactors alone.

Failure: LEMMA-026 gives an explicit five-input function with a provably
minimum five-gate AND/OR/NOT circuit. Its two `x`-cofactors are the distinct
active functions `g OR h` and `h`, but its dependent labels have exactly one
zero-residual label and one split label. Hence `z-t=0`, not positive.

Model: exact globally minimum unrestricted non-uniform circuits; unbounded
depth in the lower bound; fan-in-two AND/OR and fan-in-one NOT; no randomness,
advice, oracle, field, promise, or distribution. The example is not SAT-gamma
and has only one restriction pair, so the no-go leaves open a theorem using
SAT's full multi-identifier trace relations.

## NG-028 — one-bit polarity gadget with fixed leaf data

**Label: NO-GO**

Scope: upgrade ENC-009 to a coordinate subcube by finding two valid
equal-length polarity gadgets at Hamming distance one while keeping the same
leaf-identifier multiset, or by using only identifier 1.

Failure: ENC-011 proves that the encoding-weight parity is determined by the
leaf multiset. Equal leaf data therefore forces even Hamming distance. Every
identifier-1 formula has odd encoding weight regardless of its tree, so no two
such formulas can differ in exactly one bit.

Model: exact SAT-gamma syntax and Hamming geometry; arbitrary formula depth;
no circuit restriction, randomness, advice, oracle, field computation,
promise, or distribution. The no-go does not exclude one-bit gadgets using
different auxiliary leaf multisets. ENC-012 shows that a coordinate cube is
unnecessary for the current witnesses: they already form an affine subspace
with multi-bit independent directions.

## NG-029 — affine complementary-INDEX table alone

**Label: NO-GO**

Scope: infer a superlinear unrestricted-circuit lower bound, a positive
parent-minus-joint-quotient loss, or GATE-004L's labelwise bias using only the
facts that selected suffix witnesses form an affine subspace with disjoint
directions and selected conditioned rows realize complementary INDEX.

Failure: LEMMA-028 constructs, for every such `R`-coordinate table with
`p`-bit distinct prefix rows, a total Boolean extension computed by a
fan-in-two AND/OR and fan-in-one NOT circuit of size at most
`2Rp+3R+p-1`. For the exact conditioned-row width `p=O(log R)`, this is
`O(R log R)`; for the repository's `R=Theta(n^c)`, fixed `0<c<1`, it is
`o(n)`. The extension matches every selected row/subspace value and differs
from SAT only away from the audited table. Therefore no universal implication
from the table data alone can establish the required loss.

Model: total non-uniform unrestricted Boolean circuits; unbounded size outside
the explicit upper bound, depth at most logarithmic in the construction,
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. Affine notation is over `F_2` only.
The no-go does not give a small circuit for SAT-gamma and leaves open arguments
using SAT's off-table values, global minimum-circuit structure tied to those
values, or cross-label collision surplus `kappa`.

## NG-030 — mandatory output split forces a stable-core collision

**Label: NO-GO**

Scope: infer `lambda_j>0` in LEMMA-029 solely because the parent output has
two distinct active residual functions under a prefix-restriction pair.

Failure: LEMMA-030 gives an explicit eight-gate circuit with cofactors
`y_1 AND y_2` and `w_1 AND w_2`. Every one of its gate functions depends on
the prefix bit, so there is no prefix-independent active set at all and
`lambda=0`. The output nevertheless splits into two distinct active non-input
functions.

Model: one exact non-uniform unrestricted circuit; depth four; fan-in-two
AND/OR and fan-in-one NOT; no randomness, advice, oracle, field, promise, or
distribution. The circuit is not claimed minimum and is not SAT-gamma. Thus
the no-go blocks only output-semantics-only compensation; GATE-004M remains
open for a minimum-SAT, multi-identifier argument.

## NG-031 — suffix-boundary count forces a stable gate core

**Label: NO-GO**

Scope: infer a polynomial lower bound on `lambda_j`, or even on the number of
prefix-independent gate labels, from LEMMA-021's polynomial number of suffix-
boundary signals together with the affine complementary-INDEX table and
distinct active conditioned output functions.

Failure: LEMMA-031 constructs the full multi-identifier table with `4R` raw
suffix-input boundary nodes and no prefix-independent gate at all. Every gate
depends semantically on the prefix block, while each selected cofactor is a
distinct two-input AND and the suffix witnesses retain disjoint affine
directions. Consequently `I=0` and `lambda_j=0` for every pair despite meeting
the audited boundary and output hypotheses.

Model: an explicit total non-uniform AND/OR/NOT circuit family of size
`2Rp+4R+p-1` and logarithmic depth; fan-in-two AND/OR and fan-in-one NOT; no
randomness, advice, oracle, promise, distribution, or algebraic computation.
The circuit is not claimed minimum and is not SAT-gamma. The no-go therefore
blocks the boundary-only inference, not GATE-004M's minimum-SAT theorem.

## NG-032 — adjacency plus minimum size forces growing loss

**Label: NO-GO**

Scope: infer superconstant parent-to-joint-quotient loss from one-bit adjacency,
two complementary active cofactors, and global minimum circuit size, without
using relations across many SAT-specific edges.

Failure: LEMMA-032 takes an arbitrary hard function `G` and defines
`F(s,y)=s XOR G(y)`. A minimum circuit for `F` has size at most `C(G)+4`, while
the joint quotient under `s=0,1` has size at least `C(G)` because one output is
`G`. Thus the loss is at most four even as the shared core complexity grows
without bound.

Model: exact minimum unrestricted non-uniform AND/OR/NOT circuits; one prefix
bit; unbounded depth; fan-in-two AND/OR and fan-in-one NOT; no randomness,
advice, oracle, field, promise, or distribution. The no-go is not SAT-gamma and
has only one edge, so GATE-004N remains open for the simultaneous polynomial
family of adjacent SAT conditioning pairs.

## NG-033 — parallel edge influence forces a large edge-dependent region

**Label: NO-GO**

Scope: infer polynomially many gates depending on the common flip coordinate
from output sensitivity on every edge of ENC-014's parallel family, even when
the context residuals realize complementary INDEX.

Failure: LEMMA-033 wraps any context function `M(s,y)` in the four-gate shell
`q XOR M(s,y)`. All gates computing `M` are independent of `q`, only four new
gates can depend on it, and every context still has the complementary adjacent
cofactors `M(s,.)` and `NOT M(s,.)`. Choosing `M` as a context multiplexer
reproduces the full output table without expanding the edge-direction shell.

Model: exact unrestricted non-uniform AND/OR/NOT circuits; arbitrary context
and suffix dimensions; core depth unrestricted and shell depth constant;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, field,
promise, or distribution. The no-go concerns only dependence on the common
edge bit. LEMMA-034 separately forces a large context-dependent region, which
GATE-004O must eliminate on average.

## NG-034 — minimum context-region size forces positive quotient loss

**Label: NO-GO**

Scope: infer positive, let alone polynomial, joint-quotient loss solely from
global minimum circuit size and an arbitrarily large top region in which every
gate depends semantically on the context.

Failure: LEMMA-035 proves that
`F_m=(s OR y_1) AND y_2 AND ... AND y_m` has minimum circuit size exactly `m`,
with all `m` displayed gates depending on `s`. After the two context
restrictions, its semantic joint quotient contains the `m-1` distinct
functions `y_1 AND ... AND y_k` and the `m-2` distinct functions
`y_2 AND ... AND y_k`, for exact size `2m-3`. The signed loss is `3-m`, which
is nonpositive and tends to negative infinity.

Model: exact globally minimum non-uniform AND/OR circuits; one context bit;
parent depth `m` but lower bound depth unrestricted; fan-in two; no NOT,
randomness, advice, oracle, field, promise, or distribution. The construction
has only two contexts and no SAT assignment-column shattering, so GATE-004O
remains open only as a simultaneous SAT-specific theorem.

## NG-035 — parallel shattering plus minimum size forces positive loss

**Label: NO-GO**

Scope: infer positive average joint-quotient loss from global minimum size,
parallel adjacent pairs, one common OR of the two branch residuals, all `2^R`
output columns over `R` contexts, and semantic context dependence of every
parent gate, without using a compressed full context cube.

Failure: LEMMA-036 constructs a minimum `2R+m`-gate circuit satisfying every
listed property on the `R` one-hot contexts `e_i`. Every pair's exact joint
quotient has size `2m-2`, so its signed loss is `2R-m+2`. Taking
`m>2R+2` makes every loss negative, and increasing `m` makes the failure
arbitrarily large. The branch union remains the same suffix conjunction for
every context, while explicit witnesses realize all `2^R` vectors.

Model: exact globally minimum non-uniform AND/OR circuits; an `R`-bit one-hot
context block and one common adjacent edge bit; depth unrestricted in the
minimum lower bound; fan-in two; no NOT, randomness, advice, oracle, field,
promise, or distribution. The obstruction does not use all assignments of a
`log_2 R`-bit context cube. GATE-004P isolates that remaining compact-context
hypothesis and its proved SAT bridge.

## NG-036 — compressed full-cube shattering forces positive loss

**Label: NO-GO**

Scope: infer positive polynomial average loss from an affine embedded full
`d`-bit context cube with `R=2^d`, parallel adjacent pairs, one common branch
union, exact complementary `2^R` shattering, ambient minimum-circuit size, and
at least `R` context-dependent trace gates.

Failure: LEMMA-037 first proves that conjoining one fresh input raises exact
minimum circuit size by exactly one. LEMMA-038 applies this to the base
`w AND XNOR(q,y_s)` and an `m`-gate fresh conjunction tail. The resulting
ambient minimum circuit has size `K+m`, satisfies the identity compressed-cube
embedding and every other hypothesis, has `U>=m`, and leaves at least `2m`
distinct active tail classes in every joint quotient. Thus loss is at most
`K-m`, negative whenever `m>K`, including choices with `m>=R`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; identity affine
edge/context cube with `d=log_2 R`; unrestricted base depth and an AND tail;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. The construction is not SAT-gamma.
It proves that the next gate must use SAT's values outside the embedded cube or
another genuinely SAT-specific ambient relation.

## NG-037 — neutral off-cube duplicates force quotient loss

**Label: NO-GO**

Scope: infer gate disappearance, collision, or positive parent-to-quotient
loss solely because a one-bit off-cube neighbor computes exactly the same
residual as its adjacent embedded row, even when the ambient circuit is
globally minimum.

Failure: LEMMA-039 extends an arbitrary function `H(r,y)` to
`F(u,r,y)=H(r,y)` on a fresh coordinate. Restriction and lifting prove the
exact identity `C(F)=C(H)`, and a minimum implementation ignores `u` at every
gate while its two adjacent rows are identical. Thus semantic duplication
alone has zero generic forcing power.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; depth
unrestricted; fan-in-two AND/OR and fan-in-one NOT; no randomness, advice,
oracle, field, promise, or distribution. This obstruction applies only to the
two neutral cases in ENC-015. It does not address the four mixed SAT-specific
halo relations, especially the exact union
`H_{j,0} OR H_{j',0}`.

## NG-038 — the complete radius-one halo schema forces quotient loss

**Label: NO-GO**

Scope: infer positive parent-to-joint-quotient loss from ambient minimality,
the full compressed affine cube, common branch union, exact shattering, a
large context-dependent trace region, and all six pointwise ENC-015 relations
on every single-occurrence off-cube neighbor.

Failure: LEMMA-040 constructs one total lookup function on a triplicated
context block that realizes all designated cube and halo rows simultaneously.
The two equal context copies uniquely identify the base row, so the halo
requirements do not conflict. Conjoining `m` fresh inputs raises the exact
minimum parent size from `K_d` to `K_d+m`, while every cube-pair quotient
retains at least `2m` distinct tail classes. Its signed loss is therefore at
most `K_d-m`, negative for `m>K_d`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; a full
`d`-bit context cube with three disjoint copies and its complete radius-one
halo; base depth unrestricted and a fresh AND tail; fan-in-two AND/OR and
fan-in-one NOT; no randomness, advice, oracle, promise, distribution, or
algebraic computation. The construction matches the pointwise six-case
relation schema but is not SAT-gamma. It does not match SAT's exact residual
functions on all suffix strings or impose radius-two compatibility.

## NG-039 — the full expanded context-cube schema forces quotient loss

**Label: NO-GO**

Scope: infer positive diagonal parent-to-joint-quotient loss from ambient
minimality, every GATE-004P diagonal property, and the complete pointwise
ENC-016 semantic schema across all independent settings of the three repeated
context blocks and polarity.

Failure: LEMMA-041 defines one total function directly by the two ENC-016
Boolean conditions on the entire `(3d+1)`-dimensional expanded cube. On its
diagonal it reduces to `w AND XNOR(q,y_s)`. Appending `m` fresh conjuncts
raises exact minimum size from `K_d` to `K_d+m` but leaves `2m` distinct tail
classes in every diagonal quotient. Loss is at most `K_d-m`, negative for
`m>K_d`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; a full affine
expanded context cube with `3d+1` independent coordinates; unrestricted base
depth and a fresh AND tail; fan-in-two AND/OR and fan-in-one NOT; no
randomness, advice, oracle, promise, distribution, or algebraic computation.
The counterexample matches every pointwise formula condition but is not
SAT-gamma. It does not reproduce existential satisfiability of those
conditions conjoined with every possible encoded suffix formula.

## NG-040 — exact expanded output incidence forces quotient loss

**Label: NO-GO**

Scope: infer positive diagonal parent-to-joint-quotient loss from ambient
minimality, every GATE-004P diagonal property, and the exact ENC-017 equality
classes and multiplicities among all `2R^3` expanded-row output functions.

Failure: LEMMA-042 observes that the LEMMA-041 counterexample multiplies each
ENC-017 condition by a common input `w`. Equality of `w AND g` and `w AND h`
is equivalent to equality of `g` and `h`, so the entire cubic incidence table
is preserved exactly. A further fresh conjunction tail also preserves it,
while exact minimum parent size is `K_d+m`, each diagonal quotient has at
least `2m` tail classes, and loss is at most `K_d-m`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; full expanded
affine context cube and exact static output-incidence table; unrestricted base
depth and a fresh AND tail; fan-in-two AND/OR and fan-in-one NOT; no
randomness, advice, oracle, promise, distribution, or algebraic computation.
The construction lacks SAT's compact multi-witness columns, including suffixes
for which both polarities of many conditioned variables are satisfiable.

## NG-041 — compact ternary multi-witness columns force quotient loss

**Label: NO-GO**

Scope: infer positive diagonal parent-to-joint-quotient loss from ambient
minimality, exact ENC-017 expanded incidence, the common diagonal union,
complete-assignment columns, and all `3^R` compact ternary columns allowing
zero, one, or both polarities independently at every diagonal context.

Failure: LEMMA-043 gives each primary and auxiliary variable two domain bits
indicating whether zero and one are allowed. Each expanded output reports
whether its ENC-016 condition is feasible in that product domain. Singleton
domains preserve exact incidence; three primary-domain choices realize all
ternary columns; and diagonal branches OR to common domain validity. Appending
`m` fresh conjuncts yields exact minimum size `K_d+m`, at least `2m` diagonal
quotient classes, and loss at most `K_d-m<0`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; full affine
expanded prefix cube; `4R` product-domain allowance bits and an arbitrary
fresh AND tail; base size `O(R+L)` and unrestricted depth; fan-in-two AND/OR
and fan-in-one NOT; no randomness, advice, oracle, promise, distribution, or
algebraic computation. The construction matches the column set but not the
actual bit-level formula encodings that produce SAT's columns.

## NG-042 — common outer padding preserves syntax-linked forcing

**Label: NO-GO**

Scope: infer positive diagonal quotient loss merely because compact DNF
witnesses occur at their actual formula encodings after all are placed at one
length by a common growing outer double-NOT padding block.

Failure: ENC-019 shows that reserving `m` outer padding bits puts every witness
in the raw face `{1}^m x {0,1}^t`. LEMMA-044 uses those same raw coordinates as
fresh conjunctive circuit inputs away from the witness face. It preserves the
entire prescribed table on the face, has exact minimum size `K+m`, retains at
least `2m` tail classes per diagonal pair, and has loss at most `K-m`.
Canonical compact DNF evaluation has polynomial base size, so sufficiently
small fixed `c` permits `m/K -> infinity` at compatible lengths.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; explicit local
agreement on a codimension-`m` raw suffix face; unrestricted polynomial-size
DNF parser base and a fresh AND tail; fan-in-two AND/OR and fan-in-one NOT; no
randomness, advice, oracle, promise, distribution, or algebraic computation.
The no-go does not cover GATE-004U's dense near-boundary DNF encodings, which
do not share a growing outer fixed-coordinate block.

## NG-043 — padding-dense witnesses still admit a raw-coordinate fresh tail

**Label: NO-GO**

Scope: extend the LEMMA-044 counterexample to a witness family containing all
ENC-020 neutral placements by finding one or more raw outer padding
coordinates fixed across every encoding.

Failure: ENC-020 supplies, for each outer coordinate, one exact neutral
encoding with bit zero and another with bit one. LEMMA-045 therefore proves
that no nonempty conjunction of positive or negative raw-coordinate literals
is one on the entire family. The growing raw face required by LEMMA-044 has
codimension zero on the padding region.

Model: exact SAT-gamma neutral contexts and arbitrary conjunctions of raw
suffix-coordinate literals; unrestricted later ambient circuits; fan-in-two
AND and optional fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This is a no-go for the raw fresh-
input counterexample method, not a circuit lower bound. A non-coordinate
predicate recognizing the witness set remains possible, but LEMMA-037 gives
no additive minimum-cost identity for such a predicate.

## NG-044 — coordinate-dense neutral contexts force quotient loss

**Label: NO-GO**

Scope: infer positive polynomial diagonal quotient loss from exact SAT-gamma
agreement on common-inner-length compact DNF cores under every coordinate-
dense ENC-020 neutral context.

Failure: ENC-021 pairs the two halves of the outer context. Every ENC-020
zero lies in one block of length at most 16, so each distant clause
`z_i OR z_{i+P/2}` is one on every witness. LEMMA-046 proves the exact
identity `C(H AND W_P)=C(H)+P`. In its displayed minimum circuit the `P/2`
clause functions and `P` row-specific AND-prefix functions give at least
`3P/2` quotient classes, so every diagonal loss is at most `K-P/2`. The
canonical DNF base has `K=o(P)` for sufficiently small fixed context exponent
`c`, making the loss negative.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; common-inner-
length DNF cores and every ENC-020 outer placement; disjoint coordinate-pair
clauses; exact size `K+P`, unrestricted depth, fan-in-two AND/OR and fan-in-one
NOT; no randomness, advice, oracle, promise, distribution, or algebraic
computation. This falsifies ENC-020-only forcing, not full GATE-004U. The full
suffix set contains other padding forms and cores that need not satisfy the
paired clauses. The next syntax audit requires at least pairwise zero coverage
on any proposed large neutral-padding region.

Cycle 046 response: ENC-022 meets this defense up to four root-token pairs,
whose matching number is only two. LEMMA-047 therefore prevents this specific
no-go from extending to the enlarged one/two-block witness family. This
repair is not promoted to a loss theorem; higher-width and overlapping common
predicates remain unaudited.

## NG-045 — almost pairwise-zero contexts force quotient loss

**Label: NO-GO**

Scope: infer positive polynomial diagonal quotient loss from exact SAT-gamma
agreement on common-inner-length DNF cores under every one/two-block ENC-022
context.

Failure: ENC-023 partitions the outer coordinates into triples separated by
`P/3`. An ENC-022 context has only two blocks, each shorter than the triple
spacing, so every width-three OR clause is one on every witness. LEMMA-048
proves that `m` disjoint width-`w` clauses add exactly `wm` gates and expose at
least `(w+1)m` quotient classes. At width three and `m=P/3`, the counterexample
has exact size `K+P`, quotient at least `4P/3`, and loss at most `K-P/3<0` for
sufficiently small fixed context exponent.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; common-inner-
length compact DNF cores and every one/two-block ENC-022 placement; disjoint
width-three positive clauses; exact size and semantic quotient accounting;
unrestricted depth, fan-in-two AND/OR and fan-in-one NOT; no randomness,
advice, oracle, promise, distribution, or algebraic computation. This is a
no-go for ENC-022-only forcing, not full GATE-004U. The next defense requires
triple-zero coverage or broader syntax interactions, and any fixed-width
repair remains subject to the general LEMMA-048 audit.

## NG-046 — a bounded number of neutral blocks forces quotient loss

**Label: NO-GO**

Scope: infer positive diagonal quotient loss from exact SAT-gamma agreement on
common-inner-length DNF cores under a neutral-context family whose zero
supports use at most `b(P)` intervals of length at most `D(P)`.

Failure: ENC-024 and LEMMA-049 put
`m=floor(P/(b(P)+1))` coordinates into each of `m` disjoint distant groups of
width `b(P)+1`. When `m>=D(P)`, each block hits at most one coordinate in a
group, so every group clause is common. The exact extension has size
`K+(b+1)m`, quotient at least `(b+2)m`, and loss at most `K-m`. It is negative
whenever `m>K`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; arbitrary
sparse-block outer context families; common-inner-length canonical DNF base;
exact disjoint width-`b+1` positive clauses; unrestricted depth, fan-in-two
AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This closes every fixed-block-count
repair and every growing regime satisfying `m>=D` and `m>K`. It does not
cover dense block counts, long blocks, or full GATE-004U's broader syntax
interactions.

## NG-047 — dense finite neutral blocks force quotient loss

**Label: NO-GO**

Scope: infer positive diagonal loss from agreement on common-inner-length DNF
cores under arbitrary, even linear-count, concatenations of a fixed finite
neutral-block alphabet, or more generally under contexts with maximum zero
run `rho(P)`.

Failure: ENC-025 and LEMMA-050 partition the outer region into
`m=floor(P/(rho+1))` disjoint width-`rho+1` windows. Every window OR is common.
The exact extension has size `K+(rho+1)m`, quotient at least `(rho+2)m`, and
loss at most `K-m`, negative whenever `m>K`. The ten ENC-022 blocks have
`rho=7` under arbitrary concatenation, so dense block count still leaves a
linear tail.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; arbitrary
bounded-zero-run outer context families; common-inner-length canonical DNF
base; exact disjoint positive window clauses; unrestricted depth, fan-in-two
AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This does not cover long zero runs or
full GATE-004U's variable-core syntax. Escaping the method requires roughly
`rho(P)>=P/(K(P)+1)-1`, but that condition is not asserted sufficient.

## NG-048 — a sweeping long-zero block forces quotient loss

**Label: NO-GO**

Scope: infer positive diagonal loss from exact agreement on common-inner-
length DNF cores under every placement of one tunable long-zero ENC-026 block.

Failure: the length-`4rho` block destroys many bounded-window clauses but all
zeros remain in one interval. For `P>=8rho`, the half-separated coordinate
pairs cannot both lie in that interval. Their `floor(P/2)` disjoint width-two
clauses are common. LEMMA-046/049 give exact size `K+2m`, quotient at least
`3m`, and loss at most `K-m<0` when `m=floor(P/2)>K`.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; common-inner-
length canonical DNF base; every four-aligned single-long-block placement;
exact disjoint positive two-clauses; unrestricted depth, fan-in-two AND/OR and
fan-in-one NOT; no randomness, advice, oracle, promise, distribution, or
algebraic computation. Long runs remain necessary against NG-047, but must be
combined with sufficiently dense independent placements to escape NG-046.

## NG-049 — disjoint positive clauses falsify GATE-004V

**Label: NO-GO**

Scope: falsify balanced long-run product rigidity by finding `m>K` disjoint
positive clauses common to every slot-product witness and applying the exact
LEMMA-048 extension.

Failure: ENC-028/LEMMA-053 evaluate every clause on the all-long member. It
has exactly `6s` one bits, and disjoint clauses must hit distinct ones, so
`m<=6s`. With `s=floor((R-1)/8)` and the eligible base floor `K>=R-1`, one
has `m<=3(R-1)/4<=K`. The certified bound `K-m` cannot be negative.

Model: exact balanced product witnesses; arbitrary-width pairwise variable-
disjoint positive clauses; globally minimum non-uniform AND/OR/NOT circuits
only through the already proved LEMMA-048 identity; no randomness, advice,
oracle, promise, distribution, or algebraic computation. This no-go does not
prove actual loss nonnegative and does not cover signed, overlapping, or
non-clausal common predicates.

## NG-050 — signed clauses inherit a fixed additive NOT cost

**Label: NO-GO**

Scope: extend the exact LEMMA-048 positive-clause identity to signed clauses
by charging a fixed extra cost for each negated literal, independently of the
nonconstant base circuit.

Failure: LEMMA-054 proves exact sizes on two raw variables. Conjoining the
same fresh literal `NOT z` to base `x` increases size from zero to two, while
conjoining it to base `NOT x` increases size from one to two because
`NOT x AND NOT z=NOT(x OR z)`. Thus output polarity can share the NOT gate,
and base size plus signed clause data do not determine an additive cost.

Model: exact globally minimum non-uniform Boolean circuits; unrestricted
depth; fan-in-two AND/OR and fan-in-one NOT; raw inputs free; no randomness,
advice, oracle, promise, distribution, or algebraic computation. This closes
only naive signed-clause accounting. Complement-sensitive signed extensions,
overlap, nonclausal predicates, GATE-004V, and the terminal problem remain
open.

## NG-051 — complement-exposed negative unit tails defeat GATE-004V

**Label: NO-GO**

Scope: use an eligible base whose complement is exactly one gate cheaper and
attach common fresh negative unit literals. LEMMA-055 proves exact size
`K+m`, at least `2m+2` paired-row tail classes, and loss at most `K-m-2`.

Failure: LEMMA-052's balanced product is coordinate-dense. Every outer raw
coordinate is zero on one member and one on another, so neither polarity of
any unit literal is common. The candidate tail count is forced to `m=0`.

Model: exact balanced Boolean slot products; globally minimum non-uniform
AND/OR/NOT circuits; complement-exposed nonconstant base; unrestricted depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This excludes only unit signed tails.
Mixed width-at-least-two clauses and overlapping/nonclausal predicates remain
open.

## NG-052 — one essential restriction per implication certifies its displayed circuit

**Label: NO-GO**

Scope: prove the `K+3m` displayed circuit for `m` disjoint implication clauses
minimum by setting each negative variable to one, charging the generic one-
gate essential-variable deletion, and applying the exact fresh-conjunction
identity to the residual.

Failure: LEMMA-057 gives only `m` deleted gates plus residual size `K+m`, for
the lower bound `K+2m`. The displayed circuit costs `K+3m`; the shortfall is
exactly `m`, equal to its prospective quotient surplus because it exposes
`4m` tail classes. The certificate cannot establish minimality or preserve
those classes through global minimization.

Model: exact globally minimum non-uniform AND/OR/NOT circuits; disjoint fresh
mixed implication clauses; unrestricted depth; fan-in-two AND/OR and fan-in-
one NOT; no randomness, advice, oracle, promise, distribution, or algebraic
computation. This is only a no-go for the specified restriction certificate.
GATE-004W, GATE-004V, and the terminal problem remain open.

## NG-053 — support connectivity plus inversion complexity closes the implication direct sum

**Label: NO-GO**

Scope: certify the displayed `3m-1` size of the standalone conjunction of
`m` disjoint implications using essential-input connectivity for binary gates
and Markov's inversion-complexity theorem for NOT gates.

Failure: LEMMA-058 proves the complete combined bound
`2m-1+ceil(log_2(m+1))`. It is exact for `m=1,2`, but its gap from the
displayed upper bound is `m-ceil(log_2(m+1))`, linear asymptotically. Neither
measure is additive relative to the canonical base or controls semantic
quotient classes.

Model: exact non-uniform unrestricted circuits; standalone disjoint
implications; Boolean-lattice increasing chains; unrestricted depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This closes only the combined
support/NOT-count certificate, not the exact growing predicate size or
GATE-004W.

## NG-054 — the minimum-binary formula boundary closes the growing implication size

**Label: NO-GO**

Scope: strengthen NG-053 by proving that equality in the `2m-1` binary-gate
connectivity floor forces a formula, then apply formula inversion complexity
to obtain `m` NOT gates.

Failure: LEMMA-059 closes the displayed size only for `m<=4`. For `m>=5`, a
circuit with at least `2m` binary gates is outside the formula case and
Markov's general-circuit theorem requires only `ceil(log_2(m+1))` NOT gates.
The resulting gap from `3m-1` is `m-1-ceil(log_2(m+1))`, linear
asymptotically.

Model: exact non-uniform unrestricted circuits; equality-case output-cone
graph; formula and circuit inversion complexity; unrestricted depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This is a method no-go only; it does
not exhibit compression or refute the growing exact-size conjecture.

## NG-055 — signed-binary sparsity controls higher-width signed tails

**Label: NO-GO**

Scope: infer GATE-004X rigidity, or even absence of a linear disjoint common
signed-clause tail, from LEMMA-060's bound on common unit and signed-binary
families.

Failure: LEMMA-061 constructs one common signed width-three clause on every
aligned four-bit chunk. The product therefore has `rho*s=P/4` pairwise
variable-disjoint common triples while its signed-binary packing is still at
most `18s`. Binary sparsity and linear ternary packing coexist.

Model: exact enhanced SAT-gamma slot products; signed raw-coordinate clauses;
finite incidence and Cartesian-product localization; later globally minimum
non-uniform unrestricted AND/OR/NOT circuits; unrestricted depth; fan-in-two
AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This rejects only the inference from
signed-binary sparsity. LEMMA-062 does not yet convert the triples into a
minimum-circuit counterexample, so GATE-004X and P versus NP remain open.

## NG-056 — the clausewise signed-triple circuit is minimum

**Label: NO-GO**

Scope: prove the `K+5m` clausewise circuit minimum and transfer its `6m`
paired-row quotient classes to a GATE-004X counterexample.

Failure: LEMMA-064 factors every clause as `p OR NOT(u AND v)`. The resulting
circuit costs at most `K+4m`, strictly less than `K+5m` for every `m>=1`.
Thus the literalwise clause representation is never minimum. Its quotient
richness is implementation-specific and cannot be promoted by minimality.

Model: exact globally minimum non-uniform unrestricted AND/OR/NOT circuits;
pairwise-disjoint signed width-three clauses with one positive and two
negative literals; exact paired-row semantic quotients; unrestricted depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This closes only clausewise
minimality. Representation-independent quotient survival, GATE-004Y,
GATE-004X, and P versus NP remain open.

## NG-057 — the minimum-binary formula boundary closes the growing signed-triple tail

**Label: NO-GO**

Scope: combine essential-input connectivity, equality forcing a formula,
Morizumi formula inversion complexity, and Markov circuit inversion
complexity to prove the factorized `4m-1` standalone signed-triple circuit
minimum for growing `m`.

Failure: LEMMA-065 proves exact size for `m<=4`. Starting at `m=5`, a circuit
with at least `3m` binary gates escapes the formula case and needs only
`ceil(log_2(m+1))` NOT gates by this certificate. The resulting gap from the
factorized upper bound is `m-1-ceil(log_2(m+1))`, linear asymptotically.

Model: exact non-uniform unrestricted circuits; disjoint factorized signed
width-three predicates; Boolean-lattice inversion complexity and output-cone
connectivity; unrestricted depth; fan-in-two AND/OR and fan-in-one NOT; no
randomness, advice, oracle, promise, distribution, or algebraic computation.
This is a method no-go only. It proves neither a smaller circuit nor base
additivity, and GATE-004Z, GATE-004X, and P versus NP remain open.

## NG-058 — signed-triple standalone size is an independent route

**Label: NO-GO**

Scope: treat exact size or displayed minimality of the factorized signed-
triple tail as a structurally new way around the unresolved implication-tail
direct sum.

Failure: LEMMA-066 proves an exact identity over every disjoint nonconstant
base. Computing the pairwise AND inputs adds `m` gates to a minimum implication
circuit; restricting one input of each pair to one removes at least `m` gates
and recovers that implication function. The lifted circuit is minimum, and
the derived AND gates add exactly `m` distinct quotient classes. Therefore
the signed-triple displayed-minimality question is precisely the implication
question plus a settled additive layer.

Model: exact globally minimum non-uniform unrestricted circuits; disjoint
implication and signed width-three tails; functional substitution,
restrictions, and paired-row semantic quotients; unrestricted depth;
fan-in-two AND/OR and fan-in-one NOT; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This rejects only an independent-
route interpretation. GATE-004W/Z quotient survival, GATE-004X, and P versus
NP remain open.

## NG-059 — a fixed alphabet with one translated block suppresses width three

**Label: NO-GO**

Scope: add every aligned placement of every universally neutral block up to a
fixed length, one block per option, plus the sole tunable `A_rho`, and bound
all disjoint common signed width-three clauses by a constant per slot.

Failure: LEMMA-067 partitions a length-`4rho` slot into three distant regions
and obtains `floor(4rho/3)` disjoint triples. A bounded block can put zeros on
at most one coordinate of each triple and therefore misses all four patterns
with at least two zeros. The one exceptional long option supplies at most one
of them, leaving at least three common signed clauses per triple. The packing
is linear for every fixed alphabet bound.

Model: exact neutral SAT-gamma contexts; arbitrary fixed bounded-block
alphabet; one translated block per option and one arbitrary exceptional
option; signed width-three matching; later unrestricted non-uniform circuits;
no randomness, advice, oracle, promise, distribution, or algebraic
computation. This is a witness-geometry no-go. Two-block options, GATE-004AB,
GATE-004X, and P versus NP remain open.

## NG-060 — the ten ENC-022 blocks suffice for two-block width-three sparsity

**Label: NO-GO**

LEMMA-069 shows that their aligned three-bit alphabet omits `101` and `110`.
Two nonoverlapping blocks cannot jointly alter one aligned chunk, and the one
long option adds at most one missing pattern. Hence `rho` disjoint common
signed triples remain per slot. Identifier-10/12 enrichment repairs this
specific defect, but GATE-004AB and P versus NP remain open.

## NG-061 — width-three sparsity controls all disjoint signed tails

**Label: NO-GO**

LEMMA-072 gives `floor(rho)` distant disjoint common signed width-four clauses
per slot when options contain at most two bounded blocks plus `A_rho`.
Therefore the proved width-three hitting set cannot be extrapolated to higher
width. This is an incidence no-go only: the circuit cost of the width-four
tail, GATE-004AC, and P versus NP remain open.

## NG-062 — the identifier-68 alphabet lifts unchanged to width four

**Label: NO-GO**

LEMMA-073 certifies that three nonoverlapping identifier-1-through-68 blocks
cannot realize `1110` on offsets `{0,21,25,26}`. Disjoint translations leave
a linear common signed width-four packing after `A_rho` repairs at most two.
This closes only that fixed alphabet; richer GATE-004AD constructions and P
versus NP remain open.

## NG-063 — all standard neutral blocks through length 48 suffice at width four

**Label: NO-GO**

Scope: allow every block `01 T_j,10 F_j` with `1<=j<=1023`, choose up to
three nonoverlapping aligned blocks per ordinary option, and seek constant
signed-width-four packing per slot.

Failure: LEMMA-074's exact interval DP omits `1110` on offsets `{0,5,9,10}`
even for this complete alphabet. Twelve-spaced translations are disjoint, and
the six-one exceptional option repairs at most two, leaving `N/12-O(1)` common
signed clauses. This dominates every subset of the length-48 alphabet.

Model: exact three-block SAT-gamma neutral contexts; complete identifier range
1 through 1,023; one six-one long option; signed width-four matching;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, distribution, or algebraic computation. Identifiers of length at
least 52 repair individual failed types, so larger-alphabet GATE-004AD and P
versus NP remain open.

## NG-064 — the first length-68 repair set is quartet-universal

**Label: NO-GO**

Scope: use the first 86-identifier length-68 alphabet, selected to repair all
Cycle-070 counterquartets, and infer four-coordinate universality from those
repairs plus a 1,000-type random sample.

Failure: the audited `4*71^3` subdomain returns six residue-1 types, all omitting
zero mask 8: `(69,72,77,78)`, `(69,73,77,78)`, `(69,74,77,78)`,
`(69,75,77,78)`, `(69,76,81,82)`, and `(69,77,81,82)`. The sampling inference
is therefore false. This is not a structural length-68 obstruction: identifiers
`1044,1060,1092,1156,16452,16516` repair the six types. The completed alphabet
passes the same subdomain audit. LEMMA-104/105/106 later prove its corrected
all-quartet coverage; they do not validate the failed 86-identifier claim.

Model: exact three-block neutral contexts; fixed 86-identifier alphabet;
four-coordinate finite incidence; unrestricted later non-uniform circuits;
no randomness in the exhaustive result, advice, oracle, promise,
distribution, or algebraic computation. GATE-004AD is later restored to
`PROVED` for the completed alphabet; P versus NP remains open.

## NG-065 — width-four sparsity controls all disjoint signed tails

**Label: NO-GO**

LEMMA-076 partitions every sufficiently long slot into `floor(N/5)` distant
quintuples. Three bounded blocks can place zeros on at most three coordinates,
so all six patterns with four or five zeros are absent from ordinary options.
The one exceptional option supplies at most one, leaving at least five common
signed width-five clauses per quintuple and hence a linear disjoint packing.

Model: exact three-block slot options; one arbitrary exception; signed
width-five incidence and matching; later circuits fully non-uniform and
unrestricted; no randomness, advice, oracle, promise, distribution, or
algebraic computation. This rejects only extrapolation from the LEMMA-075
width-four hitting set. Tail cost and quotient survival, GATE-004AE, and P
versus NP remain open.

## NG-066 — the width-four alphabet lifts unchanged to width five

**Label: NO-GO**

LEMMA-077 certifies with two exact interval-DP implementations that four
nonoverlapping blocks from the 92-identifier LEMMA-075 alphabet cannot realize
`11110` on offsets `{0,4,7,9,10}`. Twelve-spaced translations are disjoint,
and the six-one long option can repair at most one because each occurrence
uses four one positions. A linear common signed width-five packing survives.

Model: exact four-block SAT-gamma neutral contexts; fixed 92-identifier
alphabet; one six-one long option; signed width-five matching; unrestricted
later non-uniform circuits; no randomness, advice, oracle, promise,
distribution, or algebraic computation. This closes only alphabet reuse;
richer GATE-004AF constructions and P versus NP remain open.

## NG-067 — repairing the first two quintet masks suffices

**Label: NO-GO**

Identifiers 1,089 and 1,098 realize the two masks missing from the LEMMA-077
representative without increasing the block bound. The resulting
94-identifier alphabet nevertheless has 1,787 failures in the exact
gap-at-most-20 audit. LEMMA-078 isolates mask 8 on offsets `{0,1,6,7,10}`;
twelve-spaced translations survive except for at most one repair by the
six-one long option.

Model: exact four-block SAT-gamma neutral contexts; fixed 94-identifier
alphabet; one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness in the exhaustive local audit, advice,
oracle, promise, distribution, or algebraic computation. This closes only the
two-identifier patch; GATE-004AF and P versus NP remain open.

## NG-068 — strength-five coverage of free identifier bits suffices

**Label: NO-GO**

LEMMA-079 constructs and exhaustively verifies a 318-row covering basis for
all five-column patterns on the fourteen free bits of a 15-bit identifier.
After adjoining it, the exact local quintet failure count drops from 1,787 to
497 but does not vanish. LEMMA-080 isolates mask 16 on offsets
`{0,1,10,15,16}`; the selected coordinates cross fixed syntax and gamma
boundaries, which the free-bit covering property does not constrain.

Model: deterministic exact covering array; four-block SAT-gamma neutral
contexts; fixed 412-identifier alphabet; one long option; signed width-five
matching; unrestricted later non-uniform circuits; no randomness, advice,
oracle, promise, distribution, or algebraic computation. The next construction
must cover complete-block phases. GATE-004AF and P versus NP remain open.

## NG-069 — some length-at-most-68 identifier enrichment repairs width five

**Label: NO-GO**

LEMMA-081 proves that 2,066 representatives cover every five-coordinate
behavior of the literal complete identifier range 1 through 32,767. LEMMA-082
then checks that range directly and through the projection reduction: mask 16
is absent on offsets `{0,1,10,15,16}` under four nonoverlapping blocks.
Twenty-spaced translations leave a linear common signed width-five packing.

Model: complete standard neutral alphabet of block length at most 68;
four-block options; one six-one long option; signed width-five matching;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, distribution, or algebraic computation. Any repair must use block
length at least 72. GATE-004AF and P versus NP remain open.

## NG-070 — some length-at-most-72 identifier enrichment repairs width five

**Label: NO-GO**

LEMMA-083 audits the literal identifier range 1 through 65,535 and an
independent 2,437-row projection-complete basis. Both exact DPs omit mask 16
on offsets `{0,1,10,15,16}` with four blocks. Twenty-spaced translations leave
a linear common signed width-five packing after at most one long-option repair.

Model: complete standard neutral alphabet of block length at most 72;
four-block options; one six-one long option; signed width-five matching;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, distribution, or algebraic computation. Identifier 98,370 repairs
the representative at length 76, so the full gate remains open. P versus NP
is unaffected.

## NG-071 — the first length-76 repair suffices globally

**Label: NO-GO**

Identifier 98,370 repairs the LEMMA-083 representative but the exact
gap-at-most-20 audit retains 494 failures. LEMMA-085 isolates mask 16 on
offsets `{0,2,10,15,16}`. Twenty-spaced translations leave a linear common
signed width-five packing after at most one `A_rho` repair.

Model: fixed 413-identifier alphabet with one length-76 addition; four-block
options; one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness in the exact audit, advice, oracle,
promise, distribution, or algebraic computation. The projection-complete full
length-76 alphabet remains open under LEMMA-086. P versus NP is unaffected.

## NG-072 — some length-at-most-76 identifier enrichment repairs width five

**Label: NO-GO**

LEMMA-087 gives an exact symbolic oracle for the complete identifier alphabet.
The bound-76 local audit finds 195 failures. LEMMA-088 confirms with both the
symbolic oracle and literal enumeration that mask 16 is absent on offsets
`{0,4,12,17,18}` under four blocks. Twenty-spaced translations leave a linear
common signed width-five packing.

Model: every standard neutral block of length at most 76; four-block options;
one six-one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness, advice, oracle, promise, distribution,
or algebraic computation. Any repair must use length at least 80. GATE-004AF
and P versus NP remain open.

## NG-073 — some length-at-most-80 identifier enrichment repairs width five

**Label: NO-GO**

LEMMA-089 audits the literal identifier range 1 through 262,143 and the exact
LEMMA-087 symbolic oracle. Both omit only mask 16 on offsets
`{0,4,12,17,18}` under four nonoverlapping aligned blocks. Twenty-spaced
translations leave a linear common signed width-five packing after at most one
long-option repair.

Model: every standard neutral block of length at most 80; four-block options;
one six-one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness, advice, oracle, promise, distribution,
or algebraic computation. Identifier 278,594 repairs this representative at
length 84, so the full gate remains open. P versus NP is unaffected.

## NG-074 — some length-at-most-84 identifier enrichment repairs width five

**Label: NO-GO**

The complete symbolic gap-at-most-20 audit finds 122 failures across 640,000
types. LEMMA-091 checks one representative independently by literal
enumeration of identifiers 1 through 524,287: mask 8 is absent on offsets
`{0,8,16,19,20}` under four blocks. Twenty-four-spaced translations leave a
linear common signed width-five packing.

Model: every standard neutral block of length at most 84; four-block options;
one six-one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness, advice, oracle, promise, distribution,
or algebraic computation. Any repair must use length at least 88. GATE-004AF
and P versus NP remain open.

## NG-075 — some length-at-most-88 identifier enrichment repairs width five

**Label: NO-GO**

The complete symbolic local audit finds 111 failures across 640,000 types.
LEMMA-093 independently checks one by literal enumeration of all 1,048,575
identifiers: mask 16 is absent on offsets `{0,8,16,21,22}`. Twenty-four-spaced
translations leave a linear common signed width-five packing.

Model: every standard neutral block of length at most 88; four-block options;
one six-one long option; signed width-five matching; unrestricted later
non-uniform circuits; no randomness, advice, oracle, promise, distribution,
or algebraic computation. Longer blocks remain open. P versus NP is unaffected.

## NG-076 — some length-at-most-96 identifier enrichment repairs width five

**Label: NO-GO**

The exact LEMMA-087 symbolic oracle shows that the LEMMA-093 mask-16
obstruction survives the complete length-92 and length-96 alphabets. LEMMA-094
translates offsets `{0,8,16,21,22}` by twenty-four to retain a linear common
signed width-five packing.

Model: every standard neutral block of length at most 96, equivalently every
identifier through 4,194,303; four-block options; one six-one long option;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, distribution, or algebraic computation. Identifier 4,210,754 repairs
the representative at length 100, so the full gate remains open. P versus NP
is unaffected.

## NG-077 — some length-at-most-100 identifier enrichment repairs width five

**Label: NO-GO**

The exact local audit finds 46 failures across 640,000 types. LEMMA-096 checks
one representative using both the symbolic oracle and an independently
derived 851-identifier basis that has zero selected-projection coverage
failures. Mask 8 is absent on offsets `{0,12,20,23,24}`. Twenty-eight-spaced
translations leave a linear common signed width-five packing.

Model: every standard neutral block of length at most 100, equivalently every
identifier through 8,388,607; four-block options; one six-one long option;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, average-case, distributional, or algebraic computation. Identifier
8,390,664 repairs the representative at length 104, so the full gate remains
open. P versus NP is unaffected.

## NG-078 — some length-at-most-104 identifier enrichment repairs width five

**Label: NO-GO**

The exact local audit finds 44 failures across 640,000 types. LEMMA-098 checks
one representative with the symbolic oracle and a 985-identifier basis having
zero selected-projection failures. Mask 16 is absent on offsets
`{0,12,20,25,26}`. Twenty-eight-spaced translations leave a linear common
signed width-five packing.

Model: every standard neutral block of length at most 104; four-block options;
one six-one long option; unrestricted later non-uniform circuits; no
randomness, advice, oracle, promise, average-case, distributional, or algebraic
computation. Longer blocks remain open. P versus NP is unaffected.

## NG-079 — some length-at-most-112 identifier enrichment repairs width five

**Label: NO-GO**

The exact symbolic oracle retains the LEMMA-098 mask-16 obstruction at lengths
108 and 112. At length 112 an independent 1,232-identifier projection-complete
basis and literal DP agree. Twenty-eight-spaced translations retain the linear
common signed width-five packing.

Model: every standard neutral block of length at most 112, equivalently every
identifier through 67,108,863; four-block options; one six-one long option;
unrestricted later non-uniform circuits; no randomness, advice, oracle,
promise, average-case, distributional, or algebraic computation. Identifier
67,125,314 repairs the representative at length 116. P versus NP is unaffected.

## NG-080 — one-block-length gap truncation can destroy nonoverlap

**Label: NO-GO**

The finite-certificate route used for LEMMA-075 truncated every gap at least
the block bound `B` to `{B,...,B+3}`. LEMMA-101 gives a four-aligned `B=8`
counterexample: mask 3 is reachable on coordinates `(8,23)` by adjacent
length-eight blocks but is unreachable after reducing the congruent gap from
15 to 11 because the two forced placements overlap.

LEMMA-102 proves the safe geometry-only threshold `2B`; LEMMA-103 then derives
the smaller exact 9,515,749-type phase domain for the literal alphabet. Thus
the prior `4*71^3` LEMMA-075 audit covers a strict subdomain. LEMMA-075 and
GATE-004AD are `EXPLORATORY` pending that extension. The corrected LEMMA-071
domain is small enough to audit and passes all 22,500 types. LEMMA-104/105/106
later bypass the large corrected quartet domain and restore GATE-004AD without
reviving the unsafe reduction. No circuit or terminal claim is affected
positively; P versus NP remains open.

## NG-081 — essential restrictions certify the one-negative width-five tail

**Label: NO-GO**

Scope: use the LEMMA-108 four-positive/one-negative disjoint width-five tail,
restrict its `m` negative variables to one, and combine earliest-dependent-
gate elimination with LEMMA-048's exact positive-clause cost to prove the
minimality-or-quotient alternative in GATE-004AG.

Failure: LEMMA-107 gives only `K+5m<=C(F)<=K+6m`. The restriction lower bound
is short by exactly `m` gates, which is also the entire quotient surplus
needed to derive displayed loss at most `K-m`. Treating the local clause
circuits as additively mandatory would silently assume the desired direct-sum
property for unrestricted DAGs.

Model: minimum unrestricted non-uniform Boolean circuits; disjoint signed
width-five clauses with four positive and one negative literal; AND/OR fan-in
two and NOT fan-in one; exact worst-case quantifiers; no randomness, advice,
oracle, promise, distribution, or algebraic computation. The restriction-only
method is closed, while GATE-004AG, GATE-004AE, and P versus NP remain open.

## NG-082 — binary connectivity plus inversion complexity closes GATE-004AG

**Label: NO-GO**

Scope: prove the standalone four-positive/one-negative tail circuit minimum by
combining essential-input connectivity, the formula forced at minimum binary
gate count, and Markov/Morizumi inversion complexity.

Failure: LEMMA-109 computes `d(W_m)=m` and proves
`min(6m-1,5m+ceil(log_2(m+1)))<=C(W_m)<=6m-1`. Equality follows only for
`m<=4`. For every `m>=5`, the certificate deficit is
`m-1-ceil(log_2(m+1))`, which is linear in the asymptotic family. One extra
binary gate leaves the formula regime and permits only the logarithmic
circuit inversion bound; no representation-independent quotient count is
obtained.

Model: minimum unrestricted non-uniform Boolean circuits; AND/OR fan-in two,
NOT fan-in one; Boolean-lattice chains and graph connectivity; exact
worst-case quantifiers; no randomness, advice, oracle, promise, distribution,
or algebraic circuit model. This combined method is closed, while
GATE-004AG, GATE-004AE, and P versus NP remain open.

## NG-083 — one-cycle formula unfolding closes GATE-004AG

**Label: NO-GO**

Scope: analyze the first non-formula stratum, with exactly `5m` binary gates,
by unfolding its single reconvergence into a formula and applying formula
inversion complexity.

Failure: LEMMA-110 proves the output multigraph is unicyclic, so every gate is
copied at most twice in the unfolding. This yields the genuine linear bound
`N>=ceil(m/2)`, strengthened by Markov to
`N>=max(ceil(m/2),ceil(log_2(m+1)))`. The resulting total lower bound remains
short of `6m-1` by
`m-1-max(ceil(m/2),ceil(log_2(m+1)))`, positive from `m=5` and asymptotic to
`m/2`. The unfolding cannot identify two copied NOTs as a single charge
without an additional structural theorem.

Model: pruned minimum unrestricted non-uniform Boolean circuit output cones;
exactly `5m` binary gates; AND/OR fan-in two and NOT fan-in one; undirected
multigraph cycle rank and Boolean-lattice inversion; exact worst-case
quantifiers; no randomness, advice, oracle, promise, distribution, or
algebraic circuit model. The method is closed, while GATE-004AG, GATE-004AE,
and P versus NP remain open.

## NG-084 — optimizing cycle-rank unfolding proves GATE-004AG

**Label: NO-GO**

Scope: extend one-cycle unfolding to arbitrary output-cone cycle rank `t`,
charge all extra binary gates, combine with Markov, and optimize over every
possible binary-gate count.

Failure: LEMMA-111 proves that a rank-`t` cone has at most `2^t` paths from any
gate to the output. The strongest direct unfolding certificate is therefore
`N>=max(ceil(m/2^t),ceil(log_2(m+1)))`. After charging the `t` extra binary
gates and minimizing, the total lower bound is `5m-1+g(m)`, where

`g(m)=min_t[t+max(ceil(m/2^t),ceil(log_2(m+1)))] = Theta(log m)`.

The displayed circuit needs surplus `m`, so the remaining deficit is
`m-g(m)=m-Theta(log m)`, positive from `m=5`. The optimization covers every
cycle rank; repeating the same unfolding argument cannot close the gap.

Model: every pruned minimum unrestricted non-uniform Boolean circuit output
cone; arbitrary binary-gate count; AND/OR fan-in two, NOT fan-in one; binary
cycle spaces over `F_2` and Boolean-lattice inversion; exact worst-case
quantifiers; no randomness, advice, oracle, promise, distribution, or
algebraic circuit model. The method is closed, while GATE-004AG, GATE-004AE,
and P versus NP remain open.

## NG-085 — independent canonical cofactors prove the binary/NOT tradeoff

**Label: NO-GO**

Scope: fully assign the positive variables of the fixed-sign tail, lower-bound
the resulting negative-literal residuals exactly, and aggregate those bounds
to prove GATE-004AH.

Failure: LEMMA-112 gives residual size exactly `|S|`. The maximum over all
canonical cofactors is only `m` and the average is `m/2`, versus parent target
`6m-1`. Summing the `2^m` residual complexities is invalid: the restrictions
are mutually exclusive, and one parent gate may survive or normalize into
classes under many assignments. Distinct residual functions do not provide
an additive gate charge without a multi-cofactor survival theorem.

Model: every unrestricted non-uniform AND/OR/NOT parent circuit; all canonical
full assignments of positive tail variables; exact residual circuit size;
worst-case and uniform average over subsets; no randomness, advice, oracle,
promise, distribution, or algebraic model. Independent cofactor charging is
closed. GATE-004AH was later proved by dependency Hall; GATE-004AG/AE and P
versus NP remain open.

## NG-086 — output cofactor transitions yield distinct internal charges

**Label: NO-GO**

Scope: count every adjacent pair of canonical positive restrictions on which
the output residual changes and use those transitions to inject clause
indices into NOT gates or independent cycle coordinates.

Failure: LEMMA-113 gives `2^m` distinct output cofactors and
`m*2^(m-1)` changing cube edges, but all belong to the cofactor profile of
one fixed output node. Therefore raw transition count has no additive
relation to parent gate count. Any division by a supposed per-gate edge bound
is invalid because the output itself witnesses every edge. A valid route must
define internal first-divergence or survival witnesses and prove bounded reuse
across clause indices.

Model: every unrestricted non-uniform AND/OR/NOT parent circuit; canonical
positive restriction cube; exact output cofactor profiles; unrestricted
depth; AND/OR fan-in two and NOT fan-in one; no randomness, advice, oracle,
promise, distribution, or algebraic circuit model. Raw output-transition
counting is closed. GATE-004AI/AH were later proved by dependency Hall;
GATE-004AG/AE and P versus NP remain open.

## NG-087 — first cofactor-difference birth nodes are NOT gates

**Label: NO-GO**

Scope: for each clause index, find the first circuit node where the XOR of the
`alpha_empty` and `alpha_{ {i} }` cofactor functions becomes dependent on
`u_i`, then charge that node directly as a NOT resource.

Failure: LEMMA-114 proves that complementing both cofactor functions preserves
their XOR exactly. A NOT gate therefore cannot be the first node where the
difference acquires `u_i`-dependence; every first birth node is binary. The
zero-length birth-to-NOT trace is categorically unavailable. A valid proof
must trace to a nonlocal NOT or independent reconvergence and prove that the
resource cannot be reused across clause indices.

Model: every unrestricted non-uniform AND/OR/NOT circuit for the fixed-sign
tail; paired canonical cofactor functions at every node; unrestricted depth;
AND/OR fan-in two and NOT fan-in one; no randomness, advice, oracle, promise,
distribution, or algebraic circuit model. Direct birth-to-NOT charging is
closed, while GATE-004AJ/AI/AH/AG/AE and P versus NP remain open.

## NG-088 — sensitivity semantics alone gives Hall expansion

**Label: NO-GO**

Scope: define each clause index's resources as the NOT gates and non-tree
edges whose values or endpoints change on its canonical witness pair, then
prove Hall expansion without using the low-N restriction.

Failure: the explicit formula
`NOT OR_i (u_i AND AND_j NOT v_{i,j})` has `B=5m-1`, `t=0`, and `N=4m+1`.
For witness `i`, the only changing NOT is the final shared NOT; all local
`NOT v_{i,j}` gates remain fixed. Hence every resource neighborhood is the
same singleton, and every index subset of size at least two violates Hall.
The example is outside the unresolved range, so it does not refute
GATE-004AK; it proves that the quantitative condition `N<=m-1` must enter any
successful expansion proof.

Model: uniform explicit fan-out-one De Morgan formulas; assignment-sensitive
subgraphs; `B=5m-1`, `N=4m+1`, `t=0`; unrestricted depth; AND/OR fan-in two
and NOT fan-in one; no randomness, advice, oracle, promise, distribution, or
algebraic circuit model. Range-free sensitive Hall is closed, while the low-N
GATE-004AK and GATE-004AJ/AI/AH/AG/AE remain open.

## NG-089 — generic residual inversion proves quintet dependency Hall

**Label: NO-GO**

Scope: restrict the parent circuit to any five selected clause blocks, bound
its residual NOT count plus cycle rank by the union of their dependency-cone
resources, and apply only LEMMA-111.

Failure: the exact generic optimization is
`g(5)=min_c[c+max(ceil(5/2^c),ceil(log2(6)))]=4`, attained at `c=1` with
the permitted lower bound `q=3`. Hall requires union size five. Thus the
restriction/unfolding certificate is short by exactly one resource at the
first open subset size. This does not exhibit a deficient quintet; it proves
that total cycle rank and inversion complexity alone cannot exclude one.

Model: every unrestricted non-uniform parent circuit; arbitrary five-block
restriction; dependency-cone NOT and non-tree-edge resources; unrestricted
depth; AND/OR fan-in two and NOT fan-in one; binary cycle spaces over `F_2`;
no randomness, advice, oracle, promise, distribution, or algebraic circuit
model. LEMMA-111-only quintet Hall is closed, while function-specific
GATE-004AL/AI/AH were later proved by the general rank theorem; the sensitive
GATE-004AK, optional GATE-004AJ, and GATE-004AG/AE remain open.

## NG-090 — unfolded NOT-occurrence count excludes the deficient quintet

**Label: NO-GO**

Scope: use the exact `c=1,q=3` obstruction from LEMMA-117, unfold its single
cycle, and compare the number of formula NOT occurrences with inversion
complexity `d(W_5)=5`.

Failure: if `k` of the three NOT gates have two directed paths to the output,
unfolding produces exactly `3+k` NOT occurrences. Formula inversion forces
only `3+k>=5`, hence `k>=2`. Both `k=2` and `k=3` remain numerically
compatible, producing five or six occurrences. The bound reaches equality
but supplies no contradiction or clause-indexed allocation constraint.

Model: every pruned non-uniform unicyclic circuit for fixed `W_5` with
exactly 25 binary gates and three NOT gates; unrestricted depth; AND/OR fan-in
two and NOT fan-in one; directed path multiplicity, formula unfolding, and
Boolean-lattice inversion; no randomness, advice, oracle, promise,
distribution, or algebraic circuit model. Occurrence counting is closed,
while GATE-004AM was later proved by a different factorization argument;
GATE-004AL/AI/AH were later proved by the general rank theorem; the sensitive
and base-tail gates remain open.

## NG-091 — total path multiplicity excludes the deficient sextet

**Label: NO-GO**

Scope: unfold the exact bicyclic three-NOT residual forced by LEMMA-124 and
compare only the total number of resulting NOT occurrences with formula
inversion complexity `d(W_6)=6`.

Failure: cycle rank two gives each NOT gate between one and four directed
paths to the output. The formula lower bound requires only
`r_1+r_2+r_3>=6`, compatible with patterns including `(2,2,2)` and
`(1,1,4)`. Thus total multiplicity neither contradicts the stratum nor
distinguishes the two-cycle block-cut topologies. Interface dimension and
clause cofactor incidence must enter.

Model: every pruned non-uniform candidate for fixed `W_6` with 31 binary
gates, three NOT gates, and cycle rank two; unrestricted depth; AND/OR fan-in
two and NOT fan-in one; formula unfolding and Boolean-lattice inversion; no
randomness, advice, oracle, promise, distribution, or algebraic circuit
model. Path-counting alone is closed. GATE-004AN was later proved by
core/orientation analysis; GATE-004AL beyond size eight and
GATE-004AK/AJ/AI/AH/AG/AE remain open.

## NG-092 — one-bit articulation factorization excludes the theta core

**Label: NO-GO**

Scope: repeat LEMMA-126 by removing one cut vertex, factor the upstream
variables through one bit, and apply the one-bit cofactor dichotomy to the
remaining theta-core candidate.

Failure: the suppressed theta kernel has two branch vertices joined by three
internally disjoint paths. Removing either branch vertex leaves the core
connected, so neither is a cycle-separating articulation. Declaring one to be
a one-bit interface without proving that all relevant variable-output paths
pass through it would discard theta branches and invalidate the factorization.

Model: every pruned non-uniform theta-core candidate for fixed `W_6` with 31
binary gates and three NOT gates; unrestricted depth; AND/OR fan-in two and
NOT fan-in one; undirected vertex connectivity and Boolean cofactors; no
randomness, advice, oracle, promise, distribution, or algebraic circuit
model. Articulation-only reuse is closed, while GATE-004AO/AN were later
proved by orientation analysis; GATE-004AL beyond size eight and the larger
gates remain open.

## NG-093 — collapse the two theta splits to one intermediary bit

**Label: NO-GO**

Scope: after excluding the ternary-source orientation, choose one of the two
remaining binary split vertices as a common bit and apply LEMMA-121 exactly as
in the one-source proof.

Failure: the split budget permits two distinct source splits, whose attached
input trees compute separate bits, or a source split followed by a non-source
split whose value also depends on newly attached inputs. In neither topology
has every relevant upstream variable been proved to reach the output through
one common Boolean node. Assuming such a factorization would erase the second
split rather than analyze it.

Model: every pruned non-uniform two-binary-split theta candidate for fixed
`W_6` with 31 binary gates and three NOT gates; unrestricted depth; AND/OR
fan-in two and NOT fan-in one; directed split topology and Boolean cofactors;
no randomness, advice, oracle, promise, distribution, or algebraic circuit
model. Single-bit collapse is closed, while GATE-004AP/AO/AN were later
proved by separate parallel/nested analysis; GATE-004AL beyond size eight and
the larger gates remain open.

## NG-094 — treat the nested theta state as an independent second bit

**Label: NO-GO**

Scope: reuse LEMMA-130 by writing the two split values as independent
functions `z_1(X_1)` and `z_2(X_2)`, then apply the one-bit cofactor dichotomy
to each group separately.

Failure: in the nested orientation the later split lies downstream of the
first and has the form `z_2=H(z_1,X_2)`. It may therefore carry information
about `X_1`, and its NOT gates have different unfolding multiplicities from
those in the first source tree. Treating `z_2` as independent of `X_1` assumes
both the variable partition and the NOT allocation that must be proved.

Model: every pruned non-uniform nested theta candidate for fixed `W_6` with
31 binary gates and three NOT gates; unrestricted depth; AND/OR fan-in two
and NOT fan-in one; sequential Boolean interfaces and directed path regions;
no randomness, advice, oracle, promise, distribution, or algebraic circuit
model. Independent-two-bit reuse is closed, while sequential GATE-004AQ and
GATE-004AP/AO/AN were later proved by first-source restriction; GATE-004AL
beyond size eight and GATE-004AK/AJ/AI/AH/AG/AE remain open.

## NG-095 — total path multiplicity for the tricyclic septet stratum

**Label: NO-GO**

Scope: unfold a fixed `W_7` circuit with cycle rank three and exactly three
NOT gates, then combine the generic at-most-eight path multiplicity per gate
with the seven-NOT formula inversion lower bound.

Failure: the resulting constraints are only `1<=r_j<=8` and
`r_1+r_2+r_3>=7`. Compatible integer patterns such as `(1,1,5)` and
`(2,2,3)` remain. The inequalities do not encode which cycles share a source,
separator, or NOT gate, so they cannot exclude the exact residual stratum.

Model: every pruned non-uniform candidate for fixed `W_7` with 37 binary
gates, three NOT gates, and cycle rank three; unrestricted depth; AND/OR
fan-in two and NOT fan-in one; formula unfolding and Boolean-lattice
inversion; no randomness, advice, oracle, promise, distribution, or algebraic
circuit model. Path multiplicity alone is closed. GATE-004AR was later proved
by the structural rank-three reduction LEMMA-135 and later fully by
LEMMA-139/141; the base-tail and larger SAT gates remain open.

## NG-096 — total path multiplicity for the tetracyclic nonet stratum

**Label: NO-GO**

Scope: unfold a fixed `W_9` circuit with cycle rank four and exactly four NOT
gates, then combine the generic at-most-sixteen path multiplicity per gate
with the nine-NOT formula inversion lower bound.

Failure: the constraints `1<=r_j<=16` and `sum_j r_j>=9` admit patterns such
as `(1,1,1,6)` and `(2,2,2,3)`. They contain no information about rank-four
blocks, source deletion, or separators and therefore do not exclude the exact
residual stratum.

Model: every pruned non-uniform candidate for fixed `W_9` with 48 binary
gates, four NOT gates, and cycle rank four; unrestricted depth; AND/OR fan-in
two and NOT fan-in one; formula unfolding and Boolean-lattice inversion; no
randomness, advice, oracle, promise, distribution, or algebraic circuit
model. Path multiplicity alone is closed. GATE-004AS and full dependency Hall
were later proved by LEMMA-139/141; base-tail GATE-004AG remains open.

## NG-097 — promote exact standalone tail size to base-tail additivity

**Label: NO-GO**

Scope: use the exact theorem `C(W_m)=6m-1` as if it implied an additive lower
bound for `C(H AND W_m)` or forced the displayed tail's diagonal semantic
classes to survive in every minimum circuit.

Failure: unrestricted circuits may share gates across base and tail variables.
Restricting `H` to a satisfying assignment recovers the standalone lower but
does not charge computation on other base assignments. Circuit size alone
also says nothing about which semantic quotient classes occur in a different
minimum representation. The proposed promotion therefore assumes precisely
the direct-sum or quotient-survival statement required by GATE-004AG.

Model: minimum unrestricted non-uniform circuits for the canonical base `H`
conjoined with `m` disjoint four-positive/one-negative clauses; unrestricted
depth and fanout; AND/OR fan-in two and NOT fan-in one; no randomness, advice,
oracle, promise, distribution, or algebraic circuit model. The standalone
promotion is closed; GATE-004AG/AE and every SAT/terminal bridge remain open.

## NG-098 — infer a pure-base bottleneck from disjoint supports alone

**Label: NO-GO**

Scope: from freshness and disjointness of the base variables `X` and tail
variables `Y`, assert that some minimum circuit for `H(X) AND W_m(Y)` has one
pure-base gate through which every essential base-to-output path passes.

Failure: unrestricted binary gates may mix `X` and `Y` before the output,
fan out into several mixed regions, and reconverge. Disjoint primary supports
do not imply a directed one-vertex separator, and pruning supplies no
size-nonincreasing uncrossing transformation. Assuming the separator invokes
the conclusion of GATE-004AT.

Model: minimum unrestricted non-uniform base-tail circuit DAGs; disjoint
primary input supports; unrestricted depth and fanout; AND/OR fan-in two and
NOT fan-in one; no randomness, advice, oracle, promise, distribution, or
algebraic circuit model. Support-only separation is closed; canonical-row or
uncrossing GATE-004AT and GATE-004AG/AE remain open.

## NG-099 — promote near-minimum parent size to diagonal quotient stability

**Label: NO-GO**

Scope: use LEMMA-144's canonical size deficit `Delta=o(m)` as if it directly
bounded the number of missing active semantic classes in the two-row diagonal
quotient.

Failure: globally distinct gate functions may restrict to the same Boolean
function on a selected row, and globally essential gates may become constant
or inactive on both rows. Neither collapse reduces the unrestricted parent
size, so `Delta` alone does not count row-quotient collisions. A separate
charge to canonical suffix dependence or to an explicit slack resource is
required.

Model: globally minimum unrestricted non-uniform canonical base-tail circuits
and their two designated row restrictions; unrestricted depth and fanout;
AND/OR fan-in two and NOT fan-in one; no randomness, advice, oracle, promise,
distribution, or algebraic circuit model. Size-only promotion is closed;
GATE-004AU/AT/AG/AE remain open.

## NG-100 — add the two canonical row-size lower bounds

**Label: NO-GO**

Scope: apply LEMMA-145 separately to the two canonical row residuals and add
their circuit-complexity lower bounds as if the corresponding quotient class
sets were disjoint.

Failure: the quotient is a union, so the class-set intersection must be
subtracted. A size-`K+6m` architecture may compute `W_m` first and conjoin it
with `H` only at the output; all `6m-1` tail-gate functions are then shared
between the two row restrictions. The construction does not establish
minimum size when `Delta>0`, but it proves that separate row sizes contain no
intersection bound.

Model: unrestricted non-uniform base-tail circuits under two canonical row
restrictions; unrestricted depth and fanout; AND/OR fan-in two and NOT fan-in
one; finite semantic class unions; no randomness, advice, oracle, promise,
distribution, or algebraic circuit model. Separate-row addition is closed;
GATE-004AV/AU/AT/AG/AE remain open.

## NG-101 — exact derived OR prefixes close width-five quotient stability

**Label: NO-GO**

Scope: substitute a three-gate four-input OR chain for every implication input
`t_i`, use the exact size identity of LEMMA-146, and count the derived gates
as automatically new diagonal quotient classes.

Failure: only the two proper OR prefixes per block are guaranteed not to be
inherited row cofactors. The full OR `P_i` can collide with an inherited gate
whose selected-row cofactor is raw `t_i`, losing up to `m` classes. Separately,
the implication quotient baseline is only `3m`, another `m` below its target.
The unconditional combination gives `5m`, not `7m-o(m)`.

Model: exact functional substitution into minimum unrestricted non-uniform
implication circuits and two-row semantic quotients; unrestricted depth and
fanout; AND/OR fan-in two and NOT fan-in one; no randomness, advice, oracle,
promise, distribution, or algebraic circuit model. Prefix-only transfer is
closed; GATE-004AW/AV/AU/AT/AG/AE remain open.

## NG-102 — bound raw-input collisions from two cofactor tables

**Label: NO-GO**

Scope: infer `b=o(m)` from the facts that a minimum parent has no globally raw
input gate and that only two designated base-row cofactors are observed.

Failure: choose one nonzero base predicate `R` that vanishes on both rows.
The `m` globally non-raw functions `g_i=t_i OR R` all restrict to raw `t_i`
on both rows and cost only one shared circuit for `R` plus `m` OR gates. Thus
bilateral cofactor equality supplies neither a collision bound nor automatic
cross-row quotient surplus. LEMMA-147 proves the witness exactly.

Model: unrestricted Boolean parent-gate functions under two fixed base
restrictions; fully non-uniform finite witness; shared `C(R)` plus `m` binary
gates; unrestricted depth and fanout; AND/OR fan-in two and NOT fan-in one;
no randomness, advice, oracle, promise, distribution, or algebraic model.
Two-rows-only inference is closed; GATE-004AX/AW/AV/AU/AT/AG/AE remain open.

## NG-103 — normalize every raw cofactor to an exposed common OR mask

**Label: NO-GO**

Scope: apply LEMMA-148 to every collision by treating a gate with selected-row
cofactor `t_i` as an exposed gate `t_i OR R(X)`, with masks shared across
indices and only clause-local uses.

Failure: if `S(X)` vanishes on both selected rows, `t_i XOR S` has cofactor
`t_i` on both while being neither `t_i OR R(X)` nor `t_i AND R(X)` for any
base-only `R`. It has a constant-size AND/OR/NOT implementation. Moreover,
cofactor semantics say nothing about fanout or downstream mixing. Thus exact
mask form, mask commonality, and exposed use are all additional structural
premises. LEMMA-148's factorization is sound only after they are established.

Model: minimum unrestricted implication circuits audited through an exposed
common-mask submodule; fully non-uniform finite witness; unrestricted depth
and fanout; AND/OR fan-in two and NOT fan-in one; no randomness, advice,
oracle, promise, distribution, or algebraic model. Common-mask-only
normalization is closed; GATE-004AX/AW/AV/AU/AT/AG/AE remain open.

## NG-104 — promote GATE-004AX to every pair of nonconstant row residuals

**Label: NO-GO**

Scope: replace the canonical row geometry in GATE-004AX by the assertion that
both selected residual base functions are merely nonconstant.

Failure: take `H(a,z)=z`, use rows `a=0,1`, and conjoin the implication tail.
Both row residuals are the nonconstant input `z`, while LEMMA-142 gives exact
size `C(z AND W_m)=3m` and `K=Delta=0`. The output is independent of `a`, so
LEMMA-149 makes every gate function of every minimum circuit independent of
`a`. LEMMA-150 then gives `Q<=3m`, hence `Q-b<4m`, falsifying the generalized
target for every `m>=1`.

Model: minimum unrestricted non-uniform circuits for a raw enable input and
the implication tail; two rows of an inessential selector; exact size `3m`;
unrestricted depth and fanout; AND/OR fan-in two and NOT fan-in one; no
randomness, advice, oracle, promise, distribution, or algebraic model.
Arbitrary-base promotion is closed; canonical GATE-004AY/AX/AW/AV/AU/AG/AE
remain open.

## NG-105 — infer selector penetration from displayed parent size

**Label: NO-GO**

Scope: use the common size `K+3m`, or the deficit relative to that number, as
if it determined how many gates depend on the interpolating row selector.

Failure: LEMMA-151 constructs two circuits for the same function with exactly
`K+3m` gates. Aggregating the implication tail before one final AND gives
`D_a<=K+1`; interleaving the same `m` conjunctions above `H` gives `D_a>=m`,
`Q>=4m`, and `b=0`. Associativity moves a linear selector-dependent region
without changing size. Hence size data do not select the high-penetration
representation.

Model: two explicit unrestricted non-uniform circuits for one base conjoined
with disjoint implication clauses; equal size `K+3m`; unrestricted depth and
fanout; AND/OR fan-in two and NOT fan-in one; no randomness, advice, oracle,
promise, distribution, or algebraic model. Size-only selector inference is
closed; GATE-004AY/AX/AW/AV/AU/AG/AE remain open for positive deficit.

## NG-106 — locate the last circuit saving from the scalar deficit recurrence

**Label: NO-GO**

Scope: combine only `Delta_0=0`, increments in `{0,1}`, and
`Delta_m<=K` to conclude that the last positive increment occurs by
`Delta_m+K`.

Failure: the abstract sequence staying zero through `m-1` and jumping to one
at `m` satisfies all those constraints whenever `K>=1`, yet has last increase
`r=m`. In the canonical regime `m>>K`, it violates the required timing by a
linear margin. The sequence is an arithmetic witness, not a claimed circuit-
complexity realization.

Model: integer abstraction of nested implication circuit complexities;
increments zero or one and endpoint at most `K`; circuit topology,
uniformity, depth, fanout, randomness, advice, oracle access, promises,
distributions, and algebraic structure are absent. Recurrence-only timing is
closed; GATE-004AZ/AY/AX/AW/AV/AU/AG/AE remain open.

## NG-107 — localize final savings from full Hall incidence alone

**Label: NO-GO**

Scope: use only the dependency-cone neighborhood cardinalities
`|union_{i in I}P_i|>=|I|` for every clause subset to force a saving witness
of size at most `K+d`.

Failure: take clause indices as vertices of an `m`-cycle and resources as its
edges, with each index adjacent to its two incident edges. Every proper
nonempty subset `I` has neighborhood union `|I|+c` for some complement-
component count `c>=1`; the full set has union exactly `m`. With abstract
surplus `sigma=1`, the induced deficit is zero on every proper cardinality and
one only at `m`. All Hall inequalities hold while localization fails.

Model: explicit finite clause-resource incidence systems; no Boolean-circuit
realizability claim; full Hall expansion but no gate orientation, depth,
fanout, Boolean semantics, randomness, advice, oracle, promise, distribution,
or algebraic circuit structure. Hall-cardinality-only localization is closed;
GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open.

## NG-108 — promote base-tail cone overlap to restriction survival

**Label: NO-GO**

Scope: infer from LEMMA-154's shared dependency-path membership that each
matched resource survives after all unmatched clauses are set to their
neutral value one.

Failure: the NOT gate computing
`NOT(H AND q_1 AND NOT q_2 AND ... AND NOT q_m)` lies on paths from the base
and every clause signal and depends essentially on all of them. Setting any
`q_i=1` for `i>=2` makes the inner conjunction zero and the NOT output
constant. Thus path membership does not bound the clause set needed for
semantic survival.

Model: explicit unrestricted Boolean gate function in a mixed base-tail
dependency cone; non-uniform linear-size witness; no minimum-circuit or saving
claim; unrestricted depth/fanout; AND/OR fan-in two and NOT fan-in one; no
randomness, advice, oracle, promise, distribution, or algebraic model.
Cone-membership-only survival is closed; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE
remain open.

## NG-109 — import a basis-agnostic direct-sum theorem from disjoint supports

**Label: NO-GO**

Scope: infer additive base-tail cost, an optimal decomposition-respecting
circuit, or small saving support solely from the disjoint variable blocks.

Failure: PAUL76 proves that in a general two-input switching-gate model there
are arbitrarily complex scalar functions `f` whose two disjoint copies under
OR have complexity at most `(1+epsilon)C(f)`. Thus disjointness does not
support a generic direct-sum principle. The source model counts general binary
gates and differs from the repository's counted AND/OR/NOT basis, so the paper
is not a counterexample to GATE-004BA and no numeric bound transfers.

Model: literature comparison between unrestricted general binary switching
gates and counted fan-in-two AND/OR plus unary NOT; non-uniform exact finite
functions; unrestricted depth; no randomness, advice, oracle, promise,
distribution, or algebraic model. Basis-agnostic direct-sum inference is
closed; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open.

## NG-110 — localize maximal deficit from endpoint counts alone

**Label: NO-GO**

Scope: infer GATE-004BB solely from LEMMA-155's numerical/topological tuple:
rank zero, exactly `m` NOT gates, and survival of all those NOT gates under a
satisfying-base restriction.

Failure: the explicit formula
`F(x,q)=x AND AND_i NOT q_i` has rank zero and exactly `m` displayed NOT
gates, all of which survive `x=1`. Fixing any one abstract clause signal
`q_j=1`, however, makes the output constant zero and removes all remaining
tail NOTs under constant propagation. Rank, count, and base survival do not
record the signal polarity needed for prefix restriction.

Model: explicit non-uniform fanout-one formulas with binary AND and unary NOT;
every `m>=1`; unrestricted depth; no minimum-size or canonical-function claim;
no randomness, advice, oracle, promise, distribution, or algebraic model. The
witness does not refute GATE-004BB. It closes only endpoint-count-only
inference. LEMMA-157 later proves GATE-004BB using exact read-once wiring;
GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open.

## NG-111 — derive one-clause pruning from scalar NOT-state counts

**Label: NO-GO**

Scope: use only LEMMA-156's exact scalar trajectory
`0,1,1,2,2,...,m,m` to persistently match NOT gates to clauses and prove
GATE-004BC.

Failure: for two abstract labels, the down-state sets can follow
`empty -> {a} -> {b} -> {a,b} -> {a,b}`. Falling steps increase cardinality
by one and repair steps preserve it exactly, but the first repair swaps the
identity of the down-state NOT. This is compatible with the paired-transition
accounting behind the scalar inequality. Fresh labels extend the trace to any
`m>=2`.

Model: explicit finite state-set traces with no formula-realizability claim;
no circuit depth or gate topology represented; no randomness, advice, oracle,
promise, distribution, or algebraic model. The trace does not refute
GATE-004BC. It closes scalar-state-only pruning. LEMMA-157 later proves
GATE-004BC/BB using exact read-once wiring; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE
remain open.

## NG-112 — derive one-excess pruning from residual integer strata

**Label: NO-GO**

Scope: infer GATE-004BE using only LEMMA-158's possible pairs `(q,rho)` after
a satisfying-base restriction.

Failure: take an abstract resource set `R` of size `m+1` and declare the
survival set under every neutral single-clause restriction to be all of `R`.
The table can be assigned any allowed NOT/cycle partition from LEMMA-158,
because the integer pair places no constraint on clause-resource incidence or
survival. No restriction loses a resource.

Model: explicit finite resource/survival tables; no Boolean-circuit
realizability, depth, fan-in, uniformity, randomness, advice, oracle, promise,
distribution, or algebraic model. The table does not refute GATE-004BE. It
closes only stratum-count-only pruning. LEMMA-164/165 later prove
GATE-004BE/BD using topology and Boolean residuals; GATE-004BA/AZ/AY/AX/AW/
AV/AU/AG/AE remain open.

## NG-113 — lift a residual private NOT directly to the parent

**Label: NO-GO**

Scope: infer parent-level clause locality and GATE-004BF solely because a NOT
gate specializes to `NOT u_i` in one satisfying-base residual formula.

Failure: for any nonconstant base mask `R(X)` with `R(x*)=0`, the gate
`g_i=NOT(u_i OR R(X))` specializes to `NOT u_i` at `x*` but globally depends
on the base. Setting `u_i=0` leaves `NOT R(X)`, which is nonconstant. A single
cofactor therefore does not determine the parent support or make the gate
constant under tail restriction.

Model: one explicit non-uniform Boolean gate function; no minimum-circuit,
unicyclic-parent, or full-neutral-restriction survival claim; OR fan-in two,
NOT fan-in one, unrestricted ambient depth/fanout; no randomness, advice,
oracle, promise, distribution, or algebraic model. Residual-locality-only
lifting is closed. LEMMA-160/163 later prove GATE-004BF using the full
factorization; LEMMA-164/165 later prove GATE-004BE/BD; GATE-004BA/AZ/AY/AX/
AW/AV/AU/AG/AE remain open.

## NG-114 — infer unicyclic survival from regional NOT counts

**Label: NO-GO**

Scope: derive GATE-004BG only from LEMMA-160's exact upstream/downstream NOT
split in the no-cut or sole-cut partition.

Failure: an occurrence that is `NOT u_i` in a satisfying cofactor may be
decorated globally as `NOT(u_i OR R_i(X_base))`. Such mixed occurrences
preserve the same regional integer counts while changing parent support. The
counts do not state whether a second output path retains the occurrence or
the unique cycle after clause neutralization.

Model: abstract regional NOT allocations decorated by explicit non-uniform
mixed Boolean gate functions; no minimum unicyclic realization claim;
unrestricted ambient depth, OR fan-in two and NOT fan-in one; no randomness,
advice, oracle, promise, distribution, or algebraic model. NOT-split-only
survival is closed. Tree wiring and LEMMA-163 later prove GATE-004BG/BF, and
LEMMA-164/165 later prove GATE-004BE/BD; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE
remain open.

## NG-115 — derive two-excess pruning from source/rank equality data

**Label: NO-GO**

Scope: infer GATE-004BM from only the source degree, parent and residual
ranks, regional clause counts, regional NOT bounds, and equality/slack status
isolated by LEMMA-166.

Failure: the abstract assignment `r=2,d=2,a=0,b=j,p=0,N=j` meets the exact
residual-rank and NOT equalities and has total resource `j+2`. A formal
survival table may nevertheless retain all `j+2` resource labels under every
neutral one-clause restriction, because none of the scalar fields constrains
resource identity or survival.

Model: explicit integer/source data and finite survival sets; no Boolean
circuit realizability, depth, fan-in, uniformity, randomness, advice, oracle,
promise, distribution, or algebraic computation. This does not refute
GATE-004BM. It closes source-rank-count-only pruning and leaves GATE-004BN as
the Boolean/topological equality gate.

## NG-116 — close a primary base source by arity induction

**Label: NO-GO**

Scope: iterate LEMMA-170 using only essential base arity as a well-founded
measure until every base-only core source disappears.

Failure: if the source is the primary input `x`, compression replaces it by a
fresh input `z` and merely renames the distinguished argument of
`H(x,Y)=G(x,Y)`. Essential arity, cycle rank, NOT count, and the factor graph
at the interface are unchanged. There is no strict inductive descent.

Model: exact Boolean variable renaming and integer arity; no minimum-circuit
counterexample, randomness, advice, oracle, promise, distribution, or
algebraic model. This does not refute GATE-004BP. It closes arity-only
induction and leaves GATE-004BQ to exploit cofactor or path structure.

## NG-117 — glue independently minimal primary cofactors

**Label: NO-GO**

Scope: combine separate resource-`j` circuits for `H_0 W_{j-1}` and
`H_1 W_{j-1}` into a resource-`j+1` circuit for `H(x,Y)W_{j-1}` using only
their scalar bounds.

Failure: the witnesses need not identify any NOT gate, cycle, or tail
subgraph. Two disjoint abstract resource sets of size `j` satisfy both bounds,
but their Shannon-selector union has `2j` resources before selector cost.
The maximum-plus-one conclusion requires common resource identity not present
in the premises.

Model: abstract pairs of non-uniform cofactor witnesses and finite resource
sets; no common-parent realizability, randomness, advice, oracle, promise,
distribution, or algebraic model. This does not refute GATE-004BR. It closes
cofactor-minimum-only gluing and leaves GATE-004BS on the actual common graph.

## NG-118 — infer clause identity from common NOT survival

**Label: NO-GO**

Scope: use LEMMA-172's survival of every NOT under both nonzero primary
cofactors to infer a tail clause whose private NOT has the same identity in
both codes.

Failure: the physical gate `NOT(u_i OR (x AND u_k))` survives both codes but
is `NOT u_i` at `x=0` and `NOT(u_i OR u_k)` at `x=1`. Neutralizing clause
`i` makes the first specialization constant while the second remains
`NOT u_k`. No `NOT x` is used.

Model: one explicit non-uniform local gate; no exact-parent minimum,
resource-total, randomness, advice, oracle, promise, distribution, or
algebraic model. This does not refute GATE-004BS. It closes survival-only
identity and leaves GATE-004BT to prove uniform neutralization from the common
minimum graph.

## NG-119 — align clauses from the common residual cycle space

**Label: NO-GO**

Scope: combine LEMMA-174's common equal-rank cycle space with one
clause-coordinate loss pair in each primary code and infer a common pair.

Failure: choose one nonzero vector `v` and distinct clauses `i,k`. Let code
zero lose `v` only under `i` and code one lose it only under `k`. Both codes
have the same pre-restriction vector space and each has a loss witness, but
their clause-vector incidence sets are disjoint.

Model: abstract two-code incidence over one finite `F_2` space; no circuit
realizability, depth, fan-in, randomness, advice, oracle, promise,
distribution, or algebraic-computation claim. This does not refute
GATE-004BT. It closes dimension/vector-only alignment and leaves GATE-004BU
to use actual directed paths and Boolean semantics.

## NG-120 — charge every changed tail signature to a selector gate

**Label: NO-GO**

Scope: if uniform neutralization fails, inject each affected tail clause into
a distinct selector-dependent gate and derive linear selector penetration or
a resource contradiction.

Failure: LEMMA-175's gate
`NOT(v OR (x AND (u_1 OR ... OR u_m)))` changes from `NOT v` to a function
depending on every `u_i`, while only the final AND, OR, and NOT gates depend
on `x`. One constant-size selector-dependent region therefore mixes an
arbitrarily large tail. LEMMA-151/NG-105 also show no size premium follows
from selector penetration alone.

Model: explicit non-uniform local gadget family and integer signature counts;
no exact minimum-parent, randomness, advice, oracle, promise, distribution,
or algebraic model. This does not refute GATE-004BU. It closes
signature-count-only charging and leaves GATE-004BV to prove an exposed form
by exact exchange.

## NG-121 — invoke an unspecified size-preserving normal-form exchange

**Label: NO-GO**

Scope: replace the common minimum parent by another minimum representation
that exposes a uniform neutral NOT or cycle path, citing “normal-form
exchange” without giving the exchange or a descending invariant.

Failure: LEMMA-153 already makes `N+r` fixed by size and essential-input
count. The remaining assertion — existence of the exposed minimum
representation — is the structural theorem to be proved. Naming it as an
exchange provides neither a function-preserving rewrite nor a well-founded
descent and therefore cannot be used as an intermediate proof step.

Model: finite non-uniform minimum pruned AND/OR/NOT circuits; unrestricted
depth and fanout; binary AND/OR and unary NOT; no randomness, advice, oracle,
promise, distribution, or algebraic computation. This does not refute a
normal form. LEMMA-176 supplies an independent selector-minimal choice, and
GATE-004BW must prove exposure from that extremality.

## NG-122 — selector minimality alone forces a neutral resource loss

**Label: NO-GO**

Scope: infer from minimum total size and minimum selector-sensitivity count
that one of arbitrarily many tail-block neutralizations must delete a NOT or
lower cycle rank.

Failure: LEMMA-177 proves that
`NOT(v OR (x AND (u_1 OR ... OR u_m)))` has exact circuit size `m+2` and
minimum selector count three. Its displayed minimum formula has `N+r=1`,
and every restriction `u_i=0` leaves one NOT and rank zero. Thus every one of
the `m` singleton neutralizations preserves the resource sum.

Model: uniform explicit minimum AND/OR/NOT formulas; unrestricted competing
circuits for the exact lower bounds; binary AND/OR, unary NOT, no randomness,
advice, oracle, promise, distribution, or algebraic computation. The blocks
are not implication pairs, so this does not refute GATE-004BW. It closes
extremality-only reasoning and leaves GATE-004BX to use the three satisfying
and one falsifying codes of each implication clause.

## NG-123 — model a two-gate saving as an exposed pair shell

**Label: NO-GO**

Scope: assume a hypothetical `C(A AND (t OR NOT u))=C(A)+2` circuit consists
of a minimum base circuit plus only two pair-sensitive attachment gates, and
exclude the saving by enumerating that shell.

Failure: LEMMA-178 proves that every realization of the four-code table needs
at least three pair-sensitive gates. Under the two-gate total increment, all
three satisfying restrictions nevertheless delete exactly two binary gates
and preserve every NOT and cycle coordinate. Hence at least one pair-
sensitive gate survives each restriction as nonconstant base computation.
The only possible saving is interleaved, not an exposed shell.

Model: finite non-uniform minimum AND/OR/NOT circuits for an arbitrary
nonconstant base and one fresh implication pair; unrestricted depth and
fanout; no randomness, advice, oracle, promise, distribution, or algebraic
computation. This does not prove or refute the two-gate plateau. It closes the
output-shell-only architecture and leaves GATE-004BY to uncross a pair-
minimal interleaved parent.

## NG-124 — expose the fresh negative literal as `NOT u`

**Label: NO-GO**

Scope: locate a physical pair-only NOT for the fresh negative literal and
delete it under one satisfying restriction, copying the displayed three-gate
extension.

Failure: a two-gate plateau preserves every parent NOT under each of `00`,
`01`, and `11`. Any NOT depending only on the fully fixed pair becomes
constant and would be pruned. LEMMA-179 proves that every NOT carrying the
necessary negative `u` dependence instead also depends on base variables; its
input is an internal mixed binary gate and receives neither raw pair input
directly.

Model: finite non-uniform minimum AND/OR/NOT circuits at exact
`C(A AND (t OR NOT u))=C(A)+2`; unrestricted depth and fanout; no randomness,
advice, oracle, promise, distribution, or algebraic computation. This does
not refute the plateau. It closes literal-NOT-only pruning and leaves
GATE-004BZ to uncross the earliest mixed surviving NOT.

## NG-125 — infer uncrossing from ordered earliest-NOT cofactors

**Label: NO-GO**

Scope: combine the pointwise order `n_01>=n_11` with equality of the final
`01,11` output cofactors and conclude that the switching cone contains a
deletable gate or a size-preserving simplification.

Failure: with independent `u,v,w`, let
`n=NOT(v OR (u AND w))`, `q=NOT v AND w`, and `d=n OR q`. Then the two
cofactors of `n` are the distinct ordered functions `NOT v` and
`NOT v AND NOT w`, while `d=NOT v` for both values of `u`. One OR gate masks
the ordered difference without a generic local deletion.

Model: explicit constant-size non-uniform AND/OR/NOT gadget; unrestricted
ambient depth/fanout; no minimum-parent claim, randomness, advice, oracle,
promise, distribution, or algebraic computation. This is not a plateau
counterexample. It closes cofactor-order-only rewriting and leaves
GATE-004CA to use pair minimality, exact resource survival, or the zero code.

## NG-126 — infer a saving from the local first-cancellation type

**Label: NO-GO**

Scope: conclude that either the one-sided mask containment or the two-sided
reconvergence cycle of LEMMA-181 directly yields a deletion or same-size
uncrossing.

Failure: both types have constant-size identities. The NG-125 mask gadget is
one-sided. For the two-sided case, `p=u AND v`, `q=NOT u AND v`, and
`d=p OR q` give `d=v`; both inputs change with `u` and their paths create an
undirected reconvergence cycle. Neither local table alone supplies a global
minimum-circuit exchange.

Model: finite non-uniform AND/OR/NOT gadgets; constant witness depth,
unrestricted ambient depth/fanout; no minimum-parent claim, randomness,
advice, oracle, promise, distribution, or algebraic computation. These are
not plateau counterexamples. The no-go closes local-type-only reasoning and
leaves GATE-004CB to use pair minimality, minimum satisfying minors, and the
fourth zero cofactor in the one-sided branch.

## NG-127 — treat semantic edge erasure as a free DAG rewrite

**Label: NO-GO**

Scope: after LEMMA-182 replaces the satisfying cofactors of one input edge by
their meet or join, infer a same-size circuit with fewer pair-sensitive gates.

Failure: the replacement is a Boolean function, not an existing AND/OR/NOT
gate. Constructing it can require new gates or duplicated feeding cones.
Furthermore the source gate may have other consumers, so changing it globally
need not preserve the parent function, while changing only one outgoing edge
can incur exactly that duplication cost. Equality of four cofactors at `d`
does not control either cost.

Model: individual finite non-uniform unrestricted AND/OR/NOT DAG; unrestricted
depth and fanout; no randomness, advice, oracle, promise, distribution, or
algebraic computation. This does not refute the one-sided exchange. It closes
semantic-erasure-only reasoning and leaves GATE-004CC to provide an explicit
same-size basis realization or force satisfying-code resource loss.

## NG-128 — infer a replacement budget from fanout one

**Label: NO-GO**

Scope: assume the masked path signal `p` has only the consumer `d`, and infer
that LEMMA-182's canonical signal can replace it without increasing the gate
count.

Failure: for raw `x,u,t`, take `p=u OR x`, `q=t AND NOT x`, and `d=p OR q`.
At codes `01,11`, the stable `q=NOT x` masks `p_01=x` versus `p_11=1`.
The canonical replacement is `x OR (u AND NOT t)`. It has exact size three:
three essential inputs require at least two binary gates and nonmonotonicity in
`t` requires a NOT. The private signal `p` itself uses one gate.

Model: explicit constant-size non-uniform AND/OR/NOT gadget; exact local sizes
one and three; unrestricted ambient depth, fan-in two/one, and fanout-one at
`p`; no minimum-parent claim, randomness, advice, oracle, promise,
distribution, or algebraic computation. This is not a plateau counterexample.
It closes fanout-one-only budgeting and leaves GATE-004CD to obtain an actual
private-cone realization or charge a shared exit to resource loss.

## NG-129 — infer resource loss from shared-cycle existence

**Label: NO-GO**

Scope: use the reconvergence cycle created by a live second exit from `p` as
though its existence forced some satisfying restriction to kill a cycle
coordinate.

Failure: exact plateau rank equality and LEMMA-174 force every parent cycle
coordinate to survive every satisfying minor modulo contractions. Locally,
let `r=x XOR y`, `s=NOT r`,
`p=(NOT u AND x) OR (u AND y)`, `d=p OR r`, `c=p AND s`, and
`o=d AND NOT c`, with XOR expanded in the standard AND/OR/NOT basis. For both
values of `u`, `d=x OR y`, `c=x AND y`, and `o=x XOR y`; both exits remain
nonconstant and their cycle survives after multiplexer contraction.

Model: explicit constant-size non-uniform AND/OR/NOT double-cancellation DAG
plus the general equal-rank graph theorem; unrestricted ambient depth and
fanout; no minimum-gadget claim, randomness, advice, oracle, promise,
distribution, or algebraic computation beyond cycle space over `F_2`. This is
not a plateau counterexample. It closes topology-only charging and leaves
GATE-004CE to identify a kernel from edgewise four-code signatures.

## NG-130 — infer a cycle kernel from the full four-code table and local signatures

**Label: NO-GO**

Scope: combine two `01/11` cancellation fronts with the exact table
`F_00=F_01=F_11=A`, `F_10=0`, and infer that their cycle is killed in a
satisfying minor without using minimum-size structure.

Failure: set `r=x XOR y`, `s=NOT r`,
`p=(NOT u AND x) OR (u AND y)`, `d=p OR r`, `c=p AND s`,
`a=d AND NOT c`, `i=t OR NOT u`, and `F=a AND i`, expanding XOR in the
AND/OR/NOT basis. Then `d=x OR y`, `c=x AND y`, and `a=x XOR y` for both
values of `u`. With `A=x XOR y`, the four output cofactors are exactly
`A,A,0,A`, while the two branches from `p` remain nonconstant and cyclic in
all three satisfying restrictions modulo multiplexer contraction.

Model: explicit constant-size non-uniform AND/OR/NOT circuit with unrestricted
ambient depth/fanout; no minimum or plateau claim, randomness, advice, oracle,
promise, distribution, or algebraic computation beyond cycle space over
`F_2`. This is not a plateau counterexample. It closes full-table/signature-
only inference and leaves GATE-004CF to use the exact two-binary-deletion
budget or obtain a private certificate.

## NG-131 — charge cancellation fronts injectively to eliminations

**Label: NO-GO**

Scope: count distinct first `01/11` cancellation gates or reconvergence cycles
and assign a different binary neutralization event to each.

Failure: for every `m`, LEMMA-186 uses one multiplexer signal `p` with
`p_01=x`, `p_11=y`, stable masks
`q_i=(x XOR y) OR z_i`, and live fronts `d_i=p OR q_i`. Every `d_i` has equal
satisfying cofactors and remains essential in an AND-tree output, but all
incoming differences equal the single function `x XOR y`. Arbitrarily many
fronts can therefore be fanout copies of one semantic obligation.

Model: uniform `O(m)`-size non-uniform AND/OR/NOT family; unrestricted target
depth/fanout, fan-in two/one; no minimum or plateau claim, randomness, advice,
oracle, promise, distribution, or algebraic computation beyond the Boolean
function vector space over `F_2`. This is not a plateau counterexample. It
closes front-count-only charging and leaves GATE-004CG to prove three event-
separated path regions using minimum-parent structure.

## NG-132 — require one eliminated gate per canonical carrier region

**Label: NO-GO**

Scope: after defining pruning-independent Boolean-difference carriers, infer
that every such region must meet a distinct eliminated binary gate in a
satisfying restriction.

Failure: let `h=u OR x`, let `g_i=h OR z_i`, and combine all `g_i` in a binary
AND tree. Every `g_i` depends on `u` in the parent. Under `u=0`, the single
upstream `h` contracts to `x`, while every `g_i` survives as the essential
binary base gate `x OR z_i`. Thus arbitrarily many carrier routes are absorbed
into surviving base computation after one upstream event. LEMMA-178 likewise
forces at least one pair-sensitive survivor in every hypothetical plateau
minor.

Model: uniform `O(m)`-size non-uniform AND/OR/NOT family; unrestricted target
depth/fanout, fan-in two/one; no minimum or plateau claim, randomness, advice,
oracle, promise, distribution, or algebraic computation. This is not a
plateau counterexample. It closes single-code carrier-coverage counting and
leaves GATE-004CH to compare absorption across all three minimum satisfying
prunings.

## NG-133 — promote physical overlap to semantic alignment

**Label: NO-GO**

Scope: use the `K-4` three-way survivor intersection from LEMMA-188 as though
each common physical gate computed the same base function under `00,01,11`.

Failure: let `r=x XOR y`,
`p=(NOT u AND x) OR (u AND y)`, `g=p OR z`, `a=g OR r`,
`i=t OR NOT u`, and `F=a AND i`, expanding XOR and the multiplexer in the
AND/OR/NOT basis. With `A=x OR y OR z`, the output cofactors are exactly
`F_00=F_01=F_11=A`, `F_10=0`. The same physical binary gate `g` survives all
three satisfying restrictions, but `g_00=g_01=x OR z` and `g_11=y OR z`.

Model: explicit constant-size non-uniform AND/OR/NOT exact-table circuit;
unrestricted ambient depth/fanout, fan-in two/one; no minimum or plateau claim,
randomness, advice, oracle, promise, distribution, or algebraic computation.
This is not a plateau counterexample. It closes overlap-cardinality-only
alignment and leaves GATE-004CI to prove a strict descent in the common-
backbone misalignment potential or expose three distinct classes.

## NG-134 — normalize the switching backbone to zero misalignment

**Label: NO-GO**

Scope: assume or freely normalize to `W=0` and then use complete gatewise
alignment across `00,01,11`.

Failure: the earliest mixed NOT in the active switching branch satisfies
`n_01!=n_11`. LEMMA-178 preserves every NOT in every satisfying minor, so this
physical gate belongs to every common backbone and contributes to `W`.
LEMMA-189 therefore gives `W>=1` for every pruning triple. Assuming `W=0`
removes the branch whose exclusion is being attempted.

Model: extremal finite non-uniform minimum unrestricted AND/OR/NOT plateau
parents; unrestricted depth/fanout, fan-in two/one; no randomness, advice,
oracle, promise, distribution, or algebraic computation. This is not a
plateau counterexample and does not refute a rewrite that itself leaves the
branch. It closes zero-alignment-only normalization and leaves GATE-004CJ to
descend above the mandatory floor and analyze the case `W=1` if reached.

## NG-135 — derive a contradiction from carrier cardinality alone

**Label: NO-GO**

Scope: combine `|H|<=7` with the three two-element satisfying deletion sets
and infer that some code must delete at least three carrier gates.

Failure: the abstract set
`H={n,a_00,b_00,a_01,b_01,a_11,b_11}` with
`E_s={a_s,b_s}` for `s in {00,01,11}` meets every cardinality conclusion of
LEMMA-190. The deletion pairs are disjoint and cover exactly `H minus {n}`.
Thus the counting bound is tight and no pigeonhole contradiction follows.

Model: one finite non-uniform abstract incidence witness, explicitly not a
Boolean circuit or plateau realization; seven labels, no circuit depth or
fan-in claim; no randomness, advice, oracle, promise, distribution, field, or
algebraic computation. It closes carrier-cardinality-only reasoning. The
remaining GATE-004CK obligation must use directed topology, the distinguished
`h->n` edge, cancellation boundaries, full cofactor identities, or cycle-rank
preservation.

## NG-136 — reject the two-gate carrier from topology and the output table

**Label: NO-GO**

Scope: treat `H_{01,11}={h,n}`, `h->n`, earliest switching, a binary
cancellation boundary, and `F_00=F_01=F_11=A`, `F_10=0` as contradictory.

Failure: for any nonconstant base, LEMMA-191 adds
`q=NOT x`, `c=x OR q`, `h=u AND c`, `n=NOT h`, `i=t OR n`, and
`F=A AND i`. Then `c=1`, the output table is exact, and the carrier is exactly
`{h,n}`. This redundant extension adds six gates and is not minimum or a
two-gate plateau. It closes only topology/table-only reasoning and leaves
GATE-004CL to exploit the three exact two-binary-deletion maps.

Model: uniform six-gate non-uniform AND/OR/NOT extension of every finite base;
unrestricted base depth and fanout, fan-in two/one; no randomness, advice,
oracle, promise, distribution, field, or algebraic computation; exact
worst-case construction, not a SAT lower bound or terminal result.

## NG-137 — contradict the size-three carrier from local alternation

**Label: NO-GO**

Scope: infer that the AND→OR or OR→AND chain and its two-gate neutral
contraction are locally impossible.

Failure: `g=u AND x`, `h=g OR y`, `n=NOT h`, `d=h OR n` has canonical
`01/11` carrier exactly `{g,h,n}` and binary equal boundary `d=1`. At `u=0`,
`g,h` contract while `n=NOT y` remains nonconstant. Boolean duality gives the
OR→AND case. This is a constant-size local non-uniform gadget, not the full
`A,A,0,A` table, a minimum circuit, or a plateau. It closes local-chain-only
reasoning and leaves GATE-004CN to use every fanout exit and cross-code pruning.

Model: explicit constant-depth AND/OR/NOT gadget; fan-in two/one and arbitrary
ambient fanout; no randomness, advice, oracle, promise, distribution, field,
or algebraic computation; every assignment to `u,x,y`; not a terminal result.

## NG-138 — infer a private carrier cone from `fanout(g)=1`

**Label: NO-GO**

Scope: promote isolation of the first carrier gate `g` to isolation of the
whole binary predecessor region `{g,h}`.

Failure: with `g=u AND x`, `h=g OR y`, `n=NOT h`, `r=NOT x`, and
`b=h AND r`, the gate `g` has only consumer `h`, but `h` feeds both `n,b`.
The boundary is nonconstant and aligned:
`b_01=y AND NOT x=b_11`; it survives the neutral contraction. This is a local
nonminimal gadget, not the full output table or a plateau. It closes source-
fanout-one-only privacy and leaves GATE-004CO to classify shared `h` exits.

Model: constant-size non-uniform AND/OR/NOT gadget; constant local depth,
fan-in two/one, `g` fanout one and `h` fanout at least two; no randomness,
advice, oracle, promise, distribution, field, or algebraic computation.

## NG-139 — charge one deletion per aligned boundary

**Label: NO-GO**

Scope: use the number or fanout multiplicity of shared `h` boundaries as a
lower bound on neutral-code gate losses.

Failure: for every `m`, let `g=u AND x`, `h=g OR y`, `n=NOT h`, and
`b_i=h AND (NOT x AND z_i)`. Each `b_i` is nonconstant and satisfies
`(b_i)_01=(b_i)_11=y AND NOT x AND z_i`; all survive the neutral contraction
while `h` has `m+1` consumers. This is a uniform `O(m)` local multi-exit DAG,
not a minimum single-output circuit, the full table, or a plateau. It closes
boundary-count-only charging and leaves GATE-004CP to use shared cost.

Model: unrestricted AND/OR/NOT local family; constant depth, fan-in two/one,
unbounded `h` fanout; no randomness, advice, oracle, promise, distribution,
field, or algebraic computation; every `m>=1` and every assignment.

## NG-140 — globally factor a boundary from its satisfying-row mask

**Label: NO-GO**

Scope: replace `h` by its neutral expression using only equality under
`01/11`, and infer a global function-preserving rewrite.

Failure: with `g=u AND x`, `h=g OR y`,
`r=NOT x OR NOT t`, and `b=h AND r`, one has
`b_01=b_11=y AND NOT x`, but `b_00=y` and `b_10=x OR y`. The satisfying-row
factoring erases the switching behavior needed on the row containing code
`10`. This constant-size local gadget is not minimum, a full output circuit,
or a plateau. GATE-004CQ must preserve complete four-code vectors.

Model: unrestricted constant-depth AND/OR/NOT local gadget; fan-in two/one,
fanout unrestricted; no randomness, advice, oracle, promise, distribution,
field, or algebraic computation; every assignment to `x,y,u,t`.

## NG-141 — contradict a handoff from full signatures and output table

**Label: NO-GO**

Scope: combine a size-three `01/11` carrier, a complete four-code switching
boundary, and the exact `A,A,0,A` output table without minimum-cost input.

Failure: LEMMA-197 takes `A=x AND NOT y`, computes the exact implication via
`g=u AND x`, `h=g OR y`, `n=NOT h`, and embeds the switching boundary through
`c=b OR NOT b=1` before the final output. The canonical `01/11` carrier remains
exactly `{g,h,n}` and the boundary has the LEMMA-196 four-vector. The circuit
is deliberately redundant, not minimum or a plateau. GATE-004CR must use
minimum cost, exact losses, a private certificate, or a cycle-minor conflict.

Model: one finite non-uniform constant-size AND/OR/NOT single-output circuit;
constant depth, fan-in two/one, fanout unrestricted; no randomness, advice,
oracle, promise, distribution, field, or algebraic computation.

## NG-142 — charge the deletion budget by handoff count

**Label: NO-GO**

Scope: infer a contradiction from many bisensitive handoffs or neutral
pair-sensitive survivors.

Failure: for every `m`, extend LEMMA-197 with
`r_i=(NOT x AND z_i) OR NOT t`, `b_i=h AND r_i`, and tautologies
`c_i=b_i OR NOT b_i`; AND the `c_i` into the exact output. The resulting
single-output circuit retains the exact table and carrier `{g,h,n}` and has
`m` distinct handoffs. It is uniformly `O(m)` but deliberately redundant,
not minimum or a plateau. GATE-004CS must use an extremal minimum-parent
potential rather than multiplicity.

Model: unrestricted non-uniform AND/OR/NOT exact-table family; `O(m)` size,
fan-in two/one, unrestricted depth/fanout; no randomness, advice, oracle,
promise, distribution, field, or algebraic computation; every `m>=1`.

## NG-143 — promote semantic `u`-privacy to a physical private cone

**Label: NO-GO**

At `Q=0`, `n` being the unique `u`-sensitive child does not make every other
exit removable. With `g=u AND x`, `h=g OR y`, `n=NOT h`, and
`b=h AND NOT x`, the identity `b=y AND NOT x` makes `b` nonconstant and
`u`-independent while it physically consumes `h`. This local gadget is not
minimum, a full table, or a plateau. GATE-004CT must audit physical cost or
sensitivity counterflow.

Model: constant-size unrestricted non-uniform AND/OR/NOT local gadget;
constant depth, fan-in two/one, `h` fanout two; no randomness, advice, oracle,
promise, distribution, field, or algebraic computation.

## NG-144 — infer a contradiction from counterflow reconvergence alone

**Label: NO-GO**

Scope: treat a second `u`-sensitive route meeting `h` at a globally
`u`-cancelling boundary as an automatic third deletion or killed cycle.

Failure: GATE-004CT-COUNTERFLOW-LOCAL-ONLY builds `r` so that at `t=1` it is
the aligned mask `NOT x`, while at `t=0` it equals `z` for `u=0` and
`y AND z` for `u=1`. Then `b=h AND r` is respectively `y AND NOT x` and
`y AND z`, independent of `u` on both rows. The local gadget is nonminimal,
not a full table or plateau. GATE-004CU must use minimum cost or minor loss.

Model: constant-size unrestricted non-uniform AND/OR/NOT two-route gadget;
constant depth, fan-in two/one, fanout unrestricted; no randomness, advice,
oracle, promise, distribution, field, or algebraic computation.

## NG-145 — infer cycle loss from the existence of a counterflow cycle

**Label: NO-GO**

Scope: use the named reconvergence cycle at a counterflow boundary as though
some satisfying restriction must kill that coordinate.

Failure: LEMMA-201 constructs the nonzero coordinate `gamma_b`, but
LEMMA-174 and LEMMA-185 imply that every satisfying restriction preserves the
entire parent cycle space modulo contraction. Hence the image of `gamma_b` is
nonzero in `00`, `01`, and `11`. Its edge support may change. A contradiction
requires a separate theorem forcing independence, a third deletion, or a
non-bridge deletion; existence alone supplies none of these.

Model: minimum unrestricted non-uniform AND/OR/NOT plateau endpoint; parent
size `K+2`, unrestricted depth, fan-in two/one, fanout unrestricted; cycle
spaces over `F_2`; every satisfying code; no randomness, advice, oracle,
promise, or distributional qualification.

## NG-146 — distinguish counterflow by abstract cross-minor coordinates

**Label: NO-GO**

Scope: compare only the vector-space images of `gamma_b` in the three
satisfying minors and infer independence, extra rank, or Boolean factoring.

Failure: LEMMA-202 proves that each restriction map `rho_s` is an isomorphism.
Thus `rho_t o rho_s^{-1}` aligns the images of every parent coordinate, not
just the counterflow coordinate. A two-subdivision graph witness additionally
has exact two-vertex contraction, unchanged cycle rank, and survival of its
marked cycle without deleting a non-bridge edge. It is not a minimum Boolean
plateau witness. Physical contraction support and four-code Boolean labels
are absent from the abstract data and must be restored in GATE-004CW.

Model: finite exact-plateau cycle spaces and a subdivision multigraph witness;
parent size `K+2` in the circuit application, unrestricted depth, circuit
fan-in two/one, no randomness, advice, oracle, promise, or distributional
qualification; linear maps over `F_2`; every ordered satisfying-code pair.

## NG-147 — recover counterflow from satisfying-minor transport alone

**Label: NO-GO**

Scope: use only the `00`, `01`, and `11` restricted circuits to observe the
same-row `u` difference carried by the auxiliary input of a counterflow.

Failure: LEMMA-203 proves `r_01=r_11` and `r_00!=r_10`; the distinguishing
cofactor is always the unsatisfying code `10`. GATE-004CW-SATISFYING-
TRANSPORT-ONLY gives a six-input finite circuit in which an arbitrary live
`w` term occurs in `r_10` while `r_00,r_01,r_11` and every cofactor of the
boundary `b` remain fixed. The witness is nonminimal and not a plateau.
Satisfying transport must be supplemented by the exact zero cofactor.

Model: minimum unrestricted non-uniform endpoint for localization and a
constant nonminimal AND/OR/NOT witness for underdetermination; unrestricted
target depth, fan-in two/one, fanout unrestricted; exact worst-case cofactors;
no randomness, advice, oracle, promise, distribution, field, or algebraic
computation.

## NG-148 — treat semantic meet/join erasure as a free circuit exchange

**Label: NO-GO**

Scope: replace a counterflow edge by the abstract `r^dagger` of LEMMA-204 and
infer a same-size strict descent without constructing that signal.

Failure: realizing `r_00 AND r_10` or `r_00 OR r_10` can require duplicated
cofactor cones and selector gates. Shared fanout prevents globally changing
`r`, while an edge-local change can require a private copy. The exact truth-
table identity gives no bound on this DAG cost. GATE-004CX must exhibit the
basis-level rewrite, pay for it with provably freed gates, or force an exact
resource contradiction.

Model: minimum unrestricted non-uniform AND/OR/NOT endpoint DAG; parent size
`K+2`, unrestricted depth, fan-in two/one and unrestricted fanout; exact
cofactor meet/join with no size claim; no randomness, advice, oracle, promise,
distribution, field, or algebraic computation.

## NG-149 — globally specialize a shared comparable counterflow signal

**Label: NO-GO**

Scope: once comparability identifies `r^dagger` with `r|u=sigma`, replace the
physical gate `r` globally without checking its other fanouts.

Failure: GATE-004CX-GLOBAL-SPECIALIZATION-ONLY constructs
`r=x OR NOT(u OR t)`. At the cancelling boundary, its row-zero cofactors are
`1` and `x`, its row-one cofactors are both `x`, and specializing to `u=1`
preserves the boundary. A second live consumer `c=r OR z`, however, changes
under that global replacement, as does the displayed downstream output. All
auxiliary gates remain `01/11`-aligned. The witness is nonminimal, not the
implication table, and not a plateau. It does not rule out an edge-local
rewrite; it rules out the unaudited global substitution.

Model: constant finite non-uniform AND/OR/NOT shared-fanout gadget;
constant depth, fan-in two/one, `r` fanout two; exact worst-case cofactors;
no randomness, advice, oracle, promise, distribution, field, or algebraic
computation.

## NG-150 — infer counterflow descent from parent-output preservation alone

**Label: NO-GO**

Scope: globally specialize a shared comparable counterflow region, verify only
that the parent output is unchanged, and infer that the counted boundary has
been removed with strict `R_0` descent.

Failure: GATE-004CY-TERMINAL-OUTPUT-ONLY uses the same comparable signal
`r=x OR NOT(u OR t)` and adds `q=r OR u`, followed by the direct boundary
`c=h AND q`. Specializing `r` to `x` preserves the functions at the original
boundary `b`, at `c`, and at the parent output. It changes the row-zero
signature of `q` from `(1,1)` to `(x,1)`. Thus `b` leaves `R_0` exactly when
`c` enters it, and the potential does not descend. All 16 assignments satisfy
the displayed identities. The witness is nonminimal and not a plateau; it
refutes only terminal-output-only bookkeeping.

Model: constant finite non-uniform AND/OR/NOT shared-fanout gadget; constant
depth, fan-in two/one, unrestricted ambient fanout; exact worst-case four-code
cofactors; no randomness, advice, oracle, promise, distribution, field, or
algebraic computation.

## NG-151 — charge a counterflow-transfer path by length or changed-gate count

**Label: NO-GO**

Scope: after LEMMA-207 localizes a failed `R_0` descent to a changed path,
infer a circuit-size or satisfying-minor contradiction from the existence,
length, or number of changed gates on that path.

Failure: GATE-004CZ-TRANSFER-PATH-ONLY gives a uniform family for every
`m>=0`. The path `r -> q_0 -> ... -> q_m` has `m+1` changed gates after the
selected specialization. Exact cofactor formulas show that the original
boundary `b`, the new boundary `c`, and the parent output are all preserved,
while the counted counterflow transfers from `b` to `c` and total `R_0`
remains constant. Every member is nonminimal and not a plateau parent. Thus
the family does not refute a minimum-cost argument; it shows that such an
argument must actually use minimality, pruning budgets, or additional
topology rather than raw path data.

Model: uniform family of finite non-uniform AND/OR/NOT DAGs of size and depth
linear in `m`; fan-in two/one, shared source fanout two, transfer-chain fanout
one; exact worst-case four-code cofactors; no randomness, advice, oracle,
promise, distribution, field, or algebraic computation; every `m>=0` and all
assignments.
