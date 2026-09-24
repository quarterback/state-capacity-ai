"""The 6S/5D petition: on-court demand, JV knock-on, and the roster settings it implies."""
import json, collections, statistics as st
R=json.load(open('out_rows.json'))['rows']
JV_MIN=5                       # smallest JV format (1S/2D) needs five a side
fa=[r['roster'] for r in R if r['group']=='5A']; N=len(fa)

def playing(roster, varsity):
    v=min(roster,varsity); rest=roster-v
    return v + (rest if rest>=JV_MIN else 0)

print(f'5A, {N} program-seasons. 6S/5D = 11 courts = 16 on court.\n')
print('Spare after dressing 16:')
for k in range(6):
    c=sum(1 for r in fa if r-16==k)
    print(f'  {k} spare: {c:3d} ({100*c/N:4.1f}%)')
print(f'  6+     : {sum(1 for r in fa if r-16>=6):3d}')
print('\nOpportunity math (one roster: top N varsity, remainder is JV if >=5 left):')
for lab,v in [('today (11 varsity)',11),('4S/5D (14)',14),('6S/5D (16)',16)]:
    tot=sum(playing(r,v) for r in fa)
    nojv=sum(1 for r in fa if r-min(r,v)<JV_MIN)
    print(f'  {lab:20} kids playing {tot:5d}   programs with no JV {nojv:3d}/{N} ({100*nojv/N:.0f}%)')
base=sum(playing(r,11) for r in fa); six=sum(playing(r,16) for r in fa)
print(f'  >>> 6S/5D on UNCHANGED rosters: {six-base:+d} kids ({100*(six-base)/base:+.1f}%)')
print('\nRoster settings implied:')
print('  floor  16 (=11+5 JV)  ->  21 (=16+5 JV)')
print('  5A band (18,20)       ->  (23,25)  [same 7-9 spare over the varsity card]')
prog=collections.Counter((r['season'],r['gender']) for r in R if r['group']=='5A')
per=st.mean(prog.values())
print(f'  new varsity seats: 5 x {per:.0f} programs = {per*5:.0f} per gender-season, {per*5*2:.0f} per season')
print('\nSingles share of each postseason format:')
for n,(S,D) in [('1S/4D',(1,4)),('2S/3D',(2,3)),('3S/4D',(3,4)),('4S/5D',(4,5)),
                ('3S/3D',(3,3)),('6S/5D',(6,5))]:
    ct=S+D
    print(f'  {n:7} {ct:2d} courts {100*S/ct:5.1f}% singles  {"EVEN - can tie" if ct%2==0 else ""}')
print('\nFloor-sized programs by class (pulled onto 16 by "the wider card wins"):')
agg=collections.defaultdict(list)
for r in R: agg[r['group']].append(r['roster'])
for g in ['1A','Group 3','2A','3A','4A','5A','6A','7A','8A','9A','Group 1','Group 2']:
    w=agg[g]
    print(f'  {g:9} {100*sum(1 for x in w if x==16)/len(w):5.1f}% at the 16 floor')
