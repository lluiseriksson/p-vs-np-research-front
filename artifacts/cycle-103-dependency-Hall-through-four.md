# Cycle 103 dependency-cone Hall audit

## Refined neighborhoods

**Label: EXPLORATORY**

GATE-004AL assigns each block every NOT gate and non-tree edge lying on a
directed path from that block to the output. Full Hall expansion would prove
the exact `N+t>=m` tradeoff.

## Closed local range

**Label: PROVED**

LEMMA-116 restricts the parent circuit to any selected blocks and bounds the
residual NOT count plus cycle rank by the neighborhood union. LEMMA-111 is
exact for one through four blocks, so all Hall inequalities of sizes one
through four hold.

## First open size

**Label: NO-GO**

For five blocks the generic bound is exactly four, attained by the parameter
pair `c=1,q=3`. Restriction plus LEMMA-111 alone is therefore one resource
short. The next gate is function-specific dependency incidence for quintets;
no standalone or terminal lower bound is claimed.
