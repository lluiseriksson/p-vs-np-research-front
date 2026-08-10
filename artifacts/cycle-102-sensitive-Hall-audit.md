# Cycle 102 sensitive-Hall audit

## Sensitive parity path

**Label: PROVED**

LEMMA-115 traces each negative essential input through nodes that actually
change on a canonical witness pair and obtains an odd-NOT path to the output.

## Hall gate

**Label: EXPLORATORY**

GATE-004AK defines NOT-or-chord neighborhoods inside the sensitive subgraphs.
Singleton Hall inequalities follow from LEMMA-115; expansion for every larger
set remains unproved and would close the exact standalone tradeoff.

## Range-free outcome

**Label: NO-GO**

The De Morgan formula has `N=4m+1`, `t=0`, and every sensitive neighborhood
equal to the final NOT singleton. Hence sensitivity semantics alone cannot
prove Hall; the low-N hypothesis must do substantive work. No SAT lower bound
or terminal progress is claimed.
