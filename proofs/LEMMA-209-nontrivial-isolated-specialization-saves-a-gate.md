# LEMMA-209 — nontrivial isolated specialization saves a gate

**Label: PROVED**

Let `S` be a finite AND/OR/NOT sub-DAG with unique output `r`. Assume every
incoming noninput signal other than raw `u` is globally `u`-independent, raw
`u` is the only `u`-dependent source entering `S`, and `r` depends essentially
on `u`. For either `sigma in {0,1}`, if the cofactor `r|_{u=sigma}` is
nonconstant, then hardwiring raw `u` to `sigma` and fully propagating constants
produces an AND/OR/NOT sub-DAG for that cofactor with at most

`|S|-1`

gates. No constant generator is required.

Consequently, in the LEMMA-205/206/207 applications, any nonconstant
cofactor specialization that preserves the parent function gives a strictly
smaller parent circuit. If the selected cofactor is constant, propagation
through the cancelling boundary gives the strict saving already recorded in
LEMMA-205.

## Proof

Because every nonraw source entering `S` is `u`-independent while `r` depends
on `u`, there is a directed path from raw `u` to `r` inside `S`. Let `g` be
the first gate on such a path. It directly consumes raw `u`.

After setting `u=sigma`, gate `g` needs no gate:

- `NOT u` becomes a constant;
- `u AND w` becomes either zero or `w`;
- `u OR w` becomes either one or `w`;
- if both binary inputs are occurrences of `u`, the output is constant.

Redirect every identity case to the surviving input and propagate every
constant case forward. Each subsequent AND/OR/NOT gate is either retained
once or removed by a Boolean constant identity; no new gate is introduced.
In particular, `g` is removed.

Full propagation cannot leave an internal constant source. Whenever a
constant reaches another gate, that gate is evaluated or redirected and the
constant is propagated again. Since the final cofactor is nonconstant, this
process cannot terminate with a constant output. The resulting circuit
therefore uses no free constant and has at most one retained gate for every
gate of `S` other than `g`. Its size is at most `|S|-1`.

For the application, replace `S` by this smaller cofactor circuit. Whenever
the surrounding parent function is preserved—privately, by masked direct
consumers, or by later reconvergence—the exterior needs no new gate. Hence the
whole parent loses at least one gate. If the cofactor output is constant, the
AND/OR cancelling boundary and subsequent constant propagation remove a gate
without installing a constant source, exactly as in LEMMA-205. This proves
the consequence.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite constant-free unrestricted AND/OR/NOT DAG with one isolated raw source and free wires |
| Uniform/non-uniform | Every finite non-uniform sub-DAG satisfying the isolation and essential-dependence hypotheses |
| Circuit size | Every nonconstant cofactor has a realization with at most `|S|-1` gates |
| Circuit depth | Unrestricted; specialization and propagation may reduce depth |
| Fan-in | AND/OR two; NOT one; raw `u` may have arbitrary fanout inside `S` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction, identity redirection, and constant propagation |
| Asymptotic quantifiers | Every qualifying finite region, both values of `sigma`, and every base assignment |
| Regime | Exact worst-case local gate-saving theorem; not existence of an isolated region, SAT lower bound, or terminal result |
