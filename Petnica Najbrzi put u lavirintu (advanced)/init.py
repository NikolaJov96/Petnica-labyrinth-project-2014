# -*- coding: utf-8 -*-
import random
from math import sqrt
def reinit():
    global rows, cols, mat, startx, starty, endx, endy, seerange, iters, timewait, rnditers
    rows = 20
    cols = 20
    iters = 60
    timewait = 30
    rnditers = 100
    startx = random.randint(0,rows-1)
    starty = random.randint(0,cols-1)
    endx = random.randint(0,rows-1)
    endy = random.randint(0,cols-1)
    seerange = (rows+cols)/2/7 #random.randint(min(rows/6, cols/6), min(rows/2, cols/2))
    shapemat = 2
    if shapemat==0:
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
                        for j in range(y+dy,y+2*dy):
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
                    x = random.randint(0, rows-ln-1)
                    y = random.randint(0, cols-(ln+1)/2-1)
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
                    x = random.randint(0, rows-ln-1)
                    y = random.randint(0, cols-(ln+1)/2-1)
                    i = 0
                    for xi in range(x, x+ln+1):
                        for j in range (y+(ln+1)/2-i, y+(ln+1)/2):
                            if mat[xi][j] == 1:
                                ucels += 1
                            mat[xi][j] = weig
                        if xi <= x+(ln/2): i += 1
                        else: i -= 1
    elif shapemat==1: mat = [[random.choice([0, 0, 1, 1, 1, 3]) for i in range(cols)] for j in range(rows)]
    else:
        mat = [[0 for i in range(cols)] for j in range(rows)]
        edgedots=[(random.randint(1, rows-1), random.randint(1, cols-1))]
        mat[edgedots[0][0]][edgedots[0][1]] = 1
        while edgedots:
            ln = len(edgedots)
            ind = random.randint(0, ln-1)
            x = 0
            y = 0
            dx = edgedots[ind][0]
            dy = edgedots[ind][1]
            direct = random.randint(1, 4)
            
            succ = False
            i = 1
            while succ==False and i <= 4:
                i = i + 1
                direct = (direct - 1) if (direct>1) else 4
                zsum = 0
                if direct == 1:
                    if dx == 0: continue
                    x = dx - 1
                    y = dy
                    zsum += mat[x-1][y-1] if (x>0 and y>0) else 0
                    zsum += mat[x-1][y] if (x>0) else 0
                    zsum += mat[x-1][y+1] if (x>0 and y<cols-1) else 0
                    zsum += mat[x][y-1] if (y>0) else 0
                    zsum += mat[x][y+1] if (y<cols-1) else 0
                if direct == 2:
                    if dy == cols-1: continue
                    x = dx
                    y = dy + 1
                    zsum += mat[x-1][y] if (x>0) else 0
                    zsum += mat[x-1][y+1] if (x>0 and y<cols-1) else 0
                    zsum += mat[x+1][y] if (x<rows-1) else 0
                    zsum += mat[x+1][y+1] if (x<rows-1 and y<cols-1) else 0
                    zsum += mat[x][y+1] if (y<cols-1) else 0
                if direct == 3:
                    if dx == rows-1: continue
                    x = dx + 1
                    y = dy
                    zsum += mat[x+1][y-1] if (x<rows-1 and y>0) else 0
                    zsum += mat[x+1][y] if (x<rows-1) else 0
                    zsum += mat[x+1][y+1] if (x<rows-1 and y<cols-1) else 0
                    zsum += mat[x][y-1] if (y>0) else 0
                    zsum += mat[x][y+1] if (y<cols-1) else 0
                if direct == 4:
                    if dy == 0: continue
                    x = dx
                    y = dy - 1
                    zsum += mat[x-1][y-1] if (x>0 and y>0) else 0
                    zsum += mat[x-1][y] if (x>0) else 0
                    zsum += mat[x+1][y-1] if (x<rows-1 and y>0) else 0
                    zsum += mat[x+1][y] if (x<rows-1) else 0
                    zsum += mat[x][y-1] if (y>0) else 0
                if mat[x][y] == 1: continue
                if zsum == 0:
                    mat[x][y] = 1
                    edgedots.append((x,y))
                    succ = True
            if succ == False:
                edgedots.pop(ind)
        for i in range(0,rows*cols/5): mat[random.randint(0, rows-1)][random.randint(0, cols-1)] = 2
        #print mat

    while sqrt((endx-startx)**2 + (endy-starty)**2) < seerange or sqrt((endx-startx)**2 + (endy-starty)**2) < (rows+cols)/3 or mat[startx][starty] == 0 or mat[endx][endy] == 0: 
        startx = random.randint(0,rows-1)
        starty = random.randint(0,cols-1)
        endx = random.randint(0,rows-1)
        endy = random.randint(0,cols-1)

#reinit()
