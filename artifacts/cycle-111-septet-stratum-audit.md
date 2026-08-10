# Cycle 111 septet-stratum audit

## Bicyclic lower bound

**Label: PROVED**

LEMMA-133 selects a genuine one-bit interface in every bicyclic core. A leaf
cycle articulation handles cactus cores; a source of the acyclic theta
orientation handles theta cores. Fixing the bit leaves cycle rank at most one,
so the NOT count is at least `m-1`.

## Septet reduction

**Label: PROVED**

LEMMA-134 uses that lower bound to show that a deficient dependency-cone
septet can only yield `W_7` with `c=3,q=3`, 37 binary gates, and 40 gates total.

## Failed first attack

**Label: NO-GO**

Cycle-rank-three unfolding permits up to eight copies of each of the three
NOT gates, while formula inversion asks for only seven occurrences. The
resulting integer inequalities are compatible and do not prove GATE-004AR.
The next brick is a connected tricyclic-kernel classification.

## Scope

**Label: EXPLORATORY**

Size-seven Hall, full Hall, all unrestricted SAT circuit lower bounds, and P
versus NP remain open. No proof-assistant certification is claimed.
