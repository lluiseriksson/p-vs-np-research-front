# LEMMA-023 — prefix-dependent trace accounting

**Label: PROVED**

## Statement

Let an `S`-gate parent circuit have a designated prefix block. Let `P` be the
number of parent gates whose semantic gate functions depend on at least one
prefix coordinate, and let `I=S-P` be the number of prefix-independent gates.

For any pair of complete prefix restrictions, normalize the two restricted
copies semantically. Let `T` be the set of distinct active residual functions
represented by surviving copies of the `P` prefix-dependent gate labels. If
the full joint quotient has `q` active residual classes, then

`q<=I+|T|`

and therefore

`S-q>=P-|T|`.

If `a` is the number of active dependent-gate occurrences among the `2P`
copies, define eliminated occurrences `e=2P-a` and collision surplus
`h=a-|T|`. Then the same lower bound is

`S-q>=e+h-P`.

## Model card

| Field | Value |
|---|---|
| Computational model | One acyclic Boolean parent circuit; two complete prefix restrictions; exact semantic residual quotient |
| Uniform/non-uniform | Fully non-uniform semantic dependence and quotient classification |
| Circuit size | Exact lower bound `S-q>=P-|T|=e+h-P` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite residual-function set counting only |
| Asymptotic quantifiers | Every finite parent circuit, every designated prefix block, and every pair of complete prefix restrictions |
| Regime | Worst-case exact multi-output circuit computation |

## Proof

A prefix-independent parent gate has the same residual function in the two
copies. If active, its copies therefore contribute at most one joint semantic
class; if constant, input-equivalent, dead, or equal to another class, they
contribute less. All `I` independent labels together contribute at most `I`
classes.

Every remaining quotient class contains a surviving copy of a dependent label
and its residual function lies in `T`. Hence `q<=I+|T|`. Substituting
`I=S-P` gives `S-q>=P-|T|`.

Finally, `e+h-P=(2P-a)+(a-|T|)-P=P-|T|`. QED.

## Scope

The lemma is one-sided and allows `P-|T|` to be negative. To obtain positive
loss, more than the one-class-per-dependent-label baseline must disappear or
collide after all split residuals are counted. GATE-004K states the required
SAT-specific average.
