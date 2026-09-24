# The 5A petition for 6S/5D

Prepared for the JHSAA competition committee
Data: Play to Clinch research exports, 2092–2094, boys and girls, all classifications
Scope: 5,373 program-seasons · 152,522 varsity dual-sides · ~1.13m court results
Engine constants verified against `quarterback/tennis-team-manager` @ `94997013`

---

## 1. Answer

**Grant it. 6S/5D works, and the roster question is a settings change, not an obstacle.**

The petitioners are right on the substance. 6S/5D is **eleven courts — odd, so it cannot tie** —
and at **54.5% singles it would be the only singles-majority postseason format in the
association**. That distinctiveness claim checks out exactly (§3). The engine's arranger is
already written for any singles width, so this is closer to a membership change than a rebuild
(§5).

The one thing the committee must decide deliberately is the roster setting, because **6S/5D puts
sixteen on court and the current floor is sixteen**. That is not a coincidence to work around —
today's floor of 16 *is* 11 varsity + a 5-player JV minimum. The same arithmetic at sixteen
varsity gives **a floor of 21 and a 5A band of 23–25**. Set those and everything below resolves;
leave them and the format quietly cannibalises the JV season.

---

## 2. What 6S/5D requires

Players on court is **S + 2D** — verified, not assumed: across all 152,522 varsity dual-sides, one
player occupies exactly one court, with no forfeits anywhere in the archive.

**6 singles + 5 doubles = 11 courts = 16 players on court.**

Against current 5A rosters (445 program-seasons, band 18–20, floor 16):

| Spare after dressing 16 | Programs | Share |
|---|---|---|
| **0 — entire roster on court** | 89 | **20.0%** |
| 1 | 59 | 13.3% |
| 2 | 37 | 8.3% |
| 3–5 | 126 | 28.3% |
| 6+ | 134 | 30.1% |

Every 5A program *can* field sixteen — the floor guarantees it. But a fifth of them would dress
their whole roster, where any injury, illness or ineligibility forfeits a court.

### The JV knock-on, which is the real mechanism

JHSAA runs **one roster, one ladder**: the top N dress varsity and everyone below them is JV. A JV
dual needs five a side. That is why the floor is 16 — it is 11 + 5, sized to guarantee every
program a JV team.

At sixteen varsity, on today's rosters:

| | Kids in a match | Programs with no JV at all |
|---|---|---|
| Today (11 varsity) | 8,969 | **0 of 445** |
| 6S/5D (16 varsity), rosters unchanged | 8,544 | **271 of 445 (61%)** |

On unchanged rosters the petition **reduces** the number of 5A kids playing by 425 (−4.7%), because
the median program (19) would dress 16 and have three left over — below the five a JV dual needs,
so those three play nothing. That is the opposite of the petitioners' stated goal, and it is worth
being explicit that this is a roster-settings artifact, not an argument against the format.

### Set the rosters and it delivers what they asked for

| Setting | Today | For 6S/5D |
|---|---|---|
| `ROSTER_FLOOR` | 16 (= 11 varsity + 5 JV) | **21** (= 16 + 5) |
| 5A band (`ROSTER_SIZE_BAND_BY_CLASS`) | (18, 20) → 7–9 spare | **(23, 25)** → same 7–9 spare |

With those set: JV survives intact, and 6S/5D creates **five more varsity seats per program —
about 371 per gender-season, ~742 per season across 5A**. That is the "more kids get
opportunities" case, and it is real, but it comes from the roster raise as much as from the
format.

---

## 3. The distinctiveness claim is correct

Singles share of every postseason format the association currently runs:

| Format | Courts | Singles share | Who plays it |
|---|---|---|---|
| 1S/4D | 5 | 20.0% | 2A, 3A, 4A, **5A**, Group 3 |
| 2S/3D | 5 | 40.0% | 1A |
| 3S/4D | 7 | 42.9% | 6A |
| 4S/5D | 9 | 44.4% | 7A, 8A, 9A, Group 1 |
| 3S/3D | 6 | 50.0% | Group 2 |
| **6S/5D** | **11** | **54.5%** | **— the petition** |

Nothing in the association is singles-majority in the postseason. Group 2's 3S/3D is exactly even
at 50%. 5A would be the only class where singles outweigh doubles, and it would do so while
playing the largest card in the state. The identity argument holds on its own terms.

Court count is odd, so **6S/5D cannot tie** — no tiebreak regime is needed. (This is the reason to
keep rejecting 4S/4D and 3S/5D, which are even and tie in 10.7–15.5% of duals.)

---

## 4. The one constraint a 5A-only roster raise will not fix

The association's rule when two formats meet is that **the wider card wins** — a program meeting a
wider-format opponent plays the wider shape rather than falling back. 5A played **631 cross-class
showcase dual-sides** over the three seasons. Under 6S/5D, every one of those opponents is pulled
onto a sixteen-player card.

All of them *can* do it — the floor is 16 association-wide, so nobody falls short. But for
floor-sized programs it means their entire roster:

| Class | Share sitting exactly at the 16 floor |
|---|---|
| 1A | **59.8%** |
| Group 3 | **50.0%** |
| 2A | 45.7% |
| 3A | 35.4% |
| 5A | 20.0% |
| 9A | 7.3% |

Raising only 5A's band does not touch this. Two clean options: raise `ROSTER_FLOOR` globally (it is
a single module constant, so this is one edit and it lifts every class), or exempt cross-class
showcases from the 5A card and play them at the opponent's shape. The first is simpler and matches
how the bands were raised once before.

---

## 5. Implementation notes

- **The arranger already generalises.** `_arrange_wide` is documented as "`_arrange_state`'s
  mechanism at ANY singles width" — it pools the top `n_singles + 2` and searches which
  `n_singles` play singles. 6S/5D pools eight and picks six. No new arrangement logic.
- **What does need building:** a `DUAL_FORMATS` entry, a flight-weight table (there is a
  per-shape `FLIGHT_WEIGHTS_4S5D`; 6S/5D needs its own), and the awards/TOSS tables extended to
  S5/S6. That is a design job, but a much smaller one than the consolidated doubles point the 2079
  study costed.
- **5A shares its roster band with 4A** (`"5A": (18, 20), "4A": (18, 20)`). Raising 5A's band
  requires splitting that entry, or 4A moves with it.
- **`ROSTER_FLOOR` is a single global constant**, not per class. There is no per-class floor to set
  today.
- Roster growth is automatic once the targets move — the builder tops a roster up to the floor from
  the current freshman class — so this propagates without a migration.

---

## 6. Method and limitations

**Method.** Computed directly from the three exports. Court requirements verified by counting
distinct players per dual-side rather than assumed. Tie rates come from re-scoring duals that
actually contested all nine courts. Engine constants (`ROSTER_FLOOR`, `ROSTER_SIZE_BAND_BY_CLASS`,
`WIDE_GROUPS`, `_arrange_wide`, `JV_FORMATS`, `injuries.BASE_RATE`) read from the simulator source
rather than inferred.

**Limitations.**

1. **No 6S/5D dual has ever been played**, in any class, in any archived season. Everything here
   about 6S/5D is arithmetic on roster sizes and format shape, not observed play. The widest
   evidence available is 4S/5D, which 55 5A programs have played across 231 dual-sides — filling
   all fourteen slots every time, including programs at the sixteen-player floor.
2. **The opportunity figures assume the JV minimum of five a side** (`JV_FORMATS`' smallest entry,
   1S/2D). Programs sitting just below a JV threshold are counted as fielding no JV at all, which
   is how the elastic table behaves but makes the cliff look sharper than a coach would experience
   it in a season with a flexible schedule.
3. **Roster counts are season rosters, not per-dual availability.** The zero-spare risk in §2 is
   structural; the archive records no 5A forfeits because no 5A team has been asked to dress
   sixteen.
4. **The 2092 export keys ~1.9% of `line_players` rows by name rather than id**, producing an
   apparent short count on 46 of 152,522 dual-sides. Artifacts of that keying, not real shortfalls.
