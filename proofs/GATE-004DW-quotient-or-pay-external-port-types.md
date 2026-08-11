# GATE-004DW — quotient or pay external port types

**Label: EXPLORATORY**

LEMMA-233 and NG-171 show that bounded marked support does not make the
external interface finite. GATE-004DV requires a proved port reduction before
any bounded-core classification.

## Falsifiable theorem

For every fully covered marked core of size at most four or six, assign every
external port a record containing:

1. its marked source gate and old/new edge identity;
2. consumer operation and complete four-code function of every other input;
3. the downstream parent-transfer function with the port treated as a formal
   input;
4. satisfying-minor loss/contraction behavior; and
5. prior host, loss, cycle, and potential charges.

Prove an exact dichotomy:

- ports with the same record admit a size-nonincreasing merge or shared
  realization preserving the parent and not increasing `W,Q,R_0`; or
- every inequivalent record supplies a distinct minimum-cost physical payment,
  so only a bounded number remain after global deduplication.

Then classify the bounded core together with one representative per residual
record. The theorem is falsified by a refined minimum endpoint with a bounded
fully covered core, unbounded inequivalent live port records, no merge or
shared realization, insufficient physical payments, and no potential descent.

Equality of only local gate operations, satisfying rows, or selector labels is
not port equivalence. Any merge must prove complete parent-transfer equality
and preserve acyclicity and all fanouts.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with bounded marked core and complete semantic/physical port records |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple with fully covered marked support |
| Circuit size | Parent `K+2`; marked core at most four/six; residual port records must merge or pay distinctly |
| Circuit depth | Unrestricted; downstream transfer regions unbounded before quotient |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and every port occurrence audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean transfer functions, physical loss/contraction data, potentials, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, endpoint, bounded core, external port, record class, and merge candidate |
| Regime | Exact worst-case port-quotient/payment gate; not a finite enumeration claim, SAT lower bound, or terminal result |
