import random
import time
import sys
from init import *

reinit()

sys.setrecursionlimit(200000)

def finddir(cx, cy, ex, ey):
    if ey==cy and cx>ex: return random.choice([8, 1])
    elif ey>cy and ex==cx: return random.choice([2, 3])
    elif ey==cy and ex>cx: return random.choice([4, 5])
    elif ey<cy and ex==cx: return random.choice([6, 7])
    elif (ex-cx)==(ey-cy) and ex<cx: return random.choice([1, 2])
    elif (ex-cx)==(ey-cy) and ex>cx: return random.choice([5, 6])
    elif (ex-cx)==-(ey-cy) and ex>cx: return random.choice([3, 4])
    elif (ex-cx)==-(ey-cy) and ex<cx: return random.choice([7, 8])
    elif ex>cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 4
    elif ex>cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 5
    elif ex>cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 6
    elif ex<cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 7
    elif ex<cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 8
    elif ex<cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 1
    elif ex<cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 2
    elif ex>cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 3
    else: return 9

avrarco = 0
avrco = 0
avrsucc = 0
avrrich = 0
avrtlap = 0

minarco = -1
minco = -1
minrich = -1
mintlap = -1

its = 300
nstits = its
timewait = 30

smer = finddir(startx, starty, endx, endy)

print 'Potraga bez gledanja:'
def rec(curx, cury, ind):
    global co, arco, endtime
    riched[curx][cury] = ind
    co += 1
    arco += 1
    if curx == endx and cury == endy: return True
    endtime = time.time()
    if endtime-starttime > timewait and timewait!=-1: return False

    smer = finddir(curx, cury, endx, endy)
    chs=[]
    if smer==1:
        chs=[0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2, 1]
    elif smer==2:
        chs=[3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 1, 1, 2]
    elif smer==3:
        chs=[3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 0, 0, 2]
    elif smer==4:
        chs=[1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 2, 2, 0]
    elif smer==5:
        chs=[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 0]
    elif smer==6:
        chs=[2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 3]
    elif smer==7:
        chs=[2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 3]
    elif smer==8:
        chs=[0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 1]
    #print smer
    pravs = []
    for i in range(0,4):
        pravs.append(random.choice(chs))
        while pravs[i] in chs: chs.remove(pravs[i])
    for i in range(0, 4):
        prav = pravs.pop(0)
        if curx > 0 and prav == 0: #gore
            if mat[curx-1][cury] > 0 and riched[curx-1][cury] == -2:
                if rec(curx-1, cury, ind + max(mat[curx-1][cury], mat[curx][cury])):
                    return True
        if curx < rows-1 and prav == 1: #dole
            if mat[curx+1][cury] > 0 and riched[curx+1][cury] == -2:
                if rec(curx+1, cury, ind + max(mat[curx+1][cury], mat[curx][cury])):
                    return True
        if cury > 0 and prav == 2: #levo
            if mat[curx][cury-1] > 0 and riched[curx][cury-1] == -2:
                if rec(curx, cury-1, ind + max(mat[curx][cury-1], mat[curx][cury])):
                    return True
        if cury < cols-1 and prav == 3: #desno
            if mat[curx][cury+1] > 0 and riched[curx][cury+1] == -2:
                if rec(curx, cury+1, ind + max(mat[curx][cury+1], mat[curx][cury])):
                    return True
        prav += 1
        if prav==4: prav = 0
    #riched[curx][cury] = -2
    co -= 1
    arco += 1
    return False

posttime = time.time()
for it in range(0, its):
    if its < 100: print '\rOdradjeno:', it*100/its, '%',
    elif it%(its/100)==0:  print '\rOdradjeno:', it*100/its, '%',
    from init import *
    reinit()
    starttime = time.time()
    endtime = starttime
    succ = rec(startx, starty, 0)
    #endtime = time.time()
    co -= 1
    tlap = endtime-starttime
    if succ:
        if minarco == -1 or (minarco > arco): minarco = arco
        if minco == -1 or (minco > co): minco = co
        if minrich == -1 or (minrich > riched[endx][endy]):
            minrich = riched[endx][endy]
        if mintlap == -1 or (mintlap > tlap): mintlap = tlap
        avrarco += arco
        avrco += co
        avrsucc += 1
        avrrich += riched[endx][endy]
        avrtlap += tlap if tlap<timewait else 0
    succ = False
    if tlap>timewait: nstits-=1
poentime = time.time()
print '\rOdradjeno:  100 %'
print 'Srednji broj predjenih koraka: ', avrarco/float(nstits if nstits>0 else 1)
print 'Najmanji broj predjenih koraka: ', minarco
print 'Srednji Broj koraka do cilja: ', avrco/float(nstits if nstits>0 else 1)
print 'Najmanji Broj koraka do cilja: ', minco
print 'Srednji broj poteza: ', avrrich/float(nstits if nstits>0 else 1)
print 'Najmanji broj poteza: ', minrich
print 'Broj pronadjenih u ogranicenju od', timewait, 's: ', avrsucc/float(its)*100, '%'
print 'Srednji vreme izvrsavanja: ', avrtlap/float(nstits if nstits>0 else 1)
print 'Broj uspesnih: ', nstits, ' / ', its
print 'Najmanje vreme izvrsavanja: ', mintlap
print 'Ukupno vreme: ', poentime-posttime
print 'Kraj'
    
