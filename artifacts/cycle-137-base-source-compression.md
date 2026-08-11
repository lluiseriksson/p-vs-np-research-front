# Cycle 137 — base-source compression

**Label: PROVED**

LEMMA-169 extends the proved one-excess pruning operation to every base with
resource at most `j+1`. LEMMA-170 proves exact compression and substitution
for a base-only source formula.

GATE-004BP-NONTRIVIAL-SOURCE uses those lemmas to show that a minimum-arity
counterexample cannot have a source formula with two or more base inputs. The
remaining source is a primary base input.

Essential base arity alone cannot cross that boundary: primary-source
compression is only variable renaming. This inference scheme is recorded as
GATE-004BP-BASE-COUNT-INDUCTION-ONLY, labelled `NO-GO`, without any claim of a
realizable circuit counterexample. GATE-004BQ is opened for the primary-source
cofactor structure.

## Classification

- LEMMA-169: `PROVED`
- LEMMA-170: `PROVED`
- GATE-004BP-NONTRIVIAL-SOURCE: `PROVED`
- GATE-004BP-BASE-COUNT-INDUCTION-ONLY: `NO-GO`
- GATE-004BQ: `EXPLORATORY`
