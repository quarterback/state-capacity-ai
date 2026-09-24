# JHSAA 5A dual-meet format review — the 6S/5D petition

**Petition.** 5A schools have asked to replace 1S/4D with **6S/5D** — eleven courts, the most
expansive card in the state — arguing it makes 5A the singles class and gets more kids playing.

**Answer: grant it.** The distinctiveness claim checks out (54.5% singles would be the only
singles-majority postseason format in the association), eleven courts is odd so it cannot tie, and
the engine's arranger is already written for any singles width.

**The one decision that matters is the roster setting.** 6S/5D puts **16 on court** and the current
floor is **16** — which is not a coincidence, since today's floor is 11 varsity + a 5-player JV
minimum. On unchanged rosters the petition *reduces* 5A kids in a match by 425 (−4.7%) and leaves
61% of programs unable to field a JV team at all.

Set `ROSTER_FLOOR` to **21** and 5A's band to **(23, 25)** and it delivers what the petitioners
asked for: JV intact, and ~742 new varsity seats per season across 5A.

One constraint a 5A-only raise won't fix: under "the wider card wins", 5A's 631 cross-class
showcase dual-sides would pull floor-sized opponents (1A 59.8%, Group 3 50.0%) onto a sixteen-player
card with zero spare. Raise the global floor, or play those showcases at the opponent's shape.

Full findings: [`findings.md`](findings.md). Reproduction: [`run.sh`](run.sh) — pure stdlib
Python 3, point `PTC_DATA` at the unpacked exports.
