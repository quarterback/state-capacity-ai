# JHSAA 5A dual-meet format review — the 6S/5D petition

**Status: adopted as JHSAA rule 2094.** Implemented in `quarterback/tennis-team-manager`
on branch `claude/jhsaa-2094-5a-6s5d`.

**Petition.** 5A schools asked to replace 1S/4D with **6S/5D** — eleven courts, sixteen on
court, the widest card in the state — arguing it makes 5A the singles class and gets more
kids playing.

**Finding.** The association's objection was roster capacity, and it did not survive the
exports. The roster floor is a hard 16, no 5A program-season in three years fell below it,
and **55 distinct 5A programs had already played 4S/5D** in showcases across 231 dual-sides
— filling all fourteen slots every time, including programs sitting at the floor.

**The distinctiveness claim verifies.** At 54.5% singles, 6S/5D is the only
singles-majority postseason format in the association; every other card runs 20% to 50%.
Eleven courts is odd, so it cannot tie.

**What the decision actually turned on: the roster floor.** Sixteen on court against a
floor of sixteen is not a coincidence — the old floor was the varsity eleven plus the five
a JV dual needs. The JV ladder (`jv_format`, unbounded) had also outgrown bands never
resized for it, with 1A, 2A and Group 3 carrying minima *below* the floor. Both were fixed
in the same rule: floor 16 → 20, every band re-cut, 5A and 4A split onto separate entries.

| class | old | new | JV spare | JV card at min → max |
|---|---|---|---|---|
| 9A, 8A | (20, 24) | (26, 30) | 15-19 | 5S/5D → 7S/6D |
| Group 1 | (19, 22) | (25, 29) | 14-18 | 4S/5D → 6S/6D |
| 7A, 6A | (19, 22) | (24, 28) | 13-17 | 5S/4D → 5S/6D |
| Group 2 | (17, 20) | (24, 28) | 13-17 | 5S/4D → 5S/6D |
| 5A | (18, 20) | (23, 26) | 12-15 | 4S/4D → 5S/5D |
| 4A | (18, 20) | (22, 24) | 11-13 | 3S/4D → 5S/4D |
| 3A | (17, 19) | (21, 24) | 10-13 | 4S/3D → 5S/4D |
| 2A | (15, 17) | (21, 23) | 10-12 | 4S/3D → 4S/4D |
| Group 3 | (14, 17) | (20, 23) | 9-12 | 3S/3D → 4S/4D |
| 1A | (14, 16) | (20, 22) | 9-11 | 3S/3D → 3S/4D |

**Correction worth recording:** an earlier draft of this analysis reported that 6S/5D would
strand 61% of 5A programs without a JV team. That was wrong — `jv_pool` cuts at
`lineup_need("regular")`, the eleven-player league card, not the postseason one, so a
road/State format change leaves the JV season untouched.

Full findings: [`findings.md`](findings.md). Reproduction: [`run.sh`](run.sh) — pure stdlib
Python 3, point `PTC_DATA` at the unpacked exports.
