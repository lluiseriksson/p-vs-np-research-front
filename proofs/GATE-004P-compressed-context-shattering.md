# GATE-004P — compressed full-context shattering loss

**Label: NO-GO**

## Falsifiable theorem

There exist explicit constants `B,eta>0` and `d_0` such that the following
holds for every `d>=d_0`. Put `R=2^d`. Let `G` be an ambient total Boolean
function with a designated prefix block, and let `C` be a globally minimum
unrestricted circuit for `G`. Let

`rho:{0,1} x {0,1}^d -> {0,1}^p`

be an injective affine embedding whose coordinate functions are constants or
possibly complemented individual coordinates of `(q,s)`, with the `q`
direction a unit vector and the context directions nonzero and disjoint. Define
the trace

`F(q,s,y)=G(rho(q,s),y)`.

Assume:

1. for every `s`, the two adjacent residuals
   `F(0,s,.)`, `F(1,s,.)` have an OR equal to one common suffix function `H`;
2. there are suffix witnesses `y_a`, one for every `a in {0,1}^R`, such that
   after indexing contexts by `i(s) in {1,...,R}`,

   `F(b,s,y_a)=1 iff b=a_{i(s)}`;

3. for one fixed edge polarity, the substituted trace top region contains
   `U>=R` parent binary-gate labels whose semantic traces depend on `s`.

Let `q_s` be the exact semantic joint quotient size obtained from the two
copies of the ambient minimum circuit `C` under prefix rows
`rho(0,s),rho(1,s)`. Then

`sum_{s in {0,1}^d} (|C|-q_s) >= R(B U^eta+1)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted ambient Boolean circuits, an affine embedded edge/context cube, exact adjacent joint quotients of the ambient circuit, and explicit shattering witnesses |
| Uniform/non-uniform | Fully non-uniform ambient circuit adversary; theorem quantifies over every finite ambient function and embedding satisfying the hypotheses |
| Circuit size | Average parent-to-joint-quotient loss at least `B U^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine input embedding over `F_2`; all computation and quotients are Boolean |
| Asymptotic quantifiers | Exists fixed `B,eta>0,d_0`; every `d>=d_0`, every ambient prefix/suffix dimension, every eligible embedding, and every ambient minimum circuit satisfying all hypotheses |
| Regime | Worst-case exact total-function computation; no promise or distribution |

## Falsification

LEMMA-038 satisfies every displayed hypothesis with the identity affine
embedding. If `K` is the minimum size of its XNOR-INDEX base, appending `m`
fresh conjunctive suffix variables gives an ambient minimum circuit of size
`K+m`, a context-dependent trace region `U>=m`, and at least `2m` active joint
quotient classes for every context. For `m>=max(K+1,R)`, every required
hypothesis holds but

`|C|-q_s<=K-m<0`.

The claimed positive lower bound is therefore false.

## Would-be bridge to SAT

ENC-013 and ENC-014 identify `q` with the common one-bit polarity coordinate
and `s` with all `d=L-2` context assignments. The pointwise conditioned-SAT
identity supplies the common OR `H=SAT-gamma` on the suffix. ENC-009 and
ENC-010 supply the `2^R` assignment witnesses, and LEMMA-034 supplies `U>=R`.

Crucially, the theorem is stated for quotients of the ambient minimum circuit;
it does not assume that the affinely substituted trace circuit is itself
minimum. Thus the application does not silently transfer minimality through a
restriction.

Had GATE-004P held, it would have implied GATE-004O for the exact SAT row family. Since
`R=Omega(n^c)` and the prefix length is `O(log n)`, LEMMA-014 then yields the
same-language superlinear SAT circuit lower bound GATE-004.

## Scope of the no-go

LEMMA-038 shows that even the compressed full cube is insufficient for
arbitrary total functions. The counterexample is not SAT-gamma. GATE-004Q
therefore returns to the exact ambient SAT function and makes off-cube behavior
an explicit required input rather than another generic table hypothesis.
