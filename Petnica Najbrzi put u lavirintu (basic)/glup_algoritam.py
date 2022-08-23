import random
import sys
import time
from init import *

reinit()

sys.setrecursionlimit(2000)

avrarco = 0
avrco = 0
avrsucc = 0
avrrich = 0
avrtlap = 0

endtime = 0

minarco = -1
minco = -1
minrich = -1
mintlap = -1

its = 100
nstits = its
timewait = 30 #2*gettime()

def rec(curx, cury, ind, prav):
    riched[curx][cury] = ind
    global co, arco, endtime
    co += 1
    arco += 1
    if curx == endx and cury == endy: return True
    endtime = time.time()
    if endtime-starttime > timewait and timewait!=-1: return False
    global randnum
    if randnum == 0: randnum = random.randint(1, 10)
    randnum -= 1
    for i in range(0, 4):
        if curx > 0 and prav == 0:
            if mat[curx-1][cury] > 0 and riched[curx-1][cury] == -2:
                if rec(curx-1, cury, ind + max(mat[curx-1][cury], mat[curx][cury]), ((prav+arco)%4 if (riched[curx-1][cury]==-2 and randnum!=0) else random.randint(0, 3))):
                    return True
        if curx < rows-1 and prav == 1:
            if mat[curx+1][cury] > 0 and riched[curx+1][cury] == -2:
                if rec(curx+1, cury, ind + max(mat[curx+1][cury], mat[curx][cury]), ((prav+arco)%4 if (riched[curx+1][cury]==-2 and randnum!=0) else random.randint(0, 3))):
                    return True
        if cury > 0 and prav == 2:
            if mat[curx][cury-1] > 0 and riched[curx][cury-1] == -2:
                if rec(curx, cury-1, ind + max(mat[curx][cury-1], mat[curx][cury]), ((prav+arco)%4 if (riched[curx][cury-1]==-2 and randnum!=0) else random.randint(0, 3))):
                    return True
        if cury < cols-1 and prav == 3:
            if mat[curx][cury+1] > 0 and riched[curx][cury+1] == -2:
                if rec(curx, cury+1, ind + max(mat[curx][cury+1], mat[curx][cury]), ((prav+arco)%4 if (riched[curx][cury+1]==-2 and randnum!=0) else random.randint(0, 3))):
                    return True
        prav += 1
        if prav==4: prav = 0
    #riched[curx][cury] = -2
    co -= 1
    arco += 1
    return False
gasttime = time.time()
print 'Glup algoritam:'
for it in range(0, its):
    if its < 100: print '\rOdradjeno:', it*100/its, '%',
    elif it%(its/100)==0:  print '\rOdradjeno:', it*100/its, '%',
    from init import *
    reinit()
    randnum = random.randint(1, 10)
    starttime = time.time()
    endtime = starttime
    succ = rec(startx, starty, 0, random.choice([0, 1, 2, 3]))
    #endtime = time.time()
    co -= 1
    tlap = endtime-starttime
    if succ:
        if minarco == -1 or (minarco > arco): minarco = arco
        if minco == -1 or (minco > co): minco = co
        if minrich == -1 or (minrich > riched[endx][endy]):
            minrich = riched[endx][endy]
        if mintlap == -1 or (mintlap > endtime-starttime): mintlap = tlap
        avrarco += arco
        avrco += co
        avrsucc += 1
        avrrich += riched[endx][endy]
        avrtlap += tlap if tlap<timewait else 0
    succ = False
    if tlap>timewait: nstits-=1
gaentime = time.time()
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
print 'Ukupno vreme: ', gaentime-gasttime
print 'Kraj'

