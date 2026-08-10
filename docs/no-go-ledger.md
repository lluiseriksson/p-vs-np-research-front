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

Failure: the complete `4*71^3` audit returns six residue-1 types, all omitting
zero mask 8: `(69,72,77,78)`, `(69,73,77,78)`, `(69,74,77,78)`,
`(69,75,77,78)`, `(69,76,81,82)`, and `(69,77,81,82)`. The sampling inference
is therefore false. This is not a structural length-68 obstruction: identifiers
`1044,1060,1092,1156,16452,16516` repair the six types, and the completed
alphabet passes the exhaustive audit in LEMMA-075.

Model: exact three-block neutral contexts; fixed 86-identifier alphabet;
four-coordinate finite incidence; unrestricted later non-uniform circuits;
no randomness in the exhaustive result, advice, oracle, promise,
distribution, or algebraic computation. GATE-004AD is separately proved by
the repaired alphabet; P versus NP remains open.

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
