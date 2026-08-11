# GATE-004DV — classify bounded contraction cores

**Label: EXPLORATORY**

LEMMA-231 leaves a common physical support gate on every long marked cycle.
LEMMA-232 and NG-170 show that loss cardinality alone leaves cores of at most
four gates in AND→OR and at most six in OR→AND.

## Falsifiable theorem

For every refined endpoint whose marked common-origin swap support is fully
covered by satisfying losses, contract all unmarked degree-two path segments
while retaining:

1. the carrier vertices `g,h`, swap gate, marked origin, and every branch or
   reconvergence port;
2. the exact labeled loss sets and contraction maps for `00,01,11`;
3. every gate's complete four-code Boolean signature and AND/OR/NOT operation;
4. all external fanout ports needed to certify the parent interface; and
5. earlier charges and `W,Q,R_0` contributions.

Prove that every resulting core with at most four marked support gates in
AND→OR or six in OR→AND either violates an exact signature/loss identity,
admits a size-nonincreasing strict potential descent, or supplies a distinct
real host. Alternatively exhibit a fully specified refined endpoint core,
which falsifies the gate.

Finite support size does not by itself bound unmarked attachments; the
contraction to ports must be proved semantics- and cost-preserving before any
finite enumeration. Abstract set systems and graph-only minors are not
admissible realizations.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with bounded marked contraction core and explicit external ports |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple with fully covered marked support |
| Circuit size | Parent `K+2`; marked core at most four gates in AND→OR or six in OR→AND; attachments unbounded until reduced |
| Circuit depth | Unrestricted before a proved port reduction |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and every external port audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean signatures, labeled loss sets, contraction maps, potentials, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, fully covered swap support, core vertex, and external port |
| Regime | Exact worst-case bounded-core classification gate; not a finite enumeration claim, SAT lower bound, or terminal result |

## Cycle-195 audit

LEMMA-233 gives a fixed marked cyclic core with arbitrarily many parent-live
external ports. Finite enumeration of only the core is NG-171. GATE-004DW
replaces that route with a complete semantic/physical port quotient or a
distinct minimum-cost payment for each inequivalent record. GATE-004DV remains
`EXPLORATORY`.
