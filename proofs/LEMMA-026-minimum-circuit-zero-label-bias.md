# LEMMA-026 — a minimum circuit can have zero labelwise bias

**Label: PROVED**

## Statement

Define the five-input Boolean function

`F(x,y_1,y_2,w_1,w_2)=(NOT x AND (y_1 AND y_2)) OR (w_1 AND w_2)`.

It has minimum AND/OR/NOT circuit size exactly five. Relative to the one-bit
prefix block `{x}`, a minimum five-gate circuit has three prefix-dependent
labels. Under the pair `x=0,x=1`, exactly one dependent label contributes no
active residual function and exactly one contributes two distinct active
residual functions. Therefore

`z=t=1` and `z-t=0`,

even though the two output cofactors are distinct active non-input functions.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact five-input total Boolean function and globally minimum acyclic circuit |
| Uniform/non-uniform | One finite non-uniform minimum circuit |
| Circuit size | Exactly five gates; dependent-label score exactly zero |
| Circuit depth | Three in the exhibited circuit; unrestricted in the lower bound |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One explicit finite function and its displayed complete prefix pair |
| Regime | Worst-case exact total-function computation; generic method counterexample, not SAT-gamma |

## Minimum circuit

Use the gates

1. `g=y_1 AND y_2`;
2. `h=w_1 AND w_2`;
3. `n=NOT x`;
4. `a=n AND g`;
5. `o=a OR h`.

This computes `F`. The function depends essentially on all five inputs. In the
output cone of any circuit depending on five input sources, connectedness and
the edge count from LEMMA-018 require at least four binary gates. Moreover `F`
is not monotone in `x`: when `g=1,h=0`, changing `x` from zero to one changes
the output from one to zero. A circuit containing only AND and OR is monotone,
so at least one NOT gate is necessary. Every circuit therefore has at least
five gates, and the displayed circuit is minimum.

## Labelwise audit

The gates `g,h` are prefix-independent. The dependent gates restrict as
follows:

| Label | `x=0` residual | `x=1` residual | Multiplicity |
|---|---|---|---:|
| `n` | constant one | constant zero | 0 |
| `a` | `g` | constant zero | 1 |
| `o` | `g OR h` | `h` | 2 |

Both `g OR h` and `h` are nonconstant, non-input, and distinct. Thus `n` is
the sole disappeared label and `o` the sole split label, giving `z=t=1`.
QED.

## Scope

This proves that global minimum size, prefix dependence, and distinct active
cofactors do not generically force `z>t`. It does not reproduce SAT-gamma's
many-identifier complementary matrix. GATE-004L remains open only as a
SAT-specific, multi-pair theorem.
