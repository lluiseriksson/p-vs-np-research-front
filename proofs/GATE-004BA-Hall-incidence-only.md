# GATE-004BA-HALL-INCIDENCE-ONLY — localize savings from Hall cardinalities

**Label: NO-GO**

Dependency-cone Hall incidence alone permits a saving that appears only at
the full clause set.

Take `m>=3` clause indices as the vertices of a cycle and take the `m` cycle
edges as abstract resources. Let the neighborhood of index `i` be its two
incident edges. For every nonempty proper index set `I`, the union of its
resource neighborhoods has size at least

`|I|+1`.

Indeed, the complement is nonempty; counting the edge components of the
complement gives exactly `|I|+c` incident resources for some `c>=1`. For the
full set, however, the union has size exactly `m`.

Set the abstract base surplus `sigma=1`. The minimum neighborhood count at
cardinality `j<m` is `j+1`, achieved by a consecutive block, while at
cardinality `m` it is `m`. Thus the induced resource-saving profile is

`Delta_j=1+j-(j+1)=0` for `j<m`,

`Delta_m=1+m-m=1`.

All Hall inequalities hold, yet the only saving is the final unit jump. This
is exactly the late profile excluded by GATE-004BA/AZ.

The cycle incidence system is not claimed to be the dependency system of a
Boolean circuit computing `J_m`. It proves that Hall neighborhood
cardinalities, even for every subset, cannot localize the saving. A successful
proof must use additional circuit topology, orientation, gate semantics, or
compatibility among the resource neighborhoods.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract clause-to-resource incidence systems satisfying full Hall expansion |
| Uniform/non-uniform | Explicit finite cycle family; no circuit-realizability claim |
| Circuit size | Abstract surplus one and saving profile zero until a final unit jump |
| Circuit depth | Not represented |
| Fan-in | Not represented; underlying target circuit model remains fan-in-two AND/OR and unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set incidence only |
| Asymptotic quantifiers | Every `m>=3` |
| Regime | Structural no-go for Hall-cardinality-only localization; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
