import random
import time
import sys
import init
from math import sqrt

global co, arco, endx, endy, startx, starty, ukpp

co = 0
arco = 0
endx = 0
endy = 0
startx = 0
starty = 0
ukpp = 0.0

def calcpotraga_bezgledanja():
    global co, arco, endx, endy, startx, starty, riched, ukpp
    sqrt2 = 1.41
    rows = init.rows
    cols = init.cols
    startx = init.startx
    starty = init.starty
    endx = init.endx
    endy = init.endy
    mat = init.mat
    riched = [[-2 for i in range(cols)] for j in range(rows)]
    succ = False
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
    avrukp = 0

    minarco = -1
    minco = -1
    minrich = -1
    mintlap = -1
    minukp = -1
    
    its = init.rnditers
    nstits = its
    timewait = init.timewait

    smer = finddir(startx, starty, endx, endy)

    print 'Potraga bez gledanja:'
    def rec(curx, cury, ind):
        global co, arco, endtime, endx, endy, riched, ukpp
        riched[curx][cury] = ind
        
        co += 1
        arco += 1
        if curx == endx and cury == endy: return True
        endtime = time.time()
        if endtime-starttime > timewait and timewait!=-1: return False

        smer = finddir(curx, cury, endx, endy)
        chs=[]
        if smer==1:
            chs=[1, 6, 7, 7, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5]
        elif smer==2:
            chs=[2, 6, 1, 1, 4, 4, 7, 7, 7, 7, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5]
        elif smer==3:
            chs=[2, 4, 6, 6, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7]
        elif smer==4:
            chs=[4, 0, 2, 2, 5, 5, 6, 6, 6, 6, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1]
        elif smer==5:
            chs=[0, 5, 4, 4, 3, 3, 2, 2, 2, 2, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1]
        elif smer==6:
            chs=[5, 3, 0, 0, 7, 7, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6]
        elif smer==7:
            chs=[3, 7, 5, 5, 1, 1, 6, 6, 6, 6, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4]
        elif smer==8:
            chs=[1, 7, 6, 6, 3, 3, 2, 2, 2, 2, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0]
        #print smer
        pravs = []
        for i in range(0,8):
            pravs.append(random.choice(chs))
            while pravs[i] in chs: chs.remove(pravs[i])
        for i in range(0, 8):
            prav = pravs.pop(0)
            if curx > 0 and prav == 0: #gore
                if mat[curx-1][cury] > 0 and riched[curx-1][cury] == -2:
                    ukpp += mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0
                    if rec(curx-1, cury, ind + mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0):
                        return True
                    ukpp += mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0
                    co -= 1
                    arco += 1
            if curx < rows-1 and prav == 1: #dole
                if mat[curx+1][cury] > 0 and riched[curx+1][cury] == -2:
                    ukpp += mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0
                    if rec(curx+1, cury, ind + mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0):
                        return True
                    ukpp += mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0
                    co -= 1
                    arco += 1
            if cury > 0 and prav == 2: #levo
                if mat[curx][cury-1] > 0 and riched[curx][cury-1] == -2:
                    ukpp += mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0
                    if rec(curx, cury-1, ind + mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0):
                        return True
                    ukpp += mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0
                    co -= 1
                    arco += 1
            if cury < cols-1 and prav == 3: #desno
                if mat[curx][cury+1] > 0 and riched[curx][cury+1] == -2:
                    ukpp += mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0
                    if rec(curx, cury+1, ind + mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0):
                        return True
                    ukpp += mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0
                    co -= 1
                    arco += 1
            if curx > 0 and cury > 0 and prav == 4: #gore-levo
                if mat[curx-1][cury-1] > 0 and riched[curx-1][cury-1] == -2:
                    ukpp += (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    if rec(curx-1, cury-1, ind + (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                        return True
                    ukpp += (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    co -= 1
                    arco += 1
            if curx > 0 and cury < cols-1 and prav == 5: #gore-desno
                if mat[curx-1][cury+1] > 0 and riched[curx-1][cury+1] == -2:
                    ukpp += (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    if rec(curx-1, cury+1, ind + (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                        return True
                    ukpp += (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    co -= 1
                    arco += 1
            if curx < rows-1 and cury > 0 and prav == 6: #dole-levo
                if mat[curx+1][cury-1] > 0 and riched[curx+1][cury-1] == -2:
                    ukpp += (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    if rec(curx+1, cury-1, ind + (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                        return True
                    ukpp += (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    co -= 1
                    arco += 1
            if curx < rows-1 and cury < cols-1 and  prav == 7: #dole-desno
                if mat[curx+1][cury+1] > 0 and riched[curx+1][cury+1] == -2:
                    ukpp += (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    if rec(curx+1, cury+1, ind + (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                        return True
                    ukpp += (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                    co -= 1
                    arco += 1
            prav += 1
            if prav==8: prav = 0
        #co -= 1
        #arco += 1
        return False

    posttime = time.time()
    for it in range(0, its):
        if its < 100: print '\rOdradjeno:', it*100/its, '%',
        elif it%(its/100)==0:  print '\rOdradjeno:', it*100/its, '%',
        riched = [[-2 for i in range(cols)] for j in range(rows)]
        succ = False
        ukpp = 0
        arco = 0
        co = 0
        starttime = time.time()
        endtime = starttime
        succ = rec(startx, starty, 0)
        #co -= 1
        tlap = endtime-starttime
        if succ:
            if minarco == -1 or (minarco > arco): minarco = arco
            if minco == -1 or (minco > co): minco = co
            if minrich == -1 or (minrich > riched[endx][endy]):
                minrich = riched[endx][endy]
            if mintlap == -1 or (mintlap > tlap): mintlap = tlap
            if minukp == -1 or (minukp > ukpp): minukp = ukpp
            avrukp += ukpp
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
    print 'Srednji ukupan broj poteza: ', avrukp/float(nstits if nstits>0 else 1)
    print 'Najmanji ukupan broj poteza: ', minukp
    print 'Srednji broj poteza do cilja: ', avrrich/float(nstits if nstits>0 else 1)
    print 'Najmanji broj poteza do ciljla: ', minrich
    print 'Broj pronadjenih u ogranicenju od', timewait, 's: ', avrsucc/float(its)*100, '%'
    print 'Srednje vreme izvrsavanja: ', avrtlap/float(nstits if nstits>0 else 1)
    print 'Broj uspesnih: ', nstits, ' / ', its
    print 'Najmanje vreme izvrsavanja: ', mintlap
    print 'Ukupno vreme: ', poentime-posttime
    print 'Kraj'
    fw = open('outdata.txt', 'a')
    fw.write(str(avrtlap/float(nstits if nstits>0 else 1))+'\n'+str(avrarco/float(nstits if nstits>0 else 1))+'\n'+str(avrco/float(nstits if nstits>0 else 1))+'\n'+str(avrukp/float(nstits if nstits>0 else 1))+'\n')
    fw.close()
