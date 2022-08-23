import time
from init import *

reinit()

class node:
    def __init__(self, x, y, he):
        self.x = x
        self.y = y
        self.heuris = he
    ind = 0
    parent = None
    cost = -1

nodes = [[node for i in range(cols)] for j in range(rows)]
for i in range(0, rows):
    for j in range (0, cols):
        nodes[i][j] = node(i, j, abs(endx-i)+abs(endy-j))

nodes[startx][starty].cost = 0
openlist = [nodes[startx][starty]]
closelist = []
usteps = 0

def appendnode(nd):
    if openlist:
        i = len(openlist)-1
        while nd.ind > openlist[i].ind:
            i -= 1
            if i == -1: break
        openlist.insert(i+1, nd)
    else: openlist.append(nd)

print 'A*:'
starttime = time.time()
while openlist:
    usteps += 1
    cur = openlist.pop() # naci najmanji
    closelist.append(cur)
    if cur.x == endx and cur.y == endy:
        succ = True
        break
    if cur.x > 0:
        weig = max(mat[cur.x-1][cur.y], mat[cur.x][cur.y])
        if mat[cur.x-1][cur.y] > 0 and not (nodes[cur.x-1][cur.y] in closelist) :
            if not(nodes[cur.x-1][cur.y] in openlist):
                nodes[cur.x-1][cur.y].parent = cur
                nodes[cur.x-1][cur.y].cost = cur.cost + weig
                nodes[cur.x-1][cur.y].ind = nodes[cur.x-1][cur.y].cost + nodes[cur.x-1][cur.y].heuris
                appendnode(nodes[cur.x-1][cur.y])
            elif nodes[cur.x-1][cur.y].cost > cur.cost + weig:
                nodes[cur.x-1][cur.y].cost = cur.cost + weig
                nodes[cur.x-1][cur.y].parent = cur
                nodes[cur.x-1][cur.y].ind = nodes[cur.x-1][cur.y].cost + nodes[cur.x-1][cur.y].heuris
    if cur.x < rows-1:
        weig = max(mat[cur.x+1][cur.y], mat[cur.x][cur.y])
        if mat[cur.x+1][cur.y] > 0 and not (nodes[cur.x+1][cur.y] in closelist) :
            if not(nodes[cur.x+1][cur.y] in openlist):
                nodes[cur.x+1][cur.y].parent = cur
                nodes[cur.x+1][cur.y].cost = cur.cost + weig
                nodes[cur.x+1][cur.y].ind = nodes[cur.x+1][cur.y].cost + nodes[cur.x+1][cur.y].heuris
                appendnode(nodes[cur.x+1][cur.y])
            elif nodes[cur.x+1][cur.y].cost > cur.cost + weig:
                nodes[cur.x+1][cur.y].cost = cur.cost + weig
                nodes[cur.x+1][cur.y].parent = cur
                nodes[cur.x+1][cur.y].ind = nodes[cur.x+1][cur.y].cost + nodes[cur.x+1][cur.y].heuris
    if cur.y > 0:
        weig = max(mat[cur.x][cur.y-1], mat[cur.x][cur.y])
        if mat[cur.x][cur.y-1] > 0 and not (nodes[cur.x][cur.y-1] in closelist) :
            if not(nodes[cur.x][cur.y-1] in openlist):
                nodes[cur.x][cur.y-1].parent = cur
                nodes[cur.x][cur.y-1].cost = cur.cost + weig
                nodes[cur.x][cur.y-1].ind = nodes[cur.x][cur.y-1].cost + nodes[cur.x][cur.y-1].heuris
                appendnode(nodes[cur.x][cur.y-1])
            elif nodes[cur.x][cur.y-1].cost > cur.cost + weig:
                nodes[cur.x][cur.y-1].cost = cur.cost + weig
                nodes[cur.x][cur.y-1].parent = cur
                nodes[cur.x][cur.y-1].ind = nodes[cur.x][cur.y-1].cost + nodes[cur.x][cur.y-1].heuris
    if cur.y < cols-1:
        weig = max(mat[cur.x][cur.y+1], mat[cur.x][cur.y])
        if mat[cur.x][cur.y+1] > 0 and not (nodes[cur.x][cur.y+1] in closelist) :
            if not(nodes[cur.x][cur.y+1] in openlist):
                nodes[cur.x][cur.y+1].parent = cur
                nodes[cur.x][cur.y+1].cost = cur.cost + weig
                nodes[cur.x][cur.y+1].ind = nodes[cur.x][cur.y+1].cost + nodes[cur.x][cur.y+1].heuris
                appendnode(nodes[cur.x][cur.y+1])
            elif nodes[cur.x][cur.y+1].cost > cur.cost + weig:
                nodes[cur.x][cur.y+1].cost = cur.cost + weig
                nodes[cur.x][cur.y+1].parent = cur
                nodes[cur.x][cur.y+1].ind = nodes[cur.x][cur.y+1].cost + nodes[cur.x][cur.y+1].heuris
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
    while cur != nodes[startx][starty]:
        steps += 1
        stack.append((cur.x, cur.y))
        cur = cur.parent
    stack.append((cur.x, cur.y))
        
    print 'Broj koraka: ', steps
    #print 'Koraci: ', stack
    print 'Broj poteza: ', nodes[endx][endy].cost

    
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
