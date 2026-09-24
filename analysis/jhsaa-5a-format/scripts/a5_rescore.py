"""Counterfactual re-scoring: played courts are a superset, so narrower formats can be scored exactly."""
import csv, collections, json
from load import DATA, load, SEASONS, GENDERS

CAND={  # name -> (singles slots, doubles slots)
 '1S/4D (current 5A)':(1,4), '2S/3D':(2,3), '3S/3D':(3,3), '3S/4D':(3,4),
 '4S/4D':(4,4), '3S/5D':(3,5), '4S/5D':(4,5), '5S/2D':(5,2),
}
def score(slotwin, S, D):
    """slotwin: dict slot->1 if home won. Returns (home,away) or None if a needed slot is absent."""
    need=[f'S{i}' for i in range(1,S+1)]+[f'D{i}' for i in range(1,D+1)]
    if any(s not in slotwin for s in need): return None
    h=sum(slotwin[s] for s in need)
    return h, len(need)-h

res=collections.defaultdict(lambda: collections.Counter())
samples=collections.Counter()
for season in SEASONS:
    for gender in GENDERS:
        P,players,PL,D,L,LP=load(season,gender)
        by_dual=collections.defaultdict(dict)
        for lid,l in L.items():
            by_dual[l['dual_id']][l['slot']]=int(l['home_won'])
        for did,slotwin in by_dual.items():
            d=D[did]
            if d['level']!='v': continue
            hg=P.get(d['home_program_id'],{}).get('championship_group')
            ag=P.get(d['away_program_id'],{}).get('championship_group')
            if hg!=ag or hg is None: continue      # same-class duals only
            full=score(slotwin,4,5)
            if full is None: continue              # only duals that played all 9 courts
            samples[hg]+=1
            fw = 1 if full[0]>full[1] else 0       # 9 courts -> never tied
            for name,(S,Dd) in CAND.items():
                r=score(slotwin,S,Dd)
                if r is None: continue
                courts=S+Dd
                if r[0]==r[1]: out='tie'
                elif (1 if r[0]>r[1] else 0)==fw: out='agree'
                else: out='flip'
                res[(hg,name)][out]+=1
                res[(hg,name)]['n']+=1
json.dump({f'{k[0]}||{k[1]}':dict(v) for k,v in res.items()},open('out_rescore.json','w'))
print('Duals with all 9 courts played (same-class), by group:', dict(samples))
print()
order=['1S/4D (current 5A)','2S/3D','3S/3D','5S/2D','3S/4D','4S/4D','3S/5D','4S/5D']
for g in ['5A','7A','8A','9A','Group 1']:
    if samples[g]==0: continue
    print(f'--- {g}  (n={samples[g]} full 9-court duals) ---')
    print(f"  {'format':22} {'courts':>6} {'ties':>7} {'flips vs 9-court':>17}")
    for name in order:
        c=res[(g,name)]
        if not c['n']: continue
        S,Dd=CAND[name]
        print(f"  {name:22} {S+Dd:6d} {100*c['tie']/c['n']:6.1f}% {100*c['flip']/c['n']:16.1f}%")
    print()
