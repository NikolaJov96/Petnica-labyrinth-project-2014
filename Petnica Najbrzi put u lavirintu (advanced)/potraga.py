import random
import time
from math import sqrt
import init

stack = []
succ = False
mat = []
riched = []
nodes = []

def calcpotraga():
    global succ, stack, rows, cols, startx, starty, endx, endy, mat, matcov, riched, co, arco, nodes, found, heur
    rows = init.rows
    cols = init.cols
    startx = init.startx
    starty = init.starty
    endx = init.endx
    endy = init.endy
    seerange = init.seerange
    mat = init.mat
    succ + False
    sqrt2 = 1.41
    co = 0
    arco = 0
    found = [[-1 for i in range(cols)] for j in range(rows)]
    heur = [[sqrt((j-endx)**2+(i-endy)**2) for i in range(cols)] for j in range(rows)] #(abs(j-endx)+abs(i-endy))
    matcov = 0
    matp = rows*cols
    stack = []
    riched = [[-2 for i in range(cols)] for j in range(rows)]

    def newmat(cx, cy):
        global matcov
        for i in range(-seerange, seerange+1):
            for j in range(-seerange, seerange+1):
                if cx+i>=0 and cx+i<rows and cy+j>=0 and cy+j<cols and sqrt(i**2 + j**2) <= seerange and found[cx+i][cy+j] == -1:
                    found[cx+i][cy+j] = mat[cx+i][cy+j]
                    matcov += 1

    # 1-gore 2 3-desno 4 5-dole 6 7-levo 8
    def finddir(cx, cy, ex, ey):
        if ey==cy and cx>ex: return 0
        elif ey>cy and ex==cx: return 3
        elif ey==cy and ex>cx: return 1
        elif ey<cy and ex==cx: return 2
        elif (ex-cx)==(ey-cy) and ex<cx: return 5
        elif (ex-cx)==(ey-cy) and ex>cx: return 5
        elif (ex-cx)==-(ey-cy) and ex>cx: return 7
        elif (ex-cx)==-(ey-cy) and ex<cx: return 4
        elif ex>cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 1
        elif ex>cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 6
        elif ex>cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 2
        elif ex<cx and ey<cy and abs(ex-cx)<abs(ey-cy): return 4
        elif ex<cx and ey<cy and abs(ex-cx)>abs(ey-cy): return 0
        elif ex<cx and ey>cy and abs(ex-cx)>abs(ey-cy): return 5
        elif ex<cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 3
        elif ex>cx and ey>cy and abs(ex-cx)<abs(ey-cy): return 7
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

    def undectaround(x, y):
        if x > 0:
            if found[x-1][y] == -1: return True
        if x < rows-1:
            if found[x+1][y] == -1: return True
        if y > 0:
            if found[x][y-1] == -1: return True
        if y < cols-1:
            if found[x][y+1] == -1: return True
        if x > 0 and y > 0:
            if found[x-1][y-1] == -1: return True
        if x > 0 and y < cols-1:
            if found[x-1][y+1] == -1: return True
        if x < rows-1 and y > 0:
            if found[x+1][y-1] == -1: return True
        if x < rows-1 and y < rows-1:
            if found[x+1][y+1] == -1: return True
        return False

    def makesuglist(cx, cy, cos): #A* za pronadjeni deo matrice
        global suglist, co, arco, nodes
        nodes = [[[j, i, heur[j][i], 0, (-1, -1), -1, -1] for i in range(cols)] for j in range(rows)]
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

        def chnode(x, y, dx, dy, di):
            weig = (mat[x+dx][y+dy]/2.0 + mat[x][y]/2.0)
            if dx != 0 and dy != 0: weig = weig * sqrt2
            if found[x+dx][y+dy] > 0 and not ((x+dx,y+dy) in closelist) :
                if not((x+dx,y+dy) in openlist):
                    nodes[x+dx][y+dy][4] = (x,y)
                    nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                    nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]
                    nodes[x+dx][y+dy][6] = di
                    appendnode(x+dx,y+dy)
                elif nodes[x+dx][y+dy][5] > nodes[x][y][5] + weig:
                    nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                    nodes[x+dx][y+dy][4] = (x,y)
                    nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]
                    nodes[x+dx][y+dy][6] = di

        while openlist:
            global stack
            cur = openlist.pop()
            closelist.append(cur)
            if (cur[0], cur[1]) == (endx, endy):
                #print 'Found'
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
                return True
            asdir = nodes[cur[0]][cur[1]][6]
            if (cur[0], cur[1], -1, False) in suglist:
                suglist[suglist.index((cur[0], cur[1], -1, False))] = (cur[0], cur[1], asdir, True)
            if cur[0] > 0:
                if cur[0] == cx and cur[1] == cy:
                    chnode(cur[0], cur[1], -1, 0, 0)
                else: chnode(cur[0], cur[1], -1, 0, asdir)
                    #print 'a'
                    #asdir = 0
            if cur[0] < rows-1:
                if cur[0] == cx and cur[1] == cy:
                    chnode(cur[0], cur[1], 1, 0, 1)
                else: chnode(cur[0], cur[1], 1, 0, asdir)
                    #print 'a'
                    #asdir = 1
            if cur[1] > 0: 
                if cur[0] == cx and cur[1] == cy:
                    chnode(cur[0], cur[1], 0, -1, 2)
                else: chnode(cur[0], cur[1], 0, -1, asdir)
                    #print 'a'
                    #asdir = 2
            if cur[1] < cols-1: 
                if cur[0] == cx and cur[1] == cy: 
                    chnode(cur[0], cur[1], 0, 1, 3)
                else: chnode(cur[0], cur[1], 0, 1, asdir)
                    #print 'a'
                    #asdir = 3
            if cur[0] > 0 and cur[1] > 0:
                if mat[cur[0]][cur[1]-1] != 0 or mat[cur[0]-1][cur[1]] != 0:
                    if cur[0] == cx and cur[1] == cy: 
                        chnode(cur[0], cur[1], -1, -1, 4)
                    else: chnode(cur[0], cur[1], -1, -1, asdir)
                        #print 'a'
                        #asdir = 4
            if cur[0] > 0 and cur[1] < cols-1:
                if mat[cur[0]][cur[1]+1] != 0 or mat[cur[0]-1][cur[1]] != 0:
                    if cur[0] == cx and cur[1] == cy: 
                        chnode(cur[0], cur[1], -1, 1, 5)
                    else: chnode(cur[0], cur[1], -1, 1, asdir)
                        #print 'a'
                        #asdir = 5
            if cur[0] < rows-1 and cur[1] > 0:
                if mat[cur[0]][cur[1]-1] != 0 or mat[cur[0]+1][cur[1]] != 0:
                    if cur[0] == cx and cur[1] == cy: 
                        chnode(cur[0], cur[1], 1, -1, 6)
                    else: chnode(cur[0], cur[1], 1, -1, asdir)
                        #print 'a'
                        #asdir = 6
            if cur[0] < rows-1 and cur[1] < cols-1:
                if mat[cur[0]][cur[1]+1] != 0 or mat[cur[0]+1][cur[1]] != 0:
                    if cur[0] == cx and cur[1] == cy: 
                        chnode(cur[0], cur[1], 1, 1, 7)
                    else: chnode(cur[0], cur[1], 1, 1, asdir)
                        #print 'a'
                        #asdir = 7

    print 'Potraga:'
    def rec(curx, cury, ind):
        parentdir = 9
        parentx = -1
        parenty = -1
        if ind <> 0: 
            parentx = stack[len(stack)-1][0]
            parenty = stack[len(stack)-1][1]
            parentdir = finddir(curx, cury, parentx, parenty)
        stack.append((curx, cury))
        global co, arco, endtime, matcov, suglist, riched
        print '\rPolja poseceno:', matcov, 'od', matp,
        riched[curx][cury] = ind
        co += 1
        arco += 1
        if curx == endx and cury == endy: return True   
        #smer = finddir(curx, cury, endx, endy)
        newmat(curx, cury)
        isk = []
        pravs = []
        suglist = []
        def initsuglist(curx, cury):
            global pravs, suglist, cols, rows, found, nodes, heur, endx, endy
            suglist = []
            for i in range(0,rows):
                for j in range(0,cols):
                    if undectaround(i, j) and found[i][j] > 0:
                        suglist.append((i, j, -1, False))
            suglist.sort(key=lambda x: heur[x[0]][x[1]])
            suglistzad = 0
            #while len(suglist)>10: suglist.pop(10)
            if makesuglist(curx, cury, ind): return True
            suglist.sort(key=lambda x: nodes[x[0]][x[1]][5] + heur[x[0]][x[1]])
            asdir = suglist[0][2]
            if asdir == -1:
                asdir = finddir(curx, cury, endx, endy)
            chs=[]
            if asdir==0:
                chs=[0, 4, 5, 2, 3, 6, 7, 1]
            elif asdir==1:
                chs=[1, 6, 7, 2, 3, 4, 5, 0]
            elif asdir==2:
                chs=[2, 4, 6, 0, 1, 5, 7, 3]
            elif asdir==3:
                chs=[3, 5, 7, 0, 1, 4, 6, 2]
            elif asdir==4:
                chs=[4, 2, 0, 6, 5, 1, 3, 7]
            elif asdir==5:
                chs=[5, 0, 3, 4, 7, 2, 1, 6]
            elif asdir==6:
                chs=[6, 1, 2, 7, 4, 3, 0, 5]
            elif asdir==7:
                chs=[7, 3, 1, 5, 6, 0, 2, 4]
            chs=[9, 10, 11, 12, 13, 14, 15, 16]  #################################################
            pravs = []
            while suglist:
                if suglist[0][3] == False: suglist.pop(0)
                elif suglist[0][2] not in pravs:
                    pravs.append(suglist[0][2])
                    sug = suglist.pop(0)
                    while sug in chs: chs.remove(sug)
                else: suglist.pop(0)
            while chs:
                cu = chs[0]
                if cu not in pravs: pravs.append(cu)
                while cu in chs: chs.remove(cu)
            #for op in isk:
            #    if op in pravs:
            #        pravs.remove(op)
            #print isk, pravs
            #isk.append(pravs[0])
            return pravs
        # if len(pravs) != 8: print pravs
        # pravs = initsuglist(curx, cury)
        isk = []
        for i in range(0, 8):
            pravs = initsuglist(curx, cury)
            if pravs == True: return True
            while pravs[0] in isk: pravs.pop(0)
            prav = pravs.pop(0)
            if prav > 8: #pravs[0] == parentdir:
                stack.append((parentx, parenty))
                return False
            isk.append(prav)
            if curx > 0 and prav == 0: #gore
                if mat[curx-1][cury] > 0 and riched[curx-1][cury] == -2:
                    if rec(curx-1, cury, ind + mat[curx-1][cury]/2.0 + mat[curx][cury]/2.0):
                        return True
            if curx < rows-1 and prav == 1: #dole
                if mat[curx+1][cury] > 0 and riched[curx+1][cury] == -2:
                    if rec(curx+1, cury, ind + mat[curx+1][cury]/2.0 + mat[curx][cury]/2.0):
                        return True
            if cury > 0 and prav == 2: #levo
                if mat[curx][cury-1] > 0 and riched[curx][cury-1] == -2:
                    if rec(curx, cury-1, ind + mat[curx][cury-1]/2.0 + mat[curx][cury]/2.0):
                        return True
            if cury < cols-1 and prav == 3: #desno
                if mat[curx][cury+1] > 0 and riched[curx][cury+1] == -2:
                    if rec(curx, cury+1, ind + mat[curx][cury+1]/2.0 + mat[curx][cury]/2.0):
                        return True
            if curx > 0 and cury > 0 and prav == 4: #gore-levo
                if mat[curx-1][cury-1] > 0 and riched[curx-1][cury-1] == -2:
                    if mat[curx][cury-1] != 0 or mat[curx-1][cury] != 0:
                        if rec(curx-1, cury-1, ind + (mat[curx-1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                            return True
            if curx > 0 and cury < cols-1 and prav == 5: #gore-desno
                if mat[curx-1][cury+1] > 0 and riched[curx-1][cury+1] == -2:
                    if mat[curx][cury+1] != 0 or mat[curx-1][cury] != 0:
                        if rec(curx-1, cury+1, ind + (mat[curx-1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                            return True
            if curx < rows-1 and cury > 0 and prav == 6: #dole-levo
                if mat[curx+1][cury-1] > 0 and riched[curx+1][cury-1] == -2:
                    if mat[curx][cury-1] != 0 or mat[curx+1][cury] != 0:
                        if rec(curx+1, cury-1, ind + (mat[curx+1][cury-1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                            return True
            if curx < rows-1 and cury < cols-1 and  prav == 7: #dole-desno
                if mat[curx+1][cury+1] > 0 and riched[curx+1][cury+1] == -2:
                    if mat[curx][cury+1] != 0 or mat[curx+1][cury] != 0:
                        if rec(curx+1, cury+1, ind + (mat[curx+1][cury+1]/2.0 + mat[curx][cury]/2.0)*sqrt2):
                            return True
        co -= 1
        arco += 1
        stack.append((parentx, parenty))
        return False
    
    starttime = time.time()
    succ = rec(startx, starty, 0)
    endtime = time.time()
    co -= 1
    arco -= 1
    tlap = endtime-starttime
    poentime = time.time()
    print
    print 'Upesno: ', succ
    print 'Broj predjenih koraka: ', arco
    print 'Najmanji broj poteza: ', nodes[endx][endy][5]
    print 'Ukupno vreme: ', tlap
    print 'Kraj'
    fw = open('outdata.txt', 'a')
    fw.write(str(tlap)+'\n'+str(arco)+'\n'+str(co)+'\n'+str(nodes[endx][endy][5])+'\n')
    fw.close()

def viz():
    print 'Vizualizacija:'
    for i in range(0,rows):
        for j in range(0,cols):
            if i==startx and j==starty: print 'S ',
            elif i==endx and j==endy: print 'E ',
            elif (i,j) in stack: print 'O ',
            elif mat[i][j]==0: print 'x ',
            elif mat[i][j]>1: print '* ',
            else: print '_',
        print

def vizdata():
    global stack
    fw = open('outdata.txt', 'a')
    for i in range(0,rows):
        for j in range(0,cols):
            if i==startx and j==starty: fw.write('S')
            elif i==endx and j==endy: fw.write('E')
            elif (i,j) in stack: fw.write ('O')
            elif mat[i][j]==0: fw.write ('x')
            elif mat[i][j]>1: fw.write ('*')
            else: fw.write ('_')
        fw.write('\n')
    fw.close()
