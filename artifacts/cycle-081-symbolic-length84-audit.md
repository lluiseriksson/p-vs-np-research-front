# Cycle 081 symbolic complete-length-84 audit

**Label: PROVED** (finite certificates only)

- The complete symbolic oracle checks 160,000 gap-at-most-20 types in each of
  four residue classes for the full identifier range 1 through 524,287.
- Failure counts are `30,31,31,30`, totaling 122.
- On `(84,92,100,103,104)`, both the symbolic oracle and literal enumeration
  of all 524,287 identifiers find mask 8 as the sole missing ordinary mask.
  The literal run took 104.03 seconds on the recording machine.

The translated packing is proved in LEMMA-091. The artifact makes no circuit
lower-bound or terminal claim.
