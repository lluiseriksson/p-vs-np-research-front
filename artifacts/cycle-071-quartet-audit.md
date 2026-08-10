# Cycle 071 exhaustive quartet audit

**Label: PROVED** (finite certificate only)

Date: 2026-08-10

## Equivalence checks

- The bitset verifier reproduced the original identifier-68 residue failure
  counts exactly: `18,33,9,11`.
- It agreed with the original interval DP on the fourteen relevant masks for
  200 seeded random types at bound 36 and 200 at bound 68.
- Routine regression tests separately retain the Cycle-069 and Cycle-070
  obstruction quartets and the six repaired length-68 quartets.

## Exhaustive results

The initial 86-identifier alphabet was checked on 357,911 types in each of
four residues. Residues 0, 2, and 3 had zero failures. Residue 1 had exactly
six failures, all for mask 8:

`(69,72,77,78)`, `(69,73,77,78)`, `(69,74,77,78)`,
`(69,75,77,78)`, `(69,76,81,82)`, `(69,77,81,82)`.

After adding identifiers `1044,1060,1092,1156,16452,16516`, the completed
92-identifier alphabet was checked on the same
`4*357,911 = 1,431,644` types. Every residue returned zero failures.

Reproduce with:

```powershell
python verification/quartet_type_audit_fast.py 0 --length68
python verification/quartet_type_audit_fast.py 1 --length68
python verification/quartet_type_audit_fast.py 2 --length68
python verification/quartet_type_audit_fast.py 3 --length68
```

This certificate proves only the finite incidence premise of LEMMA-075. The
human proof supplies the translation reduction and hitting-set consequence.
No circuit lower bound or terminal statement is certified.
