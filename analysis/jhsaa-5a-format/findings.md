# 5A dual-meet format: can the rosters carry a wider card?

Prepared for the JHSAA competition committee
Data: Play to Clinch research exports, 2092–2094, boys and girls, all classifications
Scope: 5,373 program-seasons · 152,522 varsity dual-sides · ~1.13m court results
Engine constants verified against `quarterback/tennis-team-manager` @ `94997013`

---

## 1. Answer

**Yes — to any format on the table, including the association's widest. 5A can field 4S/5D.**

The capacity question is settled by a structural fact rather than a judgement call: the
association enforces a **hard roster floor of 16** (`jhsaa.ROSTER_FLOOR`), and 4S/5D — nine courts,
the widest card anyone plays — puts **fourteen** on court. Every program in the association,
in every class, clears the widest format with bodies to spare, by construction.

If the committee wants the most expansive format available, **4S/5D is the recommendation**. It is
fieldable, it is odd-court so it cannot tie, and 7A/8A/9A/Group 1 already run it so nothing has to
be designed. The only formats worth ruling out are **4S/4D and 3S/5D**, and not on capacity —
they have even court counts and tie in roughly one dual in eight, which means adopting a tiebreak
regime alongside the format.

---

## 2. Headroom, format by format

Players required is **S + 2D** — verified, not assumed: across all 152,522 varsity dual-sides, one
player occupies exactly one court. No forfeits, no doubling up anywhere in the archive.

5A, across 445 program-seasons:

| Format | Courts | On court | Min spare | p5 spare | Median spare | % unable to field |
|---|---|---|---|---|---|---|
| 3S/2D | 5 | 7 | 9 | 9 | 12 | **0.0%** |
| 2S/3D | 5 | 8 | 8 | 8 | 11 | **0.0%** |
| 1S/4D *(current)* | 5 | 9 | 7 | 7 | 10 | **0.0%** |
| 3S/3D | 6 | 9 | 7 | 7 | 10 | **0.0%** |
| 3S/4D | 7 | 11 | 5 | 5 | 8 | **0.0%** |
| 4S/4D | 8 | 12 | 4 | 4 | 7 | **0.0%** |
| 3S/5D | 8 | 13 | 3 | 3 | 6 | **0.0%** |
| **4S/5D** | **9** | **14** | **2** | **2** | **5** | **0.0%** |

Not one 5A program-season in three seasons, across both genders, falls short of any candidate
format. The thinnest 5A program on record carries sixteen and would dress fourteen with two in
reserve.

**This is not a 5A concession — it is the same floor everyone runs on.** Minimum spare at 4S/5D,
by class:

| Class | Currently plays | Min spare at 14 | Median spare | % with <4 spare |
|---|---|---|---|---|
| **5A** | 1S/4D | **2** | **5** | **33.3%** |
| 6A | 3S/4D | 2 | 7 | 21.2% |
| 7A | **4S/5D** | 2 | 7 | 17.3% |
| 8A | **4S/5D** | 2 | 8 | 11.7% |
| 9A | **4S/5D** | 2 | 8 | 14.0% |
| Group 1 | **4S/5D** | 2 | 7 | 19.9% |

Every class already running 4S/5D has exactly the same floor-case as 5A: two spare. 5A is thinner
in the middle — median five spare against seven or eight, and a third of its programs carry fewer
than four in reserve against 12–21% elsewhere. That is the real difference, and it is a bench-depth
difference, not a can-they-field-it difference.

The engine's own design note, on why a wide-format team meeting a narrow-format one plays the
wider card rather than falling back:

> *every program in this association carries the bench for a nine-court dual … Forcing the dual
> down to 5S/2D would be defending a roster constraint that does not exist here.*

---

## 3. They have already done it

**Fifty-five distinct 5A programs have played 4S/5D** — 231 dual-sides across the three seasons, in
showcase pods and tiered showcases against 6A through 9A and Group 1 opposition (the wider card
wins when formats disagree, so 5A teams drawn against a wide-format opponent simply play nine
courts).

**They filled all fourteen slots every time.** Seventy-eight of those sides were played by programs
carrying seventeen players or fewer, several at exactly the sixteen-player floor. None came up
short, and none forfeited a court.

That is the capacity question answered observationally as well as structurally.

---

## 4. Which format

With capacity not binding, the choice comes down to two mechanical properties.

**Court count parity.** Odd cannot tie; even can. 4S/4D and 3S/5D are both eight courts and tie in
**10.7–14.6%** and **12.1–15.5%** of duals respectively (measured by re-scoring the 3,658 duals
that actually contested all nine courts). The association does have machinery for this — Group 2's
3S/3D road is settled on three concurrent 10-point tiebreakers at S1/D1/D2 — but importing it into
5A is a bigger rule change than the format itself, landing on about one 5A championship dual in
eight. **1S/4D (5), 3S/4D (7) and 4S/5D (9) are all odd and cannot tie.**

**Bench exposure.** The engine's injury rate applies per starter per dual (`injuries.BASE_RATE`
0.025, scaled by durability). Dressing fourteen instead of nine raises exposure by half again, and
it is the sixteen-player programs — a third of 5A carries fewer than four spare at 4S/5D — that
would feel it first. This is the one genuine cost of going to the widest card, and it is a real
one, not a reason to refuse.

| Format | Courts | On court | Ties | Verdict |
|---|---|---|---|---|
| 3S/2D | 5 | 7 | no | **Contraction** — fewer on court than today. Doesn't answer the petition. |
| 2S/3D | 5 | 8 | no | No wider than the status quo, one body smaller. |
| 1S/4D | 5 | 9 | no | Status quo. |
| 3S/3D | 6 | 9 | **16–18%** | Even courts, worst tie rate measured. |
| 3S/4D | 7 | 11 | no | **Safe option** — zero new capacity ask, 6A precedent. |
| 4S/4D | 8 | 12 | **10.7–14.6%** | Rule out — needs a tiebreak regime. |
| 3S/5D | 8 | 13 | **12.1–15.5%** | Rule out — same, slightly worse. |
| **4S/5D** | **9** | **14** | **no** | **Recommended if the committee wants maximum expansion.** |

**4S/5D** if the intent is to go as wide as the association goes: fieldable by every 5A program,
odd-court, and already administered by four other groups, so it is a membership change rather than
a design job.

**3S/4D** if the committee wants expansion with literally zero new capacity ask. 5A programs
already dress eleven for 3S/4D about twenty times a season — 9,071 dual-sides across the window —
and 6A's format-continuity pilot already runs exactly this shape through its postseason. It is the
conservative version of the same answer.

Either way the petition should be granted. The stated objection to it does not survive the data.

---

## 5. Method and limitations

**Method.** Computed directly from the three exports. Format requirements verified by counting
distinct players per dual-side rather than assumed. Tie rates come from re-scoring duals that
actually contested all nine courts, so no outcome is modelled. Engine constants (`ROSTER_FLOOR`,
`ROSTER_SIZE_BAND_BY_CLASS`, `WIDE_GROUPS`, `LEAGUE_SHAPE_GROUPS`, `DECIDER_FLIGHTS`,
`injuries.BASE_RATE`) read from the simulator source rather than inferred from data.

**Limitations.**

1. **Roster counts are season rosters, not per-dual availability.** The archive records who played,
   not who was healthy and held back. The floor-of-16 guarantee is structural and holds regardless;
   the bench-exposure point in §4 is a directional argument from the engine's injury rate, not a
   measurement of 5A forfeits (there are none to measure).
2. **The 231 5A dual-sides at 4S/5D were almost all against larger classes** — only ten were
   5A-versus-5A. For the capacity finding this does not matter: filling fourteen slots is filling
   fourteen slots whoever is across the net.
3. **The 2092 export keys ~1.9% of its `line_players` rows by name rather than id**, collapsing a
   few distinct players and producing an apparent short count on 46 of 152,522 dual-sides. All are
   artifacts of that keying, not real shortfalls.
4. **Rosters reflect current association configuration** applied to archived seasons, per the
   export's own documentation.
