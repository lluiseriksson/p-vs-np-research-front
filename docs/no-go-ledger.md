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
