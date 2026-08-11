# LEMMA-171 — a primary formula interface hides at most its degree

**Label: PROVED**

Let a primary base input `x` be a core source of degree `d`. Suppose deleting
that source leaves cycle rank zero. Splitting its `d` outgoing wires into `d`
formula leaves gives a formula `F(x_1,...,x_d,Y)` for the parent function.

If some common fixing `x_1=...=x_d=c` leaves the nonzero canonical residual

`Q(Y_0) W_j(T)`,

then at least `j-d` implication clauses already have a syntactically private
NOT gate in the unfixed parent formula. Neutralizing any one of those clauses
deletes its private NOT before the interface is fixed.

## Proof

After the common fixing, the pruned residual is a variable-read-once formula.
The pair-subtree argument of LEMMA-157, which does not require equality of the
total NOT count, gives at least one clause-private NOT for each of the `j`
tail pairs.

The only fixed external leaf occurrences are the `d` copies of `x`.
LEMMA-161 injects every residual private NOT that was not already private in
the parent into a distinct fixed external leaf. At most `d` clauses can
therefore be defective, leaving at least `j-d` parent-private clauses.

## Model card

| Field | Value |
|---|---|
| Computational model | Fanout-one AND/OR/NOT formulas with repeated occurrences of one primary interface input |
| Uniform/non-uniform | Every individual non-uniform formula; uniform symmetric implication tail |
| Circuit size | At least `j-d` parent-private tail NOTs after fixing `d` interface leaves |
| Circuit depth | Unrestricted formula depth |
| Fan-in | AND/OR two; NOT one; fanout one after interface unfolding |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Formula-tree ancestry and Boolean cofactors only |
| Asymptotic quantifiers | Every `j>=1`, every `d>=1`, and every attained nonzero base cofactor satisfying the premise |
| Regime | Exact worst-case external-interface defect theorem; not a cyclic-residual, SAT-lower-bound, or terminal result |
