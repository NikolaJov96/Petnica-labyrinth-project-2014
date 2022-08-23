import random
import time
from math import sqrt
from init import *

reinit()
        
seerange = 20
found = [[-1 for i in range(cols)] for j in range(rows)]
heur = [[(abs(j-endx)+abs(i-endy)) for i in range(cols)] for j in range(rows)]
matcov = 0
matp = rows*cols
stack = []

def newmat(cx, cy):
    global matcov
    for i in range(-seerange, seerange+1):
        for j in range(-seerange, seerange+1):
            if cx+i>=0 and cx+i<rows and cy+j>=0 and cy+j<cols and sqrt(i**2 + j**2) <= seerange and found[cx+i][cy+j] == -1:
                found[cx+i][cy+j] = mat[cx+i][cy+j]
                matcov += 1

# 1-gore 2 3-desno 4 5-dole 6 7-levo 8
def finddir(cx, cy, ex, ey):
    if ey==cy and cx>ex: return 8
    elif ey>cy and ex==cx: return 2
    elif ey==cy and ex>cx: return 4
    elif ey<cy and ex==cx: return 6
    elif (ex-cx)==(ey-cy) and ex<cx: return 1
    elif (ex-cx)==(ey-cy) and ex>cx: return 5
    elif (ex-cx)==-(ey-cy) and ex>cx: return 3
    elif (ex-cx)==-(ey-cy) and ex<cx: return 7
    elif ex>cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 4
    elif ex>cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 5
    elif ex>cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 6
    elif ex<cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 7
    elif ex<cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 8
    elif ex<cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 1
    elif ex<cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 2
    elif ex>cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 3
    else: return 9

cx = startx
cy = starty

endtime = 0
starttime = 0

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

nodes = [[[j, i, heur[j][i], 0, (-1, -1), -1] for i in range(cols)] for j in range(rows)]
smer = finddir(cx, cy, endx, endy)
suglist = []
asdir = 0

def undectaround(x, y):
    if x > 0:
        if found[x-1][y] == -1: return True
    if x < rows-1:
        if found[x+1][y] == -1: return True
    if y > 0:
        if found[x][y-1] == -1: return True
    if y < cols-1:
        if found[x][y+1] == -1: return True
    return False

def makesuglist(cx, cy, cos): #A* za pronadjeni deo matrice
    global suglist, co, arco, nodes
    nodes = [[[j, i, heur[j][i], 0, (-1, -1), -1] for i in range(cols)] for j in range(rows)]
    nodes[cx][cy][5] = cos
    openlist = [(cx, cy)]
    closelist = []
    def appendnode(x,y):
        if openlist:
            i = len(openlist)-1
            while nodes[x][y][3] > nodes[openlist[i][0]][openlist[i][1]][3]:
                i -= 1
                if i == -1: break
            openlist.insert(i+1, (x,y))
        else: openlist.append((x,y))

    def chnode(x, y, dx, dy):
        weig = max(mat[x+dx][y+dy], mat[x][y])
        if found[x+dx][y+dy] > 0 and not ((x+dx,y+dy) in closelist) :
            if not((x+dx,y+dy) in openlist):
                nodes[x+dx][y+dy][4] = (x,y)
                nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]
                appendnode(x+dx,y+dy)
            elif nodes[x+dx][y+dy][5] > nodes[x][y][5] + weig:
                nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                nodes[x+dx][y+dy][4] = (x,y)
                nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]

    while openlist:
        global asdir, stack
        #global suglist
        cur = openlist.pop()
        #if (cur[0] == viewx1) or (cur[0] == viewx2) or (cur[1] == viewy1) or (cur[1] == viewy2):
        if (cur[0], cur[1]) == (endx, endy):
            print 'Found'
            #print nodes[endx][endy][4][0], nodes[endx][endy][4][1]
            #print nodes[nodes[endx][endy][4][0]][nodes[endx][endy][4][1]][0], nodes[nodes[endx][endy][4][0]][nodes[endx][endy][4][1]][1]
            ln = len(stack)
            nx = endx
            ny = endy
            while nx!=cx or ny!=cy:
                arco += 1
                co += 1
                stack.insert(ln, (nx, ny))
                pom = nx
                nx = nodes[nx][ny][4][0]
                ny = nodes[pom][ny][4][1]
                #print nx, ny
                #print 'rty', stack
            return True
        if (cur[0], cur[1], -1, False) in suglist:
            suglist[suglist.index((cur[0], cur[1], -1, False))] = (cur[0], cur[1], asdir, True)
        closelist.append(cur)
        if cur[0] > 0:
            asdir = 0
            chnode(cur[0], cur[1], -1, 0)
        if cur[0] < rows-1:
            asdir = 1
            chnode(cur[0], cur[1], 1, 0)
        if cur[1] > 0: 
            asdir = 2
            chnode(cur[0], cur[1], 0, -1)
        if cur[1] < cols-1: 
            asdir = 3
            chnode(cur[0], cur[1], 0, 1)
    #return False
        #global it, arco
        #if it == 0 and arco == 2 and (cur[0],cur[1])==(startx,starty): 
        #    for h in found:
        #        print h
        #    print cur[0], cur[1]
        #    print len(suglist), suglist

            

print 'Potraga:'
def rec(curx, cury, ind):
    stack.append((curx, cury))
    global co, arco, endtime, matcov
    print '\rPolja poseceno:', matcov, 'od', matp,
    riched[curx][cury] = ind
    co += 1
    arco += 1
    if curx == endx and cury == endy: return True
    #endtime = time.time()
    #if endtime-starttime > timewait and timewait!=-1: return False    
    smer = finddir(curx, cury, endx, endy)
    newmat(curx, cury)

    suglist = []
    for i in range(0,rows):
        for j in range(0,cols):
            if undectaround(i, j) and found[i][j] > -1:
                suglist.append((i, j, -1, False))
    suglist.sort(key=lambda x: heur[x[0]][x[1]])
    while len(suglist)>10: suglist.pop(10)
    #if arco == 1:
    #    for x in suglist: print (heur[x[0]][x[1]], x[0], x[1])
    #    print
    
    if makesuglist(curx, cury, ind): return True
    suglist.sort(key=lambda x: nodes[x[0]][x[1]][5] + heur[x[0]][x[1]])
    global it
    
    #for i in range(0,len(suglist)-1):
        #minudi = i
        #for j in range(i+1,len(suglist)):
        #    if riched[suglist[j][0]][suglist[j][1]] + heur[suglist[j][0]][suglist[j][1]] < riched[suglist[minudi][0]][suglist[minudi][1]] + heur[suglist[minudi][0]][suglist[minudi][1]]:
        #        minudi = i

        #pom = suglist[minudi]
        #suglist[minudi] = suglist[i]
        #suglist[i] = pom
        
    #if arco == 1 and it == 0:
        #print len(suglist), suglist
        #for l in suglist:
        #    print l[0], l[1], riched[l[0]][l[1]]+heur[l[0]][l[1]]
        #for h in found:
        #    print h
        #for l in suglist: print '[', l[0]-startx, l[1]-starty, ']',
        #print

    chs=[]
    if smer==1:
        chs=[0, 3, 2, 1]
    elif smer==2:
        chs=[3, 0, 1, 2]
    elif smer==3:
        chs=[3, 1, 0, 2]
    elif smer==4:
        chs=[1, 3, 2, 0]
    elif smer==5:
        chs=[1, 2, 3, 0]
    elif smer==6:
        chs=[2, 1, 0, 3]
    elif smer==7:
        chs=[2, 0, 1, 3]
    elif smer==8:
        chs=[0, 2, 3, 1]
        
    pravs = []
    while suglist:
        if suglist[0][2] == -1: suglist.pop(0)
        elif suglist[0][2] not in pravs:
            pravs.append(suglist[0][2])
            suglist.pop(0)
            while suglist[0][2] in chs: chs.remove(suglist[0][2])
        else: suglist.pop(0)
    
    while chs:
        cu = chs[0]
        pravs.append(cu)
        while cu in chs: chs.remove(cu)
    if len(pravs) != 4: print pravs
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
        #prav += 1
        #if prav==4: prav = 0
    co -= 1
    arco += 1
    return False

#for it in range(0, its):
#    if its < 100: print '\rOdradjeno:', it*100/its, '%',
#    elif it%(its/100)==0:  print '\rOdradjeno:', it*100/its, '%',
#    from init import *
#    reinit()
#    found = [[-1 for i in range(cols)] for j in range(rows)]
starttime = time.time()
succ = rec(startx, starty, 0)
endtime = time.time()
#    endtime = time.time()
co -= 1
arco -= 1
tlap = endtime-starttime
#    if succ:
#        if minarco == -1 or (minarco > arco): minarco = arco
#        if minco == -1 or (minco > co): minco = co
#       if minrich == -1 or (minrich > riched[endx][endy]):
#            minrich = riched[endx][endy]
#        if mintlap == -1 or (mintlap > tlap): mintlap = tlap
#        avrarco += arco
#        avrco += co
#        avrsucc += 1
#        avrrich += riched[endx][endy]
#        avrtlap += tlap if tlap<timewait else 0
#    succ = False
#    if tlap>timewait: nstits-=1
poentime = time.time()
print
print 'Upesno: ', succ
#print '\rOdradjeno:  100 %'
#print 'Srednji broj predjenih koraka: ', avrarco/float(nstits if nstits>0 else 1)
print 'Broj predjenih koraka: ', arco
#print 'Srednji Broj koraka do cilja: ', avrco/float(nstits if nstits>0 else 1)
print 'Najmanji otkriveni broj koraka do cilja: ', co
#print 'Srednji broj poteza: ', avrrich/float(nstits if nstits>0 else 1)
print 'Najmanji broj poteza: ', nodes[endx][endy][5]#riched[endx][endy]
#print 'Broj pronadjenih u ogranicenju od', timewait, 's: ', avrsucc/float(its)*100, '%'
#print 'Srednji vreme izvrsavanja: ', avrtlap/float(nstits if nstits>0 else 1)
#print 'Broj uspesnih: ', nstits, ' / ', its
#print 'Najmanje vreme izvrsavanja: ', mintlap
print 'Ukupno vreme: ', tlap
print 'Kraj'


def viz():
    print 'Vizualizacija:'
    for i in range(0,rows):
        for j in range(0,cols):
            if i==startx and j==starty: print 'S',
            elif i==endx and j==endy: print 'E',
            elif (i,j) in stack: print 'O',
            elif mat[i][j]==0: print 'x',
            else: print '_',
        print
