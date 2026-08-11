# GATE-004CQ — classify full four-code boundary signatures

**Label: EXPLORATORY**

For every direct shared boundary `b` of `h`, record

`sigma(b)=(b_00,b_01,b_10,b_11)`

together with the corresponding four-code vector of its aligned-on-`01/11`
mask. LEMMA-195 constrains only the second and fourth coordinates;
LEMMA-196 shows the first and third can retain switching information.

## Falsifiable theorem

For every complete boundary-signature family in a minimum size-three-carrier
parent, one of the following holds:

1. a four-code-preserving common factoring removes `g,h` at no greater size
   and strictly lowers an extremal potential;
2. preserving a `00/10`-switching boundary requires a third deletion in a
   satisfying minor;
3. the first boundary carrying both carrier systems yields a private-cone
   certificate; or
4. reconvergence of the `01/11` and `00/10` carriers forces a forbidden
   non-bridge deletion.

No rewrite may be certified from only the satisfying-row coordinates.

LEMMA-197 realizes the complete output table, a size-three `01/11` carrier,
and a switching `00/10` handoff in one nonminimal single-output circuit. Thus
four-code signature consistency alone is `NO-GO`. GATE-004CR is the active
minimum-cost and cycle-minor audit for such handoffs.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1` with size-three carrier and full four-code boundary vectors |
| Uniform/non-uniform | Every finite non-uniform operational tuple |
| Circuit size | Parent `K+2`; neutral budget exhausted; boundary family unrestricted |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; all boundary fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactor vectors and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three-carrier parent |
| Regime | Exact worst-case four-code signature gate; not a SAT lower bound or terminal result |
