"""Core roster-capacity analysis: can programs physically fill a bigger lineup?"""
import csv, collections, json, statistics as st
from load import DATA, load, FORMATS, fmt_players, fmt_courts, SEASONS, GENDERS

rows=[]          # per program-season record
dual_fill=[]     # per dual-side observation of a played format
for season in SEASONS:
    for gender in GENDERS:
        P,players,PL,D,L,LP=load(season,gender)
        # index lines by dual
        by_dual=collections.defaultdict(list)
        for lid,l in L.items(): by_dual[l['dual_id']].append(lid)
        # varsity usage per program
        used_v=collections.defaultdict(set)      # program -> set(pid) varsity
        used_post=collections.defaultdict(set)   # program -> set(pid) postseason/showcase
        per_dual_side=collections.defaultdict(set)  # (dual,side)->pids
        POST={'showcase_pod','showcase_tiered','sectional','ward','regional','zonal','epiregional',
              'super_regional','semi_state','divisional','semi_conference','conference',
              'special_challenger','state_special','metastate','state','toc'}
        for did,lids in by_dual.items():
            d=D[did]
            if d['level']!='v': continue
            slots={L[lid]['slot'] for lid in lids}
            S=sum(1 for s in slots if s[0]=='S'); Dd=sum(1 for s in slots if s[0]=='D')
            fname=f'{S}S/{Dd}D'
            sides={'home':d['home_program_id'],'away':d['away_program_id']}
            cnt={'home':set(),'away':set()}
            for lid in lids:
                for lp in LP.get(lid,[]):
                    cnt[lp['side']].add(lp['player_id'])
            for side,pid_set in cnt.items():
                pr=sides[side]
                used_v[pr]|=pid_set
                if d['phase'] in POST: used_post[pr]|=pid_set
                dual_fill.append((season,gender,pr,P.get(pr,{}).get('championship_group','?'),
                                  d['phase'],fname,len(pid_set),S+2*Dd))
        for pid_prog,plist in PL.items():
            p0=P.get(pid_prog)
            if not p0: continue
            grades=sorted((float(x['current_grade']) for x in plist if x['current_grade']),reverse=True)
            vpool=used_v.get(pid_prog,set())
            vgrades=sorted((float(players[x]['current_grade']) for x in vpool if x in players and players[x]['current_grade']),reverse=True)
            rows.append(dict(season=season,gender=gender,program_id=pid_prog,
                name=p0['name'],group=p0['championship_group'],cls=p0['classification'],
                enrollment=int(p0['enrollment'] or 0),
                roster=len(plist), varsity_pool=len(vpool), post_pool=len(used_post.get(pid_prog,set())),
                grades=grades, vgrades=vgrades))
json.dump({'rows':rows},open('out_rows.json','w'))
with open('out_dualfill.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['season','gender','program_id','group','phase','format','players_used','players_required'])
    w.writerows(dual_fill)
print('program-seasons:',len(rows),'dual-sides:',len(dual_fill))
