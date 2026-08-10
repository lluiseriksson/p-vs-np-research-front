# Cycle 077 length-72 boundary audit

**Label: PROVED** (finite certificates only)

- The literal direct interval DP over identifiers 1 through 65,535 returns
  mask 16 as the sole missing ordinary mask on `(70,71,80,85,86)`.
- The sixteen-bit identifier projection basis has 371 rows and no missing
  strength-five obligation. Together with shorter lengths it yields 2,437
  behaviorally complete representatives and the same DP result.
- The complete range through identifier 131,071 realizes all ordinary masks
  on the representative.
- The first direct length-76 repair found is identifier 98,370: block
  `01 T_98370`, aligned at start 48, has zero mask 16.

Only the length-72 NO-GO and the single length-76 repair are claimed. No full
bound-76 universality audit or circuit conclusion is certified.
