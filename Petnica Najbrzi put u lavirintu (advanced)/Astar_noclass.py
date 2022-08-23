import time
from math import sqrt
import init

succ = False
stack = []

def calcAstar():
    global succ, stack, rows, cols, startx, starty, endx, endy, mat, sqrt2
    rows = init.rows
    cols = init.cols
    startx = init.startx
    starty = init.starty
    endx = init.endx
    endy = init.endy
    succ = False
    mat = init.mat
    sqrt2 = 1.41

    # nodes: x, y, heuristic, index, parent(x,y), cost
    nodes = [[[j, i, sqrt((endx-j)**2+(endy-i)**2)/5.0, 0, (-1, -1), -1] for i in range(cols)] for j in range(rows)]

    nodes[startx][starty][5] = 0
    openlist = [(startx, starty)]
    closelist = []
    usteps = 0

    def appendnode(x, y):
        if openlist:
            i = len(openlist)-1
            while nodes[x][y][3] > nodes[openlist[i][0]][openlist[i][1]][3]:
                i -= 1
                if i == -1: break
            openlist.insert(i+1, (x,y))
        else: openlist.append((x,y))

    def chnode(x, y, dx, dy):
        weig = mat[x+dx][y+dy]/2.0 + mat[x][y]/2.0
        if dx != 0 and dy != 0: weig = weig*sqrt2
        if mat[x+dx][y+dy] > 0 and not ((x+dx,y+dy) in closelist):
            if not((x+dx,y+dy) in openlist):
                nodes[x+dx][y+dy][4] = (x,y)
                nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]
                appendnode(x+dx,y+dy)
            elif nodes[x+dx][y+dy][5] > nodes[x][y][5] + weig:
                nodes[x+dx][y+dy][5] = nodes[x][y][5] + weig
                nodes[x+dx][y+dy][4] = (x,y)
                nodes[x+dx][y+dy][3] = nodes[x+dx][y+dy][5] + nodes[x+dx][y+dy][2]

    print 'A* bez klasa:'
    starttime = time.time()
    while openlist:
        usteps += 1
        cur = openlist.pop()
        closelist.append(cur)
        if cur[0] == endx and cur[1] == endy:
            succ = True
            break
        if cur[0] > 0: chnode(cur[0], cur[1], -1, 0)
        if cur[0] < rows-1: chnode(cur[0], cur[1], 1, 0)
        if cur[1] > 0: chnode(cur[0], cur[1], 0, -1)
        if cur[1] < cols-1: chnode(cur[0], cur[1], 0, 1)
        if cur[0] > 0 and cur[1] > 0:
            if mat[cur[0]][cur[1]-1] != 0 or mat[cur[0]-1][cur[1]] != 0:
                chnode(cur[0], cur[1], -1, -1)
        if cur[0] > 0 and cur[1] < cols-1:
            if mat[cur[0]][cur[1]+1] != 0 or mat[cur[0]-1][cur[1]] != 0:
                chnode(cur[0], cur[1], -1, 1)
        if cur[0] < rows-1 and cur[1] > 0:
            if mat[cur[0]][cur[1]-1] != 0 or mat[cur[0]+1][cur[1]] != 0:
                chnode(cur[0], cur[1], 1, -1)
        if cur[0] < rows-1 and cur[1] < cols-1:
            if mat[cur[0]][cur[1]+1] != 0 or mat[cur[0]+1][cur[1]] != 0:
                chnode(cur[0], cur[1], 1, 1)
    endtime = time.time()

    print 'Pretraga uspela: ', bool(succ)
    print 'Trajanje: ', endtime-starttime
    fw = open('outdata.txt', 'a')
    fw.write(str(succ)+'\n')

    if succ:
        stack = []
        steps = 0
        while cur != (startx,starty):
            steps += 1
            stack.append((cur[0], cur[1]))
            cur = nodes[cur[0]][cur[1]][4]
        stack.append((cur[0], cur[1]))
            
        print 'Broj koraka: ', steps
        print 'Broj poteza: ', nodes[endx][endy][5]
        fw = open('outdata.txt', 'a')
        fw.write(str(endtime-starttime)+'\n'+str(steps)+'\n'+str(nodes[endx][endy][5])+'\n')
    fw.close()
    print 'Kraj'
    
def viz():
    global stack
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

def retsucc():
    global succ
    return succ
