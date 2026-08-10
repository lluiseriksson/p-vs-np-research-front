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
