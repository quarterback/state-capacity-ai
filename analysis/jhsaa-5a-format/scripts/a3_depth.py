import json, collections, statistics as st
R=json.load(open('out_rows.json'))['rows']
agg=collections.defaultdict(list)
for r in R: agg[r['group']].append(r)
def q(v,p):
    v=sorted(v); 
    if not v: return float('nan')
    i=min(len(v)-1,int(p*len(v)))
    return v[i]

print('=== 5A roster capacity, distribution over 445 program-seasons (2092-2094, both genders) ===')
rs=agg['5A']
for label,key in [('nominal roster','roster'),('varsity pool used','varsity_pool'),('postseason pool used','post_pool')]:
    v=sorted(x[key] for x in rs)
    print(f'  {label:22} min {v[0]:3d}  p5 {q(v,.05):3d}  p25 {q(v,.25):3d}  median {st.median(v):5.1f}  p75 {q(v,.75):3d}  max {v[-1]:3d}')
print()
print('  5A program-seasons with nominal roster below N:')
v=[x['roster'] for x in rs]
for n in [12,13,14,15,16,17,18]:
    k=sum(1 for x in v if x<n)
    print(f'    < {n:2d} players: {k:3d} of {len(v)}  ({100*k/len(v):.1f}%)')
print()
print('=== Depth-quality curve: median current_grade of the Nth-best rostered player ===')
print('     (20-80 scouting scale; the courts a format reaches are marked)')
Ns=[1,3,5,7,9,11,12,13,14,16]
print(f"{'group':8} " + ' '.join(f'#{n:<4}' for n in Ns))
for g in ['5A','4A','3A','6A','7A','8A','9A','Group 1']:
    cells=[]
    for n in Ns:
        vals=[x['grades'][n-1] for x in agg[g] if len(x['grades'])>=n]
        cells.append(f'{st.median(vals):4.1f}' if vals else '  - ')
    print(f'{g:8} ' + ' '.join(f'{c:<5}' for c in cells))
print()
print('=== Drop-off: median grade of #1 minus #Nth (how much weaker the marginal court is) ===')
print(f"{'group':8} " + ' '.join(f'#{n:<4}' for n in [9,11,12,13,14]))
for g in ['5A','4A','6A','7A','8A','9A','Group 1']:
    cells=[]
    for n in [9,11,12,13,14]:
        d=[x['grades'][0]-x['grades'][n-1] for x in agg[g] if len(x['grades'])>=n]
        cells.append(f'{st.median(d):4.1f}')
    print(f'{g:8} ' + ' '.join(f'{c:<5}' for c in cells))
