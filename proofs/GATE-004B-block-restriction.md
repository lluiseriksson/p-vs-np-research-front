# GATE-004B — SAT-specific amortized block restriction

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `A,B>0`, `0<=beta<1`, `delta>0`, and `n0` such
that for every `n>=n0` and every minimum-size general Boolean circuit `C_n`
computing the total length-`n` slice of `SAT-gamma`, there are:

1. an integer `m` with `n-A n^beta <= m<n`; and
2. a projection `pi : {0,1}^m -> {0,1}^n`, mapping each target input position
   to a constant or one source input bit,

for which

`SAT-gamma_n(pi(y)) = SAT-gamma_m(y)` for every `y in {0,1}^m`,

and there is a Boolean circuit `D` computing `y -> C_n(pi(y))`, obtained by
substituting the projection and deleting or constant-folding gates, with at most

`|C_n| - B n^(beta+delta)`

gates.

The base circuit model has no free constant inputs. Any constants introduced
by restriction are normalized back to that model before `|D|` is counted. By
LEMMA-005 this costs at most three gates whenever `m>=1`; the displayed loss is
required after paying that additive cost.

### Model card

| Field | Value |
|---|---|
| Computational model | Minimum general acyclic Boolean circuits for exact `SAT-gamma` slices; coordinate projections |
| Uniform/non-uniform | Fully non-uniform circuit adversary; projection constants are chosen per circuit and length |
| Circuit size | Certified loss `B n^(beta+delta)` while input length falls by at most `A n^beta` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; projection may depend non-uniformly on the minimum circuit |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed constants; every sufficiently large length; every minimum circuit; exists one projection |
| Regime | Worst-case exact total-language computation; malformed encodings reject |

## Bridge to GATE-004

The derived circuit computes the length-`m` SAT slice, so if
`S(n)` is minimum circuit size,

`S(n) >= S(m) + B n^(beta+delta)`.

LEMMA-002 then gives `S(n)=Omega(n^(1+delta))`. Thus GATE-004B is a concrete
sufficient brick for GATE-004 without changing the circuit model.

## Proven projection supply

ENC-002 provides projections for `m=n-4t`: fix the first `4t` description bits
to `(1111)^t` and map the remaining `m` coordinates identically. The result is
`t` double negations around the source formula, so validity and satisfiability
are preserved for every source string, including malformed strings.

Choosing `t=Theta(n^beta)` supplies the required length window. What remains is
the circuit-loss inequality.

## First attempt: generic fanout counting

The direct attempt was to argue that fixing `Theta(n^beta)` prefix inputs of a
size-`n^(1+delta)` circuit must eliminate `Theta(n^(beta+delta))` gates by
average fanout. This does not follow. Total circuit size can lie in a large
subcircuit fed through low-fanout buffers, while the specified prefix inputs
touch only `O(n^beta)` local gates. Fanout counts edges at the input boundary;
it does not force constant propagation through an arbitrary downstream circuit.

An explicit generic counterexample is

`F(x_1,...,x_t,z) = G(z) OR (x_1 AND ... AND x_t)`.

Use an arbitrarily large circuit for `G`, an `O(t)`-gate AND tree, and one final
OR. Every `x_i` has boundary fanout one. Fixing the `x_i` to zero leaves the
entire `G` circuit and removes only `O(t)` gates, independently of the total
circuit size. This does not model a minimum SAT circuit; it refutes only the
generic fanout inference.

This is `GATE-004B-FANOUT — NO-GO`: projection identity plus generic fanout
accounting is quantitatively insufficient. It does not refute GATE-004B for
minimum SAT circuits, whose special structure is unknown.

## Next attack

ENC-003 now supplies exact left/right tautology contexts, not only a fixed
prefix. LEMMA-003 proves that averaging arbitrary coordinate weights over this
contiguous family still cannot force gate loss: every sublinearly padded
placement retains a large common core. This route is
`GATE-004B-CONTEXT-AVERAGING — NO-GO`.

The active subgate is GATE-004C. It restricts GATE-004B to the explicit ENC-003
family and demands a loss proof based on semantic structure of minimum SAT
circuits or downstream propagation rather than input-coordinate coverage.
