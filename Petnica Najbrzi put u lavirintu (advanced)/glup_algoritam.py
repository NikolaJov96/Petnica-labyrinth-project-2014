import random
import sys
import time
from math import sqrt
import init

global co, arco, endx, endy, startx, starty, randnum, ukpp

co = 0
arco = 0
endx = 0
endy = 0
startx = 0
starty = 0
randnum = 0
ukpp = 0

def calcglup_algoritam():
    global co, arco, endx, endy, startx, starty, ukpp
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
    sqrt2 = sqrt(2)
    sys.setrecursionlimit(2000)
    queue = [(startx, starty, 0, random.choice([0, 1, 2, 3]), 0.0, 0)]

    avrarco = 0
    avrco = 0
    avrsucc = 0
    avrrich = 0
    avrtlap = 0
    avrukp = 0.0

    endtime = 0

    minarco = -1
    minco = -1
    minrich = -1
    mintlap = -1
    minukp = -1.0

    its = init.rnditers
    nstits = its
    timewait = init.timewait

    gasttime = time.time()
    print 'Glup algoritam:'
    for it in range(0, its):
        if its < 100: print '\rOdradjeno:', it*100/its, '%',
        elif it%(its/100)==0:  print '\rOdradjeno:', it*100/its, '%',
        riched = [[-2 for i in range(cols)] for j in range(rows)]
        succ = False
        co = 0
        arco = 0
        lastco = -1
        ukpp = 0.0
        lastukpp = 0
        addcov = 0
        weigqueue = []
        queue = [(startx, starty, 0, random.choice([0, 1, 2, 3]), 0, 0.0)]
        weigqueue = [(0, 0.0)]
        randnum = random.randint(1, 10)
        starttime = time.time()
        endtime = starttime #def rec(curx, cury, ind, prav):
        while queue:
            queueind = len(queue)-1
            arr = queue.pop()
            curx = arr[0]
            cury = arr[1]
            ind = arr[2]
            prav = arr[3]
            riched[curx][cury] = ind
            #global co, arco, endtime, endx, endy
            co = arr[4]
            arco += 1
            ukpp = arr[5]
            if lastco >= co and lastco > 1:
                #print ukpp
                #queue[len(queue)-1] = (curx, cury, ind, prav, co, ukpp+2*(lastukpp-ukpp))
                #ukpp = queue[len(queue)-1][5]
                #print lastukpp, ukpp
                #ukpp = 2*(weigqueue.pop()[1]-weigqueue[co][1])
                #lastco -= 1
                while weigqueue[len(weigqueue)-1][0] > co: #weigqueue[len(weigqueue)-1][0] != co:
                    addcov += weigqueue.pop()[1]*2
                    #print 'as'
                    arco += 1
                addcov += weigqueue[len(weigqueue)-1][1]
                #weigqueue[len(weigqueue)-1] = (co, ukpp)
                #ukpp += weigqueue[len(weigqueue)-1][1]
                #if len(weigqueue)-1 != co: print co, len(weigqueue)
                #if len(weigqueue)-1 != lastco: print 'sdf'
                # povecavanje weiga za nod kad se na njega vrat drugi
                #weigqueue[len(weigqueue)-1] = (co, ukpp)
    
            #ukpp = arr[5]+ukpp
            #lastukpp = ukpp
            lastco = co
            if curx == endx and cury == endy:
                succ = True
                break
                #return True
            endtime = time.time()
            if endtime-starttime > timewait and timewait!=-1: break #return False
            #global randnum
            if randnum == 0: randnum = random.randint(1, 10)
            randnum -= 1
            for i in range(0, 8):
               if curx > 0 and prav == 0:
                    if mat[curx-1][cury] > 0 and riched[curx-1][cury] == -2:
                        #ukpp += mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0
                        weigqueue.append((co+1, mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0))
                        queue.append((curx-1, cury, ind + mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0 ,((prav+arco)%4 if (riched[curx-1][cury]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0))
                        #ukpp -= mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0
                        #if rec(curx-1, cury, ind + mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0 ,((prav+arco)%4 if (riched[curx-1][cury]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if curx < rows-1 and prav == 1:
                    if mat[curx+1][cury] > 0 and riched[curx+1][cury] == -2:
                        #ukpp += mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0
                        weigqueue.append((co+1, mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0))
                        queue.append((curx+1, cury, ind + mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx+1][cury]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0))
                        #ukpp -= mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0
                        #if rec(curx+1, cury, ind + mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx+1][cury]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if cury > 0 and prav == 2:
                    if mat[curx][cury-1] > 0 and riched[curx][cury-1] == -2:
                        #ukpp += mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0
                        weigqueue.append((co+1, mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0))
                        queue.append((curx, cury-1, ind + mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx][cury-1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0))
                        #ukpp -= mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0
                        #if rec(curx, cury-1, ind + mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx][cury-1]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if cury < cols-1 and prav == 3:
                    if mat[curx][cury+1] > 0 and riched[curx][cury+1] == -2:
                        #ukpp += mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0
                        weigqueue.append((co+1, mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0))
                        queue.append((curx, cury+1, ind + mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx][cury+1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0))
                        #ukpp -= mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0
                        #if rec(curx, cury+1, ind + mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0, ((prav+arco)%4 if (riched[curx][cury+1]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if curx > 0 and cury > 0 and prav == 4:
                    if mat[curx-1][cury-1] > 0 and riched[curx-1][cury-1] == -2:
                        #ukpp += (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        weigqueue.append((co+1, (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        queue.append((curx-1, cury-1, ind + (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx-1][cury-1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+(mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        #ukpp -= (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                         #if rec(curx-1, cury-1, ind + (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx-1][cury-1]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if curx > 0 and cury < cols-1 and prav == 5:
                    if mat[curx-1][cury+1] > 0 and riched[curx-1][cury+1] == -2:
                        #ukpp += (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        weigqueue.append((co+1, (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        queue.append((curx-1, cury+1, ind + (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx-1][cury+1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+(mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        #ukpp -= (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        #if rec(curx-1, cury+1, ind + (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx-1][cury+1]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if curx < rows-1 and cury > 0 and prav == 6:
                    if mat[curx+1][cury-1] > 0 and riched[curx+1][cury-1] == -2:
                        #ukpp += (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        weigqueue.append((co+1, (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        queue.append((curx+1, cury-1, ind + (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx+1][cury-1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+(mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        #ukpp -= (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        #if rec(curx+1, cury-1, ind + (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx+1][cury-1]==-2 and randnum!=0) else random.randint(0, 7))):
                            #return True
               if curx < rows-1 and cury < cols-1 and  prav == 7:
                    if mat[curx+1][cury+1] > 0 and riched[curx+1][cury+1] == -2:
                        #ukpp += (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        weigqueue.append((co+1, (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        queue.append((curx+1, cury+1, ind + (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx+1][cury+1]==-2 and randnum!=0) else random.randint(0, 7)), co+1, ukpp+(mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2))
                        #ukpp -= (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2
                        #if rec(curx+1, cury+1, ind + (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2, ((prav+arco)%4 if (riched[curx+1][cury+1]==-2 and randnum!=0) else random.randint(0, 7))):
                        #return True
               prav += 1
               if prav==8: prav = 0
            lastukpp = ukpp
            #weigqueue.append((co, ukpp)) # ne ukpp nego tezina prelaska
            #lastukpp = ukpp
            #arco += 1
             #return False
        # succ = rec(startx, starty, 0, random.choice([0, 1, 2, 3]))
        tlap = endtime-starttime
        if succ:
            ukpp += addcov
            #ukpp = queue.pop()[5]
            if minarco == -1 or (minarco > arco): minarco = arco
            if minco == -1 or (minco > co): minco = co
            if minrich == -1 or (minrich > riched[endx][endy]):
                minrich = riched[endx][endy]
            if mintlap == -1 or (mintlap > endtime-starttime): mintlap = tlap
            if minukp == -1 or (minukp > ukpp): minukp = ukpp
            avrukp += ukpp
            avrarco += arco
            avrco += co
            avrsucc += 1
            avrrich += riched[endx][endy]
            avrtlap += tlap if tlap<timewait else 0
        if tlap>timewait: nstits-=1
    gaentime = time.time()
    print '\rOdradjeno:  100 %'
    print 'Srednji broj predjenih koraka: ', avrarco/float(nstits if nstits>0 else 1)
    print 'Najmanji broj predjenih koraka: ', minarco
    print 'Srednji Broj koraka do cilja: ', avrco/float(nstits if nstits>0 else 1)
    print 'Najmanji Broj koraka do cilja: ', minco
    print 'Srednji ukupan broj poteza: ', avrukp/float(nstits if nstits>0 else 1)
    print 'Najmanji ukupan broj poteza: ', minukp
    print 'Srednji broj poteza: ', avrrich/float(nstits if nstits>0 else 1)
    print 'Najmanji broj poteza: ', minrich
    print 'Broj pronadjenih u ogranicenju od', timewait, 's: ', avrsucc/float(its)*100, '%'
    print 'Srednje vreme izvrsavanja: ', avrtlap/float(nstits if nstits>0 else 1)
    print 'Broj uspesnih: ', nstits, ' / ', its
    print 'Najmanje vreme izvrsavanja: ', mintlap
    print 'Ukupno vreme: ', gaentime-gasttime
    print 'Kraj'
    fw = open('outdata.txt', 'a')
    fw.write(str(avrtlap/float(nstits if nstits>0 else 1))+'\n'+str(avrarco/float(nstits if nstits>0 else 1))+'\n'+str(avrco/float(nstits if nstits>0 else 1))+'\n'+str(avrukp/float(nstits if nstits>0 else 1))+'\n')
    fw.close()
