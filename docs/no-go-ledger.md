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
