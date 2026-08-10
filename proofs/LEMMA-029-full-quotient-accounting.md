# LEMMA-029 — exact full quotient accounting

**Label: PROVED**

## Statement

Use the circuit and paired-prefix setting of LEMMA-023 and LEMMA-024. Let the
parent have `S=I+P` gates, where `I` labels are prefix-independent and `P`
labels are prefix-dependent.

After the two restrictions are jointly normalized, let:

- `A` be the set of distinct active residual functions represented by copies
  of prefix-independent labels;
- `T` be the set of distinct active residual functions represented by copies
  of prefix-dependent labels;
- `alpha=I-|A|`; and
- `lambda=|A intersect T|`.

Let `z,t,kappa` be the dependent-label quantities from LEMMA-024, and let `q`
be the gate count of the full semantic joint quotient. Then

`q=|A union T|`

and the exact identity is

`S-q=alpha+z-t+kappa+lambda`.

In particular, LEMMA-023's lower bound can be strict for two separate reasons:
prefix-independent labels may disappear or collide (`alpha>0`), and dependent
residuals may collide with the surviving prefix-independent core
(`lambda>0`).

## Model card

| Field | Value |
|---|---|
| Computational model | One acyclic Boolean parent circuit, two complete prefix restrictions, and the exact active semantic joint quotient |
| Uniform/non-uniform | Fully non-uniform semantic classification; no circuit-generation assumption |
| Circuit size | Exact identity `S-q=alpha+z-t+kappa+lambda` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the SAT application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set union and integer counting only |
| Asymptotic quantifiers | Every finite parent circuit, designated prefix block, and pair of complete prefix restrictions |
| Regime | Worst-case exact multi-output circuit computation after constants, input-equivalent functions, dead gates, and equal residual functions are normalized |

## Proof

Every active quotient gate class is represented by a surviving restricted copy
of some parent label. Prefix-independent labels supply exactly the function
set `A`, and prefix-dependent labels supply exactly `T`. Equality of residual
functions is precisely the quotient equivalence, so

`q=|A union T|=|A|+|T|-|A intersect T|`.

Substitute `S=I+P`, `alpha=I-|A|`, and `lambda=|A intersect T|`:

`S-q=alpha+(P-|T|)+lambda`.

LEMMA-024 gives `P-|T|=z-t+kappa`. Substitution proves the identity. QED.

## Audit against LEMMA-026

In LEMMA-026, the independent functions are `A={g,h}`. The dependent trace
set is `T={g,g OR h,h}`. Hence `alpha=0`, `lambda=2`, and
`z-t+kappa=0`. The parent has five gates and the joint quotient has three, so

`S-q=2=0+0+2`.

Thus the earlier minimum-circuit counterexample blocks positive `z-t`, but it
does not block actual quotient loss: that loss was hidden in dependent/core
collisions omitted from the conservative accounting.

## Scope

The identity proves no positive lower bound. It only prevents future audits
from discarding two helpful terms. GATE-004M isolates a sufficient theorem
using `lambda`; a proof may alternatively exploit `alpha` or return directly
to the exact full expression.
