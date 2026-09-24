import csv, collections, os, json

# Export root: set PTC_DATA to point elsewhere, otherwise ../data next to this script.
DATA=os.environ.get('PTC_DATA') or os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')

SEASONS=['2092','2093','2094']; GENDERS=['boys','girls']
FORMATS={  # name -> (S, D, courts, players)
 '2S/3D':(2,3),'1S/4D':(1,4),'3S/3D':(3,3),'3S/4D':(3,4),'5S/2D':(5,2),
 '4S/4D':(4,4),'3S/5D':(3,5),'4S/5D':(4,5),'2S/2D':(2,2),
}
def fmt_players(f):
    s,d=FORMATS[f]; return s+2*d
def fmt_courts(f):
    s,d=FORMATS[f]; return s+d

def load(season,gender):
    base=os.path.join(DATA,season,gender)
    P={r['program_id']:r for r in csv.DictReader(open(f'{base}/programs.csv'))}
    PL=collections.defaultdict(list)
    players={}
    for r in csv.DictReader(open(f'{base}/players.csv')):
        players[r['player_id']]=r; PL[r['program_id']].append(r)
    D={r['dual_id']:r for r in csv.DictReader(open(f'{base}/duals.csv'))}
    L={}
    for r in csv.DictReader(open(f'{base}/lines.csv')): L[r['line_id']]=r
    LP=collections.defaultdict(list)
    for r in csv.DictReader(open(f'{base}/line_players.csv')): LP[r['line_id']].append(r)
    return P,players,PL,D,L,LP
