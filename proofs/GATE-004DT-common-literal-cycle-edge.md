# GATE-004DT-COMMON-LITERAL-CYCLE-EDGE — survival does not fix one edge

**Label: NO-GO**

Scope: from LEMMA-229's survival of one common-origin cycle coordinate in all
three satisfying minors, select a parent edge that remains literally
uncontracted in `00,01,11` and use that edge as a common physical payment or
uncrossing pivot.

LEMMA-230 gives a rank-one six-cycle whose three labeled minors contract
disjoint pairs covering every parent edge. Each minor loses two vertices and
edges by contraction, preserves rank exactly, and carries the parent cycle to
a nonzero coordinate. Nevertheless the intersection of literal uncontracted
parent-edge supports is empty.

The witness is graph-theoretic and does not assert Boolean endpoint
realizability. It refutes the deduction from cycle-space survival alone.
A valid proof must transport support through the actual contraction maps or
derive an additional endpoint restriction that rules out the covering pattern.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact rank-preserving parent/minor cycle graphs under three labeled two-edge contractions |
| Uniform/non-uniform | One finite non-uniform graph witness |
| Circuit size | Six-edge parent cycle; two contractions per labeled minor |
| Circuit depth | Graph witness; unrestricted in the target circuit |
| Fan-in | Graph theorem; target circuit AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Literal parent-edge supports, contractions, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every parent edge and each of the three displayed minor labels |
| Regime | Common-literal-edge no-go; not endpoint counterexample, SAT lower bound, or terminal result |
