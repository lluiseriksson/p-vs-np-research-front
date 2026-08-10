# P versus NP Research Front

> **Status: EXPLORATORY. No proof of `P != NP` or `P = NP` is claimed.**

This is an independent, long-running research repository whose only terminal
objective is an unconditional, complete, non-circular, auditable resolution of
the standard P-versus-NP problem. Restricted-model lower bounds, oracle
separations, communication lower bounds, proof-complexity lower bounds,
algebraic-complexity lower bounds, experiments, and conditional consequences
remain non-terminal unless a fully proved bridge to the standard statement is
recorded.

## Fixed terminal target

The active branch is `P != NP`. Its exact terminal formulation is:

> There is no deterministic multitape Turing machine `M` and constant `c` such
> that `M` decides the fixed binary encoding of `SAT` on every input of length
> `n` in at most `n^c + c` steps.

Here `SAT` is the exact prefix language `SAT-gamma` specified in
[`docs/sat-encoding.md`](docs/sat-encoding.md); malformed strings reject.

By Cook-Levin NP-completeness, this is equivalent to `P != NP`. The stronger
terminal-sufficient theorem currently used in the vertical map is
`SAT notin P/poly`; the map records the explicit implication to the standard
uniform statement.

## Research discipline

The immutable work cycle is:

`brick -> audit -> commit -> ledger update -> next gate`

Every result receives exactly one label:

- `EXPLORATORY`
- `NUMERICAL`
- `CONDITIONAL`
- `PROVED`
- `FORMALLY VERIFIED`
- `NO-GO`

Labels are never promoted automatically. A proof is not `FORMALLY VERIFIED`
merely because repository checks pass; that label requires a proof-assistant
kernel check of the mathematical statement and an axiom audit.

Every canonical complexity claim has a machine-readable model card in
[`verification/claims.json`](verification/claims.json). The audit rejects a
claim missing its computational model, uniformity, size, depth, fan-in,
randomness, advice, oracle access, algebraic model, quantifiers, or case regime.

## Current vertical route

`P != NP <- SAT notin P <- SAT notin P/poly <- all same-language SAT circuit-exponent rungs`

The second audit proved that the proposed unbounded-ratio family GATE-003 is
equivalent to `NP notsubseteq P/poly`, so it is rejected as a circular
decomposition. Current SAT-algorithm transfers still do not close the terminal
arrow, and reindexing or padding their fixed-exponent NP lower bounds cannot
repair the exponent ratio. The active GATE-004 asks for a first same-language
superlinear unrestricted circuit lower bound for SAT; it is explicitly
non-terminal. See
[`docs/vertical-map.md`](docs/vertical-map.md) and
[`docs/no-go-ledger.md`](docs/no-go-ledger.md).

The third cycle fixed the exact `SAT-gamma` representation and reduced
GATE-004 to GATE-004B: a SAT-specific block projection must lose
`n^(beta+delta)` gates while shortening the encoding by only `O(n^beta)` bits.
The fourth cycle proved a broader exact prefix-context family, rejected the
tempting right-context analogue because it repairs some malformed strings, and
proved a general contiguous-placement coverage limit. Coordinate averaging
cannot force gate loss, so GATE-004C isolates the surviving semantic-loss
obligation for minimum SAT circuits.

The fifth cycle audits that semantic obligation against unrestricted sharing.
LEMMA-004 proves that minimality, essential prefix inputs, and even all `2^p`
distinct residual functions can coexist with only an `O(p)` size gap because a
large core survives every restriction. GATE-004D now states the precise
SAT-specific internal residual-collision surplus that would have to overcome
this obstruction.

The sixth cycle makes the parser-state attempt exact. ENC-004 supplies `k+1`
separated neutral prefixes of common length `12k`, all leaving the same SAT
suffix function. LEMMA-007 then proves that this entire output-level pattern,
even with every prefix bit essential, can retain an arbitrary shared core
behind an `O(k^2)` shell. GATE-004E isolates the still-open requirement inside
the cross-restriction table of internal SAT gate functions.

The seventh cycle exploits the neutral family’s exact block form `X*W*` and
reduces that shell to `3p+5` gates. This closes the generic cross-table route:
even all audited parser geometry can coexist with only linear prefix overhead.
GATE-004F now asks directly for a SAT-specific surplus of same-column internal
residual-function collisions.

The eighth cycle adds the adjacent annihilating context: changing two operator
bits turns the neutral SAT residual into constant zero. LEMMA-009 nevertheless
shows that a one-gate selector can place an arbitrary hard core next to a zero
cofactor without losing that core in the hard column. The full four-cofactor
operator-bit table is the next object under audit; GATE-004F remains open.

The ninth cycle computes that table exactly: one operator setting leaves SAT
and the other three give zero for every nonempty suffix. LEMMA-010 shows that a
three-gate one-hot selector realizes the complete pattern around any hard core.
Constant-width parser windows are therefore closed as a generic collision
source; the next GATE-004F attack moves to nonlocal prefix residuals.

The tenth cycle opens that nonlocal route. ENC-007 gives equal-length prefixes
for SAT conditioned on variable identifier 1 being false or true, whose OR is
exactly SAT. GATE-004G asks for a shared two-output quotient smaller than the
single parent circuit by `Omega(n^delta)`; this would directly yield GATE-004.
LEMMA-011 shows that branch distinctness, disjointness, and union alone do not
provide the gap, so the remaining obligation is explicitly SAT-internal.

The eleventh cycle closes a quantitative loophole in that route. LEMMA-012
shows that two restricted copies begin at `2S`; within-branch losses plus
cross-copy sharing must exceed the entire `S` duplication term before any
lower-bound surplus exists. Separately simplifying and ORing the branches is
therefore recorded as a no-go rather than a recurrence.

The twelfth cycle compares this obligation with primary multi-output
literature. Identical-copy amortized complexity is trivialized by arbitrary
fanout in general circuits, while NP-hardness of multi-output minimization is
not an explicit-function size lower bound. Neither result is promoted to the
conditioned-SAT gap.

The thirteenth cycle converts the joint gap into a signed parent-label count.
Each original gate represents zero, one, or two surviving residual classes;
the exact improvement is `disappeared labels - split labels`. Condition
sensitivity can create the negative split term and therefore cannot itself be
credited as progress. The next attack seeks a SAT-specific injection from split
labels into a larger disappeared set.

The fourteenth cycle expands that attack across variable identifiers. Every
identifier of a fixed bit length supplies an equal-size conditioned pair, so
`Theta(n^c)` candidates fit at `O(log n)` prefix cost. LEMMA-014 proves that one
`Omega(n^delta)` joint gap per length would still yield a superlinear SAT lower
bound despite the logarithmic step. GATE-004H makes the required averaging
theorem explicit; candidate count alone is not treated as evidence.

The fifteenth cycle makes that warning exact. LEMMA-015 expresses the total
quotient improvement as an identifier-by-parent-label signed incidence sum.
LEMMA-016 constructs arbitrarily many equal-length candidate pairs with a
single unchanged core and zero loss, so candidate multiplicity is formally
`NO-GO`. GATE-004I is now the smallest active brick: prove a polynomial
positive average using a SAT-specific disappeared-versus-split row theorem.

The sixteenth cycle tests whether essential dependence on every prefix bit can
supply that theorem. It cannot generically: LEMMA-017 stores all such
dependence in a parity-selector shell of `O(p)` gates while exponentially many
pairs retain one shared core. At `p=O(log n)` the resulting overhead is only
logarithmic. Prefix essentiality is therefore `NO-GO`; GATE-004I remains open
and now explicitly requires distinct conditioned-SAT internal structure.

The seventeenth cycle establishes one such exact structure without promoting
it prematurely. `ENC-009` builds equal-length complete-assignment formulas on
an identifier block; the conditioned outputs realize every complementary bit
vector. This is a SAT-specific shattering theorem at the output level. The
next audit must either transfer it to the internal signed incidence surplus or
produce a shared-multiplexer no-go.

The eighteenth cycle carries out the first transfer and measures its ceiling.
LEMMA-018 converts the `2^R` columns into `R` essential suffix coordinates and
an unrestricted `R-1` binary-gate lower bound. At the explicit witness lengths
this is only `Omega(n/log n)`, and it never compares the parent with a joint
quotient. `GATE-004I-SHATTERING-SUPPORT` is therefore `NO-GO`; a successful
next brick must control conditioned internal traces rather than input support.

The nineteenth cycle checks the closest primary restriction and depth-
reduction frameworks. GKST17 requires the sufficient substitution loss that
GATE-004I is trying to prove. GKW20 reduces a size-`s` unrestricted circuit to
an OR of `2^(s/3.9)` width-16 CNFs, but LEMMA-019 proves that top-component
counting has a universal `3.9n` ceiling. Neither result is promoted to a
superlinear SAT lower bound.

The twentieth cycle rules out another accounting shortcut. LEMMA-020 separates
the global quotient of all conditioned copies from the sum of the pairwise
quotients by an exact cross-pair overlap term. A shared core can make the
global quotient look dramatically compressed while every identifier pair has
zero improvement. Global pooling is therefore `NO-GO`; GATE-004I still
requires a direct bound on the actual pairwise sum.

The twenty-first cycle finally locates polynomial structure inside the parent
circuit rather than only at its output. ENC-010 pads the witness family to
every sufficiently large length. LEMMA-021 proves that ENC-009's
complementary columns force at least `R` binary gates in the prefix-dependent
top region after every suffix-only subcomputation is collapsed to a boundary
signal. GATE-004J is the new smallest brick: prove that conditioning removes or
merges a positive power of this forced region on average, including the split-
class charge.

The twenty-second cycle tests raw semantic pigeonholing inside that region.
LEMMA-022 shows that `k=Omega(n^c)` boundary signals admit a double-exponential
universe of residual functions, vastly more than the two copies of any
polynomial-size region. Region size plus boundary arity cannot force even one
collision. This route is `NO-GO`; the next transfer must prove that SAT's
actual gate traces occupy a much smaller structured family.

The twenty-third cycle makes the missing trace statement exact. LEMMA-023
proves that prefix-independent labels contribute at most one class each, so a
pair's genuine improvement is at least `P-|T|`, where `P` is the number of
prefix-dependent parent labels and `T` their distinct active residual traces.
GATE-004K is now the smallest brick: prove a polynomial positive average of
this deficit for minimum SAT circuits.

The twenty-fourth cycle removes the last representative choice from that
quantity. LEMMA-024 proves `P-|T|=z-t+kappa`: disappeared dependent labels
minus split labels, plus cross-label collisions. GATE-004L is the new smallest
brick and deliberately asks for a positive average of the conservative
`z-t` term alone.

The twenty-fifth cycle stress-tests that conservative score. LEMMA-025 shows
that even NOT chains preserve SAT exactly while making `z-t` arbitrarily
negative; the omitted cross-label collision term compensates and the chain
vanishes in the quotient. Semantics alone is therefore `NO-GO`. Any proof of
GATE-004L must use minimum-circuit optimality quantitatively or restore
`kappa`.

The twenty-sixth cycle also tests generic minimum-circuit optimality. An
explicit five-input function has a provably minimum five-gate circuit with
distinct active cofactors but exactly `z=t=1`. Minimality plus one cofactor pair
is therefore `NO-GO`; a GATE-004L proof must exploit SAT's relations across the
entire identifier block.

The twenty-seventh cycle records a mandatory SAT-specific negative term.
LEMMA-027 proves that the output label splits into two active distinct
conditioned-SAT functions for every identifier, contributing `-|J|` to the
aggregate. Any GATE-004L proof must first pay this output charge and all other
split labels before producing a polynomial reserve.

The twenty-eighth cycle explores a sharper INDEX-style embedding without
promoting finite evidence. A deterministic exhaustive search finds no
equal-length `x_1`/`NOT x_1` encodings at Hamming distance one through length
31; the first distance-two pair is at length 15. The result is labeled
`NUMERICAL` and cannot close the coordinate-subcube question.

The twenty-ninth cycle proves the underlying parity invariant. Formula-code
weight parity excludes every one-bit pair with fixed leaf data, globally.
More importantly, ENC-012 proves that the existing assignment witnesses
already form an exact affine subspace with independent disjoint directions;
conditioned SAT realizes complementary INDEX on that subspace. This strengthens
the SAT-specific input to GATE-004L but does not itself imply gate loss.

The thirtieth cycle tests that last implication. LEMMA-028 gives an explicit
total bounded-fan-in extension of every affine complementary-INDEX table using
at most `2Rp+3R+p-1` gates. With the exact conditioned-prefix width this is
`O(R log R)`, and is `o(n)` for the witness scale `R=Theta(n^c)`, `c<1`.
Affine geometry and table values alone are therefore `NO-GO`; the active
route must use SAT's off-table semantics, a minimum-circuit consequence tied
to them, or collision structure.

The thirty-first cycle restores collision structure that the prior accounting
discarded. LEMMA-029 proves the exact identity
`S-q=alpha+z-t+kappa+lambda`, where `alpha` measures loss inside the stable
prefix-independent core and `lambda` measures collisions between dependent
residuals and that core. The earlier minimum-circuit counterexample has
`lambda=2`, so its genuine quotient loss was hidden rather than absent.
GATE-004M is now the smallest active brick and retains `lambda`. Its first
output-only attack is `NO-GO`: LEMMA-030 realizes two active output cofactors
with every gate prefix-dependent and hence `lambda=0`. A proof must exploit
minimum SAT structure across the identifier block.

The thirty-second cycle checks whether LEMMA-021's large suffix boundary can
force the new `lambda` term. LEMMA-031 gives a stronger counterexample than a
single output pair: it realizes the full affine complementary-INDEX table with
distinct active two-input-AND cofactors and `4R` raw suffix-boundary inputs,
yet every gate is prefix-dependent. Thus `I=lambda_j=0` for every pair.
Boundary-signal abundance alone is `NO-GO`; the surviving GATE-004M attack must
use minimum SAT factorization tied to off-table values or the other exact
surplus terms.

The thirty-third cycle resolves the auxiliary-leaf one-bit loophole
constructively. ENC-013 gives exact `x_j`/`NOT x_j` formulas whose encodings
differ in one bit for half of every identifier bit-length block. The
equivalence is pointwise, so the auxiliary identifier may occur in the suffix;
the resulting conditioned-SAT prefixes are genuinely adjacent and retain an
`Omega(n^c)` family. GATE-004N is now the smallest active brick. Its first
generic attack is `NO-GO`: LEMMA-032 proves that a minimum circuit for
`s XOR G` loses at most four gates under adjacent complementary cofactors,
independent of the shared hard-core complexity. The next proof must use the
whole SAT-specific edge family and off-edge semantics.

The thirty-fourth cycle determines that edge family's full geometry. ENC-014
proves that all pairs flip the same coordinate `3L+10` and that their contexts
form an affine cube with disjoint weight-three directions. LEMMA-033 shows
that influence along the shared edge direction still fits in a four-gate XOR
shell, so direction sensitivity alone is `NO-GO`. LEMMA-034 then isolates the
structure the shell cannot hide: after either polarity is fixed, at least
`2^(L-2)` parent binary-gate traces depend on the identifier context.
GATE-004O is now the smallest active brick and asks whether complete context
restriction eliminates a positive power of that region on average.

The thirty-fifth cycle stress-tests that last inference against global
minimality. LEMMA-035 constructs a provably minimum `m`-gate circuit in which
every gate depends on the context bit, yet the exact joint quotient has
`2m-3` active classes and signed loss `3-m`. Context-region size plus minimum
parent size is therefore `NO-GO`; GATE-004O must use SAT's simultaneous
`2^R` assignment-column shattering, not gatewise context dependence alone.

The thirty-sixth cycle adds that shattering and finds the next exact boundary.
LEMMA-036 constructs a globally minimum circuit with parallel adjacent pairs,
one common branch union, all `2^R` output columns across `R` contexts, and every
gate context-dependent; its per-pair quotient loss is nevertheless
`2R-m+2`, arbitrarily negative for large `m`. These contexts are one-hot in
`R` coordinates. GATE-004P is now the smallest active brick and isolates the
remaining SAT feature: the same `R` contexts exhaust every assignment of only
`log_2 R` context bits under ENC-014's affine embedding.

The thirty-seventh cycle falsifies that compressed generic gate as well.
LEMMA-037 proves the exact minimum-size identity `C(f AND z)=C(f)+1` for a
fresh input. LEMMA-038 uses it to append a minimum conjunctive tail to an
XNOR-INDEX base. The construction satisfies the full compressed cube, common
union, exact shattering, ambient minimality, and `U>=R`, but every quotient loss
is at most `K-m` and becomes negative. GATE-004P is now `NO-GO`. GATE-004Q is
the smallest active brick and explicitly requires the full SAT-gamma behavior
outside ENC-014's affine cube; its first audit is the one-bit off-cube halo.

The thirty-eighth cycle completes that halo audit. ENC-015 proves that all six
single-occurrence context flips remain valid formula prefixes and classifies
their exact semantics: two neutral duplicates, neighboring negative
conditioning, an exact negative-conditioned union, and two mixed positive
unions involving the auxiliary identifier. LEMMA-039 shows that neutral row
duplication alone preserves exact minimum circuit size and can be implemented
without any gate depending on the flipped coordinate, yielding NG-037. The
active GATE-004Q attack now targets the simultaneous mixed-halo union network.

The thirty-ninth cycle stress-tests that entire network. LEMMA-040 constructs
one total function on three context copies that realizes all six pointwise
ENC-015 cases at every radius-one neighbor, while an exact-minimum fresh tail
still makes every joint quotient retain at least `2m` classes and gives loss
at most `K_d-m`. The complete radius-one schema is therefore `NO-GO` as a
generic principle. GATE-004R is the new smallest brick: it asks for the loss
theorem under exact SAT-gamma agreement on the full radius-two prefix
cylinder, beginning with a collision-aware classification of all two-bit
mutations.

The fortieth cycle discovers that the radius-two context analysis closes into
a much larger exact object. ENC-016 independently varies all three repeated
context blocks and polarity, producing a full affine cube of valid prefixes
with two closed-form SAT conditions. LEMMA-041 reproduces this entire
pointwise schema in an arbitrary total function; the exact-minimum fresh tail
still yields loss at most `K_d-m`. Thus every-radius context-coordinate
semantics are `NO-GO` when used only pointwise. GATE-004S is the new smallest
brick and requires exact SAT-gamma residual agreement across the whole
expanded cube and every suffix formula. GATE-004R remains open for
non-context radius-two mutations.

The forty-first cycle completes the expanded output-incidence audit. ENC-017
classifies every equality and multiplicity among the `2R^3` rows, yielding
exactly `(4R^3-7R^2+7R)/2` distinct sufficiently-long SAT residuals.
LEMMA-042 shows that this entire static table survives the fresh-tail
counterexample, so output incidence alone is `NO-GO`. ENC-018 isolates the
next stronger SAT feature: suffix formulas represent sets of assignments, and
the diagonal conditioned pairs realize `3^R` compact ternary patterns where
either or both polarities may be satisfiable. GATE-004T now asks whether this
multi-witness column structure forces diagonal quotient loss.

The forty-second cycle falsifies that gate. LEMMA-043 uses two allowance bits
per condition variable to encode product domains. Singleton domains preserve
the exact expanded incidence, while zero-only, one-only, and both-valued
domains realize all `3^R` ternary columns. The diagonal union is common, yet an
exact-minimum fresh tail again gives loss at most `K_d-m`; GATE-004T is
`NO-GO`. GATE-004U is the next brick and fixes the actual padded DNF suffix
strings and their formula-OR composition, rather than merely requiring that
the corresponding output columns exist.

The forty-third cycle audits that syntax placement. ENC-019 gives an exact
common-outer double-NOT padding whose witnesses all lie in a raw
codimension-`m` suffix face. LEMMA-044 proves a general obstruction: those
fixed-one raw coordinates can serve as genuinely fresh conjunctive circuit
inputs off the witness face, giving exact size `K+m`, at least `2m` quotient
classes, and loss at most `K-m`. Common outer padding is therefore `NO-GO`.
GATE-004U remains open only because its full DNF set includes near-boundary
encodings with constant padding overhead; the active audit now requires a
padding-dense witness family with no growing common coordinate block.

The forty-fourth cycle builds that family. ENC-020 uses `O(P)` exact neutral
contexts to vary both bit values at every one of `P` outer padding
coordinates while preserving validity and satisfiability for every source
string. LEMMA-045 consequently rules out every nonempty fresh tail made from
raw padding-coordinate literals, so that extension of LEMMA-044 is `NO-GO`.
This does not prove GATE-004U: the next attack is to characterize common
non-coordinate predicates, beginning with recognizers for the neutral-context
language, and to audit whether they have any exact additive minimum-circuit
cost.

The forty-fifth cycle shows that coordinate density is only one-wise.
ENC-021 pairs the two halves of the outer padding and obtains `P/2` disjoint
clauses `z_i OR z_{i+P/2}` that are one on every ENC-020 context. LEMMA-046
proves the exact identity `C(H AND W_P)=C(H)+P`; the displayed minimum circuit
has at least `3P/2` diagonal quotient classes and loss at most `K-P/2`.
Therefore ENC-020-only forcing is `NO-GO`. Full GATE-004U remains open, and
the next syntax audit requires at least pairwise zero coverage across every
large candidate padding region.

The forty-sixth cycle supplies that defense. ENC-022 uses one or two exact
neutral blocks from a fixed ten-block alphabet to put simultaneous zeros on
every outer coordinate pair except four root-token pairs. LEMMA-047 proves
that those exceptions have matching number two, so no growing disjoint
positive two-clause tail survives after these witnesses are required. This
repairs the exact cycle-045 counterexample but does not prove GATE-004U; the
next audit concerns overlapping clauses, higher-width predicates, and the
complete DNF syntax set.

The forty-seventh cycle shows that the repair is width-specific. ENC-023
partitions the padding into distant triples; every one/two-block context makes
each corresponding width-three clause true. LEMMA-048 proves generally that
`m` disjoint width-`w` clauses have exact additive cost `wm` and expose at
least `(w+1)m` quotient classes. At width three this restores loss at most
`K-P/3`, so ENC-022-only forcing is `NO-GO`. The next construction target is
triple-zero density, alongside an audit of the obstruction at growing clause
width.

The forty-eighth cycle closes the entire fixed-block ladder. ENC-024 and
LEMMA-049 show that `b` zero blocks of length at most `D` leave
`m=floor(P/(b+1))` disjoint common clauses of width `b+1` whenever `m>=D`.
The extension has exact loss at most `K-m`, so every regime with `m>K` is
`NO-GO`, including every fixed block count. The next audit must use a
sufficiently dense unbounded-block family or the broader variation of full
DNF syntax.

The forty-ninth cycle closes dense use of a finite neutral alphabet. ENC-025
and LEMMA-050 show that maximum zero-run length `rho` leaves
`floor(P/(rho+1))` disjoint common window clauses and exact loss at most
`K-floor(P/(rho+1))`. The ten-block alphabet has `rho=7` even with a linear
number of blocks, so dense block count alone is `NO-GO`. The next audit must
permit zero runs on the `P/K` scale or use the full variable-core DNF syntax.

The fiftieth cycle constructs those runs explicitly. ENC-026 and LEMMA-051
use identifier `2^(rho-3)` to produce an exact neutral block of length
`4rho`, maximum zero run `rho`, and a four-aligned sweep of interior windows.
The single-block forcing attempt is nevertheless `NO-GO`: all zeros remain in
one interval, so half-separated width-two clauses restore loss at most
`K-floor(P/2)`. The next construction must combine dense independent blocks
with long runs and retain coordinate density.

The fifty-first cycle builds that combination. ENC-027 and LEMMA-052 use
independent length-`4rho` slots containing both coordinate-dense short options
and the tunable long block. Every established sparse-cover tail has at most
`6s` clauses and the run-window tail fewer than `4s`; with
`s=floor((R-1)/8)`, both lie below the unavoidable base floor `K>=R-1`.
This proves no loss. GATE-004V is the new smallest sufficient brick and asks
whether exact agreement on the full slot product forces polynomial diagonal
rigidity.

The fifty-second cycle closes the first GATE-004V predicate class. ENC-028
and LEMMA-053 show that the all-long product has exactly `6s` one bits, so
every disjoint positive-clause family common to the product has at most `6s`
members. Because `6s<K`, the exact LEMMA-048 certificate cannot become
negative at any clause width. This is `NO-GO` only for that counterexample
route; signed, overlapping, and non-clausal predicates remain active.

The fifty-third cycle audits the first signed extension. LEMMA-054 proves
that the same fresh negated literal costs two gates over base `x` but only one
additional gate over base `NOT x`, where De Morgan's law shares output
polarity. Therefore a fixed NOT charge cannot extend LEMMA-048 to signed
clauses. This is a scoped `NO-GO` for naive additive accounting; complement-
sensitive signed predicates, overlap, and GATE-004V remain open.

The fifty-fourth cycle proves the first complement-sensitive exact theorem.
LEMMA-055 shows that if `C(NOT H)=C(H)-1`, then conjoining `m` fresh negative
literals has exact cost `C(H)+m` and its displayed minimum circuit supplies at
least `2m+2` paired-row tail classes. LEMMA-052 coordinate density, however,
makes the number of common positive or negative unit literals exactly zero.
This closes only the unit signed route; mixed clauses of width at least two
are now active.

The fifty-fifth cycle finds that mixed clauses are not sparse. ENC-029 and
LEMMA-056 construct at least `(2rho-4)s=P/2-4s` disjoint common implications;
product independence confines every common mixed two-clause to one slot.
LEMMA-057 proves the exact bracket `K+2m<=C(F)<=K+3m`. The displayed upper
circuit has at least `4m` quotient classes, but ordinary essential-variable
restriction misses its minimality by exactly `m` gates. GATE-004W is the
active falsification audit; no negative loss is yet proved.

The fifty-sixth cycle audits the standalone implication predicate before any
base direct sum. LEMMA-058 combines the `2m-1` binary connectivity floor with
Markov's `ceil(log_2(m+1))` NOT floor, proving exact sizes two and five for one
and two implication pairs. For growing `m`, the combined certificate remains
`m-ceil(log_2(m+1))` below the displayed `3m-1` circuit. This is a quantitative
`NO-GO` for support-plus-inversion counting, not evidence of compression.

The fifty-seventh cycle resolves the seven-versus-eight gate question without
numerical synthesis. LEMMA-059 proves that equality in the binary connectivity
floor forces the output cone to be a formula; formula inversion complexity
then forces one NOT per implication decrease. This proves
`C(W_m)=3m-1` for `m=1,2,3,4`. From `m=5` onward, the refined dichotomy still
has gap `m-1-ceil(log_2(m+1))`, so the asymptotic GATE-004W direct sum remains
open.

The fifty-eighth cycle takes the constructive branch instead of assuming that
direct sum. ENC-030 and LEMMA-060 add every placement of `A_7,...,A_12` to a
slot, confining all common mixed binary clauses to twelve-coordinate boundary
regions while retaining `A_rho` and its tunable run. With
`s=floor((R-1)/24)`, any disjoint signed binary family has at most `18s<K`
members. GATE-004X is the new smallest positive brick; signed clauses of width
at least three, overlap, and nonclausal predicates remain open.

The fifty-ninth cycle shows that binary sparsity does not survive the next
width. ENC-031 and LEMMA-061 select one common signed triple in every aligned
four-bit chunk, giving `rho*s=P/4` disjoint clauses. Product localization
proves that cross-slot triples contain common binary subclauses, so the new
obstruction is genuinely within-slot. LEMMA-062 gives
`K+3m<=C(F)<=K+5m`; its displayed circuit has `6m` quotient classes, but the
lower certificate is short by `2m`. GATE-004Y is the active falsification
audit. No GATE-004X counterexample or positive circuit loss is proved.

The sixtieth cycle immediately rejects the clausewise minimality route.
LEMMA-063 writes each surviving clause as the complement of a three-literal
violation term and shares one outer NOT across their DNF. This computes the
standalone conjunction in `4m` gates and the base extension in at most
`K+4m+1`, strictly below `K+5m` for `m>=2`. The compressed displayed circuit
has only `4m+2` tail/output quotient classes and loss `K-1`.
GATE-004Y-CLAUSEWISE-MINIMALITY is therefore `NO-GO`; the surviving gate asks
for a representation-independent minimum-circuit quotient surplus.

The sixty-first cycle finds the best current local factorization. Every
surviving clause is `p OR NOT(u AND v)`, requiring three rather than four
gates. LEMMA-064 gives standalone upper bound `4m-1`, base-extension bracket
`K+3m<=C(F)<=K+4m`, and `5m` displayed paired-row tail classes. If the upper
circuit is minimum, its loss is `K-m`; the essential-restriction lower bound
is short by exactly that same `m`. GATE-004Z is the active concrete
falsification audit. No minimality or quotient-survival theorem is claimed.

The sixty-second cycle audits the standalone factorized predicate. LEMMA-065
proves its inversion decrease parameter is exactly `m`. Essential dependence
forces `3m-1` binary gates; equality forces a formula and hence `m` NOT gates.
Together with Markov's general inversion bound, this gives
`C(W_m)>=min(4m-1,3m+ceil(log_2(m+1)))` and exact size `4m-1` for
`m=1,2,3,4`. From `m=5`, the remaining gap is
`m-1-ceil(log_2(m+1))`. The formula-boundary route is therefore `NO-GO` for
the growing regime, and it supplies no base additivity.

The sixty-third cycle proves that this repeated gap is structural. LEMMA-066
shows that replacing each implication input `t_i` by `u_i AND v_i` raises
exact circuit size by exactly `m`, over any disjoint nonconstant base. A
minimum implication circuit lifts to a minimum signed-triple circuit, and the
derived AND gates add exactly `m` quotient classes. Thus signed-triple
displayed minimality is the unresolved implication tail plus a settled layer,
not an independent route. GATE-004AA is the new constructive brick: seek a
fixed exact neutral-block alphabet whose translations make every disjoint
common signed clause family through width three constant per slot.

The sixty-fourth cycle refutes that one-block repair without enumerating the
alphabet. LEMMA-067 uses `floor(4rho/3)` distant disjoint triples. Any bounded
block changes at most one coordinate of such a triple, so four patterns with
at least two zeros are absent from all bounded options; the sole `A_rho`
option can add only one. A common signed triple therefore survives on every
group for every fixed alphabet. GATE-004AA is `NO-GO`. GATE-004AB is the new
constructive brick and permits two independently translated neutral blocks
per option, the first geometry not covered by this counting obstruction.

The sixty-fifth cycle verifies that the two-block threshold genuinely removes
the canonical distant obstruction. ENC-032 and LEMMA-068 use exact ENC-022
contexts to realize `111`, all one-zero patterns, and all two-zero patterns on
each distant triple. The six-one option `A_rho` supplies `000` on all but at
most six disjoint triples. Hence at least `floor(4rho/3)-6` triples realize all
eight patterns and support no common signed clause. GATE-004AB remains open
because arbitrary local and intermediate-span triple matchings are not yet
bounded.

The sixty-sixth cycle isolates and repairs the aligned local defect. The ten
ENC-022 blocks omit `101` and `110` on every aligned chunk, so LEMMA-069 gives
`rho` common triples and closes that alphabet as `NO-GO`. LEMMA-070 adds exact
identifier-10/12 contexts whose terminal chunks are `1010` and `1100`; their
translations complete all eight patterns on every aligned chunk except the
first five. Nonaligned local and intermediate-span triples remain active.

The sixty-seventh cycle closes the full two-block construction. Identifiers
1 through 68 have maximum block length 36. Cycle 091 corrects its finite
reduction to a 22,500-type translation
certificate proves that two blocks realize every triple pattern except
`000` in the interior; `A_rho` supplies `000` away from its six one bits.
Every common signed clause through width three therefore meets a 78-coordinate
hitting set, proving GATE-004AB. GATE-004AC is the new positive brick, with
width-four, overlapping, and nonclausal predicates still open.

The sixty-eighth cycle finds the next-width ladder obstruction. LEMMA-072
uses distant quadruples: two bounded blocks can zero at most two coordinates,
so five patterns with at least three zeros are absent and the sole long option
can add only one. A linear common signed width-four packing survives.
GATE-004AC-WIDTH3-ONLY is `NO-GO`; GATE-004AD opens the three-block repair.

The sixty-ninth cycle audits the first three-block alphabet exhaustively and
finds a stable failure. LEMMA-073 proves that identifiers 1 through 68 cannot
realize `1110` on offsets `{0,21,25,26}` with three nonoverlapping blocks.
Translations spaced by eight are disjoint, and the six-one long option repairs
at most two, leaving a linear width-four packing. The identifier-68
specialization is `NO-GO`; GATE-004AD remains open for a richer alphabet.

The seventieth cycle tests that enrichment and finds a sharper boundary. A
targeted length-48 alphabet fails on 35 of 530,604 reduced quartet types.
LEMMA-074 then audits the complete identifier range 1 through 1,023 and proves
that `1110` is still absent on offsets `{0,5,9,10}`. Its twelve-spaced
translations leave a linear common width-four packing, so every length-48
specialization is `NO-GO`. Explicit length-52-or-longer identifiers repair
the representatives; GATE-004AD therefore advances to a larger-bound audit
without any circuit or terminal claim.

The seventy-first cycle proposed the width-four witness construction. A first
86-identifier length-68 repair set passes sampling but fails on six of
1,431,644 reduced types, recorded as a subset-specific `NO-GO`. Six explicit
same-bound identifiers repair those types. The original LEMMA-075 audit
verified 1,431,644 types, but Cycle 091 shows that its one-block-length gap
reduction does not preserve nonoverlap in general. The corrected safe domain
has 10,742,476 types. LEMMA-075 and GATE-004AD are therefore `EXPLORATORY`;
the 142-coordinate hitting set is not claimed. GATE-004AE remains contingent
on that witness premise, with no circuit or terminal progress inferred.

The seventy-second cycle exposes the next-width ladder without promoting a
circuit claim. LEMMA-076 proves that three bounded blocks plus one exceptional
option retain `floor(N/5)` disjoint common signed width-five clauses: ordinary
options omit six four-or-five-zero patterns on every distant quintuple, and
the exception repairs at most one. GATE-004AE-WIDTH4-ONLY is `NO-GO`.
GATE-004AE itself remains open because tail cost and quotient survival are not
proved. GATE-004AF opens the four-block width-five construction audit.

The seventy-third cycle tests the width-four alphabet at that new threshold.
Two independent exact interval DPs agree that four blocks omit `11110` on
offsets `{0,4,7,9,10}`. Twelve-spaced translations are disjoint, and `A_rho`
repairs at most one because the pattern consumes four of its six one bits.
LEMMA-077 gives an `N/12-O(1)` common signed width-five packing, and the
LEMMA-075-alphabet specialization is `NO-GO`. GATE-004AF remains open for a
richer fixed alphabet; no circuit or terminal result is inferred.

The seventy-fourth cycle tests the smallest same-bound repair. Identifiers
1,089 and 1,098 realize the two masks missing from LEMMA-077, but an exhaustive
gap-at-most-20 audit finds 1,787 failures among 640,000 types. Both exact DPs
confirm that `(70,71,76,77,80)` omits only mask 8. Twelve-spaced translations
leave an `N/12-O(1)` common width-five packing after at most one `A_rho`
repair. The 94-identifier specialization is `NO-GO`; the full 101-million-type
GATE-004AF audit remains open and no circuit conclusion is drawn.

The seventy-fifth cycle replaces ad hoc patches by an exact covering basis.
LEMMA-079 constructs 318 explicit 15-bit identifiers covering all 64,064
five-column patterns on their fourteen free bits. Adding them reduces the
gap-at-most-20 failure count from 1,787 to 497, but LEMMA-080 finds a
token-boundary mask-16 obstruction on offsets `{0,1,10,15,16}` and an
`N/20-O(1)` common packing. Free-bit coverage alone is `NO-GO`; the next
GATE-004AF construction must cover phases of the complete neutral-block word.

The seventy-sixth cycle closes the entire length-68 alphabet. LEMMA-081 builds
2,066 projection-complete representatives across all fifteen identifier
lengths and proves they capture every five-coordinate behavior of identifiers
1 through 32,767. LEMMA-082 checks both that basis and the literal full range:
mask 16 still fails on offsets `{0,1,10,15,16}`, leaving an `N/20-O(1)` common
packing. Every length-at-most-68 specialization is `NO-GO`; GATE-004AF now
requires blocks of length at least 72. No circuit or terminal claim follows.

The seventy-seventh cycle locates the next exact boundary. LEMMA-083 audits
all identifiers 1 through 65,535 and an independent 2,437-row
projection-complete basis; both retain mask 16 on the stable quintuple, so
every length-at-most-72 specialization is `NO-GO`. LEMMA-084 finds the first
repair at length 76: `01 T_98370` aligned at start 48 realizes the missing
mask. This repairs one type only; the bound-76 GATE-004AF audit remains open.

The seventy-eighth cycle tests that single repair globally enough to falsify
it. The exact gap-at-most-20 audit retains 494 failures; LEMMA-085 isolates a
shifted mask-16 obstruction on offsets `{0,2,10,15,16}` and an `N/20-O(1)`
packing. The one-identifier repair is `NO-GO`. LEMMA-086 constructs 2,873
projection-complete representatives for every standard block through length
76. A 5,000-type sample finds no failure for that complete basis, but this is
only EXPLORATORY; the exhaustive or analytic bound-76 audit remains open.

The seventy-ninth cycle resolves that uncertainty negatively. LEMMA-087 proves
that a symbolic fixed-token/free-column oracle is exactly equivalent to literal
identifier enumeration. Its complete bound-76 local audit finds 195 failures.
LEMMA-088 and the direct full-range DP agree that mask 16 is absent on offsets
`{0,4,12,17,18}`, leaving an `N/20-O(1)` packing. Every length-at-most-76
specialization is `NO-GO`; GATE-004AF now requires block length at least 80.

The eightieth cycle closes the next exact boundary. The symbolic oracle and
literal enumeration of all 262,143 identifiers agree that length at most 80
still omits only mask 16 on the shifted offsets `{0,4,12,17,18}`. LEMMA-089
therefore retains the `N/20-O(1)` packing and makes the complete length-80
specialization `NO-GO`. LEMMA-090 sharply repairs that representative at
length 84 with identifier 278,594 placed at offset 60. This is a local repair,
not width-five universality; the complete length-84 type audit is next.

The eighty-first cycle executes that full local audit. Across all 640,000
gap-at-most-20 types, the complete length-84 alphabet leaves 122 failures,
partitioned `30,31,31,30` by residue. The symbolic oracle and a literal scan of
all 524,287 identifiers independently agree that `(84,92,100,103,104)` omits
only mask 8. LEMMA-091 translates it to an `N/24-O(1)` packing, so the complete
length-84 specialization is `NO-GO`; length at least 88 is now required.

The eighty-second cycle locates the next sharp local repair. Identifier
526,344 gives a length-88 block which, at offset 20 with all-one surrounding
padding, realizes the missing mask 8 on the shifted LEMMA-091 representative.
LEMMA-092 records the exact bit-string witness. The complete length-88 audit,
not this single repaired type, is the next operational gate.

The eighty-third cycle completes that audit and finds 111 failures, partitioned
`21,30,30,30` by residue. Symbolic and literal DPs over all 1,048,575
identifiers agree that `(88,96,104,109,110)` omits only mask 16. LEMMA-093
retains an `N/24-O(1)` packing, making complete length 88 `NO-GO`.

The eighty-fourth cycle follows the counterexample rather than rerunning the
whole local domain. The exact symbolic oracle proves that the shifted mask-16
type survives every identifier through block lengths 92 and 96. LEMMA-094
therefore closes all length-at-most-96 specializations with the same packing.

The eighty-fifth cycle finds the sharp next repair: identifier 4,210,754 gives
a length-100 block reading `11110` on the shifted representative. LEMMA-095 is
again only a local repair. The complete length-100 audit is next.

The eighty-sixth cycle completes that audit. The exact 640,000-type sweep
finds 46 failures, partitioned `10,12,12,12` by residue. On
`(100,112,120,123,124)`, a separately derived 851-identifier basis has zero
selected-projection coverage failures, and its literal DP agrees with the
symbolic oracle that only mask 8 is absent. LEMMA-096 retains an
`N/28-O(1)` packing, so complete length 100 is `NO-GO`.

The eighty-seventh cycle finds the next local repair. Identifier 8,390,664
gives a length-104 block reading `11101` on the shifted representative.
LEMMA-097 does not establish global coverage; the complete length-104 audit is
the next operational gate.

The eighty-eighth cycle executes that audit and finds 44 failures, partitioned
`8,12,12,12` by residue. A 985-identifier projection-complete basis and the
symbolic oracle agree that `(104,116,124,129,130)` omits only mask 16.
LEMMA-098 retains an `N/28-O(1)` packing, making complete length 104 `NO-GO`.

The eighty-ninth cycle follows the exact obstruction through complete lengths
108 and 112. At length 112, a 1,232-identifier basis independently confirms
the symbolic result. LEMMA-099 closes all length-at-most-112 specializations.

The ninetieth cycle locates the next local repair: identifier 67,125,314 gives
a length-116 block reading `11110` on the shifted representative. LEMMA-100 is
not global coverage. A gap-at-most-20 query is only a witness search; an all-
type universality audit needs the corrected reduction described next.

The ninety-first cycle audits the finite gap reduction itself. LEMMA-101 gives
an exact aligned length-eight counterexample to truncating at one block length;
that proof method is `NO-GO`. LEMMA-102 proves the safe threshold `2B`, making
the geometry-only length-116 quintet domain `4*235^4=12,199,202,500` types.
The corrected 22,500-type LEMMA-071 audit has zero failures, so width-three
sparsity remains proved. The corrected LEMMA-075 audit is not run locally and
width-four sparsity reopens. A separate 1,792-type length-116 targeted query
found no obstruction and is labeled only `NUMERICAL`.

The ninety-second cycle makes the corrected width-four gate externally
executable without weakening it. A fixed 556-shard contract covers exactly
all `10,742,476` safe quartet types, seals each alphabet/configuration/result,
and fails closed on gaps, overlaps, tampering, or incomplete coverage. Tiny
local contract tests pass; the production sweep is not run on Windows.
GATE-004AD-CORRECTED-FULL-AUDIT is the next falsifiable brick.

The ninety-third cycle proves a sharper SAT-specific reduction. Exact zero
overhangs by residue give phase caps `(135,134,133,132)`, including blocks
whose selected zero lies away from the gap boundary. LEMMA-103 reduces the
external domain to 9,515,749 types. The updated fail-closed contract has 534
shards of 17,622–18,021 types; no production shard is run on Windows and the
mathematical gate remains `EXPLORATORY`.

The ninety-fourth cycle closes the reopened width-four theorem analytically.
LEMMA-104 proves every singleton-zero pair pattern needs one block; LEMMA-105
proves every full-zero triple needs at most three. LEMMA-106 then covers every
quartet with a gap at least 72 by independent `1+3` or `2+2` components within
the same three-block budget. All remaining types are exactly the historical
`4*71^3=1,431,644` zero-failure certificate. LEMMA-075, GATE-004AD, and the
corrected full-audit gate return explicitly to `PROVED`; the 9,515,749-type
production sweep is retired, not silently assumed.

The ninety-fifth cycle attacks GATE-004AE rather than extrapolating from the
restored witness theorem. LEMMA-108 proves that every distant quintuple
retains a common signed width-five clause with exactly four positive literals
and one negative literal. LEMMA-107 gives the exact bracket
`K+5m<=C(F)<=K+6m`; the displayed upper circuit has `7m` tail classes, but
essential restrictions miss minimality by exactly `m`. GATE-004AG isolates
the required minimality-or-quotient theorem, while the restriction-only route
is `NO-GO`. GATE-004AE and every terminal bridge remain `EXPLORATORY`.

## Honest progress estimates

| Measure | Estimate | Meaning |
|---|---:|---|
| Infrastructure maturity | 93% | Repository, corrected target/bridge labels, exact bit-level SAT language, broad encoding and barrier audits, exact symbolic/literal finite verifiers, ledgers, model-card checker, manifest, and cold-clone evidence exist. Cycles 091–094 repair the width-four proof; Cycle 095 isolates the next fixed-sign tail and its exact one-gate-per-clause proof gap. Formal foundations and broader independent review remain incomplete. |
| Formally closed proof chain | 0% | No terminal-critical implication has been proof-assistant verified. |
| Real progress toward P vs NP | 0.00% | Three-block contexts have an audited width-four sparsity proof and a fixed-sign width-five obstruction, but GATE-004AG/AE minimum-circuit rigidity, overlapping/nonclausal predicates, and every unrestricted SAT circuit lower bound remain unresolved. |

These values are judgment calls, not metrics derived from files, tests, commits,
or special cases.

## Repository map

| Path | Purpose |
|---|---|
| `docs/problem-statement.md` | Exact standard target and encodings |
| `docs/sat-encoding.md` | Bit-level total SAT language used by every fine-grained claim |
| `docs/vertical-map.md` | Terminal-to-brick dependency map |
| `docs/barrier-audit.md` | Relativization, natural proofs, algebrization, diagonalization, circuit, uniformity, and reduction constraints |
| `docs/bridge-audit.md` | SAT/Circuit-SAT algorithm-to-lower-bound bridges and their terminal gaps |
| `docs/verification-ledger.md` | Result status and audit evidence |
| `docs/no-go-ledger.md` | Structural and quantitative failed routes |
| `docs/source-citations/` | Primary-source claim notes |
| `proofs/` | Human-readable gate statements and proof attempts |
| `formal/` | Proof-assistant boundary and future kernel-checked work |
| `verification/` | Machine-readable claims and deterministic audits |
| `experiments/` | Non-proof computational work, always separately labeled |
| `artifacts/` | Reproducibility manifests and auditable outputs |

Run the read-only audit with:

```powershell
python verification/audit.py
python -m unittest discover -s verification -p 'test_*.py' -v
```

## Adversarial stop condition

If a possible full solution appears, all expansion stops. The repository moves
to the protocol in [`docs/adversarial-protocol.md`](docs/adversarial-protocol.md):
circularity, relativization, natural-proofs, algebrization, quantifiers,
uniformity, reductions, primary literature, cold-clone reproduction, and formal
critical-step checks are audited before any manuscript or success claim.
