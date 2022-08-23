# -*- coding: utf-8 -*-
import random
from math import sqrt 

# inicializacija
rows = 50
cols = 50
shapemat = True

"""mat = [[1, 2, 1, 0, 2, 1, 1, 1, 0, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 2],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 2, 0, 1, 2, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 1, 2, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 2, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 2, 2, 1, 0, 2, 1, 0, 0, 1, 1, 1, 2, 0, 2, 2, 2, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 2, 0, 1, 1, 0, 0, 0, 1, 1, 2, 2, 1, 2, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 2, 0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1, 2],
    [1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 1, 0, 1, 1, 2, 0, 0, 1, 2, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2, 1, 0, 0, 0, 2, 1, 1],
    [1, 0, 2, 2, 0, 1, 1, 2, 0, 1, 0, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1, 1, 1, 0, 0, 1, 1, 2, 0, 0],
    [0, 1, 2, 2, 0, 1, 2, 1, 2, 2, 1, 0, 0, 2, 2, 0, 1, 1, 2, 1, 1, 0, 1, 0, 1, 0, 0, 0, 2, 0],
    [0, 1, 0, 1, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 2, 0],
    [1, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 0, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0],
    [0, 1, 0, 2, 1, 1, 2, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 2, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 1],
    [2, 2, 1, 0, 1, 0, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 2, 2, 0, 1],
    [1, 1, 1, 0, 0, 1, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 2, 2, 1, 2, 1, 0, 0, 0, 0, 2, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1, 1, 0, 1, 2, 2, 0, 1, 2],
    [0, 0, 0, 1, 0, 2, 2, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 2, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 2, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2],
    [1, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 2, 2, 0, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [2, 0, 1, 0, 1, 1, 0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 2, 0, 1, 1, 2, 0, 0],
    [2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 2, 0, 0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 0, 0, 0, 1, 1, 1, 1, 0],
    [2, 0, 1, 1, 2, 1, 0, 2, 2, 1, 0, 2, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [2, 1, 0, 1, 1, 0, 0, 2, 1, 2, 0, 1, 1, 1, 0, 1, 1, 2, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 2, 2, 2, 0, 0, 2, 1, 2, 1, 1, 0, 2, 1, 0, 2, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 2]]"""

if shapemat:
    mat = [[1 for i in range(cols)] for j in range(rows)]
    cels = rows*cols
    ucels=0
    while ucels/float(cels) < 0.4:
        #print ucels, cels
        shape = random.randint(0,3)
        weig = random.choice([0, 0, 2])
        if shape == 0: #kvadrat
            dx = random.randint(1, rows/8)
            dy = random.randint(1, cols/8)
            x = random.randint(0, rows-dx-1)
            y = random.randint(0, cols-dy-1)
            for i in range(x,x+dx+1):
                for j in range(y,y+dy+1):
                    if mat[i][j] == 0:
                        ucels += 1
                    mat[i][j] = weig
        elif shape == 1: #P(П)
            dx = random.randint(1, rows/14)
            dy = random.randint(1, cols/14)
            x = random.randint(0, rows-3*dx-1)
            y = random.randint(0, cols-3*dy-1)
            for i in range(x,x+dx):
                for j in range(y,y+dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            for i in range(x+2*dx,x+3*dx):
                for j in range(y+2*dy,y+3*dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            for i in range(x+2*dx,x+3*dx):
                for j in range(y,y+dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            for i in range(x,x+dx):
                for j in range(y+2*dy,y+3*dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            rndblock = [0, 1, 2, 3]
            rndblock.pop(random.randint(0,3))
            if 0 in rndblock:
                for i in range(x,x+dx):
                    for j in range(y+dy,y+2*dy):
                        if mat[i][j] == 1:
                            ucels += 1
                        mat[i][j] = weig
            if 1 in rndblock:
                for i in range(x+dx,x+2*dx):
                    for j in range(y,y+dy):
                        if mat[i][j] == 1:
                            ucels += 1
                        mat[i][j] = weig
            if 2 in rndblock:
                for i in range(x+dx,x+2*dx):
                    for j in range(y+2*dy,y+3*dy):
                        if mat[i][j] == 1:
                            ucels += 1
                        mat[i][j] = weig
            if 3 in rndblock:
                for i in range(x+2*dx,x+3*dx):
                    for j in range(y+dx,y+2*dy):
                        if mat[i][j] == 1:
                            ucels += 1
                        mat[i][j] = weig
        elif shape == 2: #krst
            dx = random.randint(1, rows/14)
            dy = random.randint(1, cols/14)
            x = random.randint(0, rows-3*dx-1)
            y = random.randint(0, cols-3*dy-1)
            for i in range(x+dx, x+2*dx):
                for j in range(y,y+3*dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            for i in range(x,x+dx):
                for j in range(y+dy,y+2*dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
            for i in range(x+2*dx,x+3*dx):
                for j in range(y+dy,y+2*dy):
                    if mat[i][j] == 1:
                        ucels += 1
                    mat[i][j] = weig
        elif shape == 3: #piramida
            rndblock = random.randint(0,3)
            if rndblock == 0:
                ln = min(random.randint(1, rows/9)*2 + 1, random.randint(1, cols/9)*2 + 1) #moze da izadje sa matrice
                x = random.randint(0, rows-(ln+1)/2-1)
                y = random.randint(0, cols-ln-1)
                i = 0
                for xi in range(x, x+(ln+1)/2):
                    for j in range (y+i, y+ln-i):
                        if mat[xi][j] == 1:
                            ucels += 1
                        mat[xi][j] = weig
                    i += 1
            if rndblock == 1:
                ln = min(random.randint(1, rows/9)*2 + 1, random.randint(1, cols/9)*2 + 1)
                x = random.randint(0, rows-(ln+1)/2-1)
                y = random.randint(0, cols-ln-1)
                i = 0
                for xi in range(x+(ln+1)/2, x, -1):
                    for j in range (y+i, y+ln-i):
                        if mat[xi][j] == 1:
                            ucels += 1
                        mat[xi][j] = weig
                    i += 1
            if rndblock == 2:
                ln = min(random.randint(1, rows/9)*2 + 1, random.randint(1, cols/9)*2 + 1)
                x = random.randint(0, cols-ln-1)
                y = random.randint(0, rows-(ln+1)/2-1)
                i = 0
                for xi in range(x, x+ln+1):
                    for j in range (y, y+i):
                        if mat[xi][j] == 1:
                            ucels += 1
                        mat[xi][j] = weig
                    if xi <= x+(ln/2): i += 1
                    else: i -= 1
            if rndblock == 3:
                ln = min(random.randint(1, rows/9)*2 + 1, random.randint(1, cols)*2 + 1)
                x = random.randint(0, cols-ln-1)
                y = random.randint(0, rows-(ln+1)/2-1)
                i = 0
                for xi in range(x, x+ln+1):
                    for j in range (y+(ln+1)/2-i, y+(ln+1)/2):
                        if mat[xi][j] == 1:
                            ucels += 1
                        mat[xi][j] = weig
                    if xi <= x+(ln/2): i += 1
                    else: i -= 1

else: mat = [[random.choice([0, 0, 1, 1, 1, 3]) for i in range(cols)] for j in range(rows)]
riched = [[-2 for i in range(cols)] for j in range(rows)]
startx = random.randint(0,rows-1)
starty = random.randint(0,cols-1)
endx = random.randint(0,rows-1)
endy = random.randint(0,cols-1)
while sqrt((endx-startx)**2 + (endy-starty)**2) < 21 or mat[startx][starty] == 0 or mat[endx][endy] == 0:
    startx = random.randint(0,rows-1)
    starty = random.randint(0,cols-1)
    endx = random.randint(0,rows-1)
    endy = random.randint(0,cols-1)
    #print 'aaaa'
print 'Pocetak:', startx, starty, 'Karj:', endx, endy
mat[startx][starty] = 1
mat[endx][endy] = 1
quex = []
quey = []
queind = []
pquex = []
pquey = []
pqueind = []
quex.append(startx)
quey.append(starty)
queind.append(0)
co=0
arco=0
succ = False

def reinit():
    global mat, riched, rows, cols, startx, starty, endx, endy, quex, quey
    global queind, pquex, pquey, pqueind
    riched = [[-2 for i in range(cols)] for j in range(rows)]
    quex = []
    quey = []
    mat[startx][starty] = 1
    mat[endx][endy] = 1
    queind = []
    pquex = []
    pquey = []
    pqueind = []
    quex.append(startx)
    quey.append(starty)
    queind.append(0)
    co=0
    arco=0
    succ = False

def newstmat(): mat = [[random.choice([0, 0, 1, 1, 1, 2]) for i in range(cols)] for j in range(rows)]
