"""Sweep / one-point rates and State-field dispersion by class — sections 3 and 4."""
import csv, collections, statistics as st, os
from load import DATA, load, SEASONS, GENDERS

FMT={'1A':('2S/3D',5),'2A':('1S/4D',5),'3A':('1S/4D',5),'4A':('1S/4D',5),'5A':('1S/4D',5),
     'Group 3':('1S/4D',5),'6A':('3S/4D',7),'Group 2':('3S/3D',6),'7A':('4S/5D',9),
     '8A':('4S/5D',9),'9A':('4S/5D',9),'Group 1':('4S/5D',9)}
POST={'sectional','ward','regional','zonal','epiregional','super_regional','semi_state',
      'divisional','semi_conference','conference','special_challenger','state_special',
      'metastate','state'}

res=collections.defaultdict(collections.Counter)      # margins, by scope
sub=collections.defaultdict(collections.Counter)      # identical duals scored 7 vs 5 courts
spread=collections.defaultdict(list); gaps=collections.defaultdict(list)

for season in SEASONS:
    for gender in GENDERS:
        P,players,D,L,LP=(lambda t:(t[0],t[1],t[3],t[4],t[5]))(load(season,gender))
        el={r['program_id']:float(r['value_elo'])
            for r in csv.DictReader(open(os.path.join(DATA,season,gender,'jhsaa_computer_ratings.csv')))
            if r['value_elo']}
        by=collections.defaultdict(dict)
        for lid,l in L.items(): by[l['dual_id']][l['slot']]=int(l['home_won'])
        field=collections.defaultdict(set)
        for did,d in D.items():
            if d['level']!='v': continue
            hg=P.get(d['home_program_id'],{}).get('championship_group')
            ag=P.get(d['away_program_id'],{}).get('championship_group')
            if hg!=ag or hg is None: continue
            ct=FMT[hg][1]
            if d['phase'] in POST:
                m=abs(float(d['home_points'])-float(d['away_points']))
                for s in ('allpost','state') if d['phase']=='state' else ('allpost',):
                    res[(hg,s)]['n']+=1
                    res[(hg,s)]['one']+= (m==1); res[(hg,s)]['shut']+= (m==ct)
            if d['phase']=='state':
                field[hg].add(d['home_program_id']); field[hg].add(d['away_program_id'])
                if d['home_program_id'] in el and d['away_program_id'] in el:
                    gaps[hg].append(abs(el[d['home_program_id']]-el[d['away_program_id']]))
            if d['phase']=='regular':
                sw=by[did]; need=['S1','S2','S3','D1','D2','D3','D4']
                if any(s not in sw for s in need): continue
                full=sum(sw[s] for s in need); five=sum(sw[s] for s in ['S1','D1','D2','D3','D4'])
                c=sub[hg]; c['n']+=1
                c['shut7']+= full in (0,7); c['shut5']+= five in (0,5)
                c['one7'] += abs(2*full-7)==1; c['one5'] += abs(2*five-5)==1
        for g,ps in field.items():
            v=[el[p] for p in ps if p in el]
            if len(v)>10: spread[g].append(st.pstdev(v))

ORDER=['5A','2A','3A','4A','Group 3','1A','Group 2','6A','7A','8A','9A','Group 1']
print('Postseason margins — all postseason vs State only')
print(f"{'class':9} {'fmt':7} {'n':>6} {'1-court':>8} {'shutout':>8} | {'n':>5} {'1-court':>8} {'shutout':>8}")
for g in ORDER:
    a,s=res[(g,'allpost')],res[(g,'state')]
    if not a['n']: continue
    print(f"{g:9} {FMT[g][0]:7} {a['n']:6d} {100*a['one']/a['n']:7.1f}% {100*a['shut']/a['n']:7.1f}% | "
          f"{s['n']:5d} {100*s['one']/s['n']:7.1f}% {100*s['shut']/s['n']:7.1f}%")
print('\nIdentical regular-season duals scored at 7 courts vs the 1S/4D 5-court subset')
print(f"{'class':9} {'n':>6} {'sweep@7':>8} {'sweep@5':>8} {'added':>7} {'1ct@7':>7} {'1ct@5':>7}")
for g in ORDER:
    c=sub[g]
    if not c['n']: continue
    s7,s5=100*c['shut7']/c['n'],100*c['shut5']/c['n']
    print(f"{g:9} {c['n']:6d} {s7:7.1f}% {s5:7.1f}% {s5-s7:+6.1f} {100*c['one7']/c['n']:6.1f}% {100*c['one5']/c['n']:6.1f}%")
print('\nState field dispersion')
print(f"{'class':9} {'field Elo SD':>13} {'median dual gap':>16}")
for g in ORDER:
    if spread[g]: print(f"{g:9} {st.mean(spread[g]):12.1f} {st.median(gaps[g]):15.1f}")
