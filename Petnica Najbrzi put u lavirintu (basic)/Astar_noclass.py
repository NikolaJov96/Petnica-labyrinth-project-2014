import time
from init import *

reinit()

"""class node:
    def __init__(self, x, y, he):
        self.x = x
        self.y = y
        self.heuris = he
    ind = 0
    parent = None
    cost = -1"""

#nodes = [[node for i in range(cols)] for j in range(rows)]
# nodes: x, y, heuristic, index, parent(x,y), cost
nodes = [[[j, i, abs(endx-j)+abs(endy-i), 0, (-1, -1), -1] for i in range(cols)] for j in range(rows)]

"""for i in range(0, rows):
    for j in range (0, cols):
        #nodes[i][j] = node(i, j, abs(endx-i)+abs(endy-j))
        nodes[i][j][0] = i
        nodes[i][j][1] = j
        nodes[i][j][2] = abs(endx-i)+abs(endy-j)"""

#nodes[startx][starty].cost = 0
nodes[startx][starty][5] = 0
openlist = [(startx, starty)]
closelist = []
usteps = 0

#def appendnode(nd):
def appendnode(x, y):
    if openlist:
        i = len(openlist)-1
        #if (x,y) == (12,6): print i,
        #while nd.ind > openlist[i].ind:
        while nodes[x][y][3] > nodes[openlist[i][0]][openlist[i][1]][3]:
            i -= 1
            if i == -1: break
        openlist.insert(i+1, (x,y))
    else: openlist.append((x,y))

def chnode(x, y, dx, dy):
    weig = max(mat[x+dx][y+dy], mat[x][y])
    if mat[x+dx][y+dy] > 0 and not ((x+dx,y+dy) in closelist) :
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
    cur = openlist.pop() # cur je tuple (x,y) trenutne celije
    closelist.append(cur)
    if cur[0] == endx and cur[1] == endy:
        succ = True
        break
    if cur[0] > 0: chnode(cur[0], cur[1], -1, 0)
    if cur[0] < rows-1: chnode(cur[0], cur[1], 1, 0)
    if cur[1] > 0: chnode(cur[0], cur[1], 0, -1)
    if cur[1] < cols-1: chnode(cur[0], cur[1], 0, 1)
endtime = time.time()

print 'Pretraga uspela: ', bool(succ)
print 'Trajanje: ', endtime-starttime

"""for i in range(0,rows):    #ispis posecenih nodova
    for j in range(0,cols):
        if nodes[i][j] in closelist: print 'p',
        else: print 'n',
    print"""

if succ:
    stack = []
    steps = 0
    #while cur != nodes[startx][starty]:
    while cur != (startx,starty):
        steps += 1
        stack.append((cur[0], cur[1]))
        cur = nodes[cur[0]][cur[1]][4]
    stack.append((cur[0], cur[1]))
        
    print 'Broj koraka: ', steps
    #print 'Koraci: ', stack
    print 'Broj poteza: ', nodes[endx][endy][5]

    
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

def gettime():
    return endtime-starttime

def retsucc():
    return succ
