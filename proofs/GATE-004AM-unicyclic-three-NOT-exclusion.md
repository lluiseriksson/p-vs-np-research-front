# GATE-004AM — exclude unicyclic three-NOT circuits for `W_5`

**Label: PROVED**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing the five-block
four-positive/one-negative product `W_5` can simultaneously have cycle rank
one and exactly three NOT gates.

No such circuit exists.

## Exact bridge

LEMMA-117 proves that every deficient quintet in GATE-004AL restricts to
exactly this stratum. Excluding it proves the Hall inequality for every
quintet. Together with LEMMA-116, this closes subset sizes through five;
LEMMA-122 records that consequence. This remains a local prerequisite, not a
full Hall theorem or SAT lower bound.

## Proof

Assume such a circuit exists. By LEMMA-118 at least two of its three NOT gates
have two directed paths to the output. Apply LEMMA-120. Its upstream formula
`A(X)` therefore contains `h>=2` NOT gates, while the downstream factor
`F(z,Y)` has a formula with exactly `3-h<=1` NOT occurrences. The intermediary
bit `z=A(X)` is nonconstant: otherwise the essential inputs in `X`, which have
no route outside the articulated upstream component, could not affect `W_5`.

Apply LEMMA-121 to `W_5(X,Y)=F(z(X),Y)`.

- If one clause is cut, no clause is wholly in `X`, and fixing an attained
  value of `z` makes `F` compute `W_4`. LEMMA-119 requires four downstream
  formula NOTs, contradicting `3-h<=1`.
- If no clause is cut, let `a` and `b` be the numbers wholly in `X` and `Y`.
  LEMMA-121 requires at least `a` NOTs in `A` and at least `b` in `F`.
  Therefore the original circuit has at least `a+b=5` NOT gates, contradicting
  its exact count three.

Both exhaustive cases are impossible. Hence the unicyclic three-NOT stratum
is empty.

## Scope

The theorem closes quintet dependency-cone Hall via LEMMA-122. It does not
close subset size six, full Hall expansion, the standalone family for all
`m`, a SAT circuit lower bound, or P versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for `W_5` with exact output-cone cycle rank and NOT count |
| Uniform/non-uniform | Every individual non-uniform five-block circuit |
| Circuit size | Excludes the exact `c=1,q=3` stratum; binary count would be `25` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean cofactor and inversion structure |
| Asymptotic quantifiers | The fixed five-block function and every pruned circuit with `c=1,q=3` |
| Regime | Exact finite structural exclusion for quintet Hall; not a full family lower bound or terminal result |
