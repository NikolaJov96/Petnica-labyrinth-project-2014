import random
import sys
import time
from init import *

reinit()

sys.setrecursionlimit(20000)

def findbyxy(x, y):
    for i in range(0, len(queind)):
        if quex[i]==x and quey[i]==y:
            return i
    return -2

# put
print 'Optimalna putanja:'
starttime = time.time()
while len(queind) > 0:#def rec(curx, cury, ind):  # rekurzija za odredivanje puta
    curx = quex.pop(0)
    cury = quey.pop(0)
    ind = queind.pop(0)
    riched[curx][cury] = ind
    global co
    global arco
    #co += 1
    #if co % 1000 == 0:
    #    print co, arco
    if curx == endx and cury == endy:
        succ = True
        break
    if curx > 0:
        weig = max(mat[curx-1][cury], mat[curx][cury])
        if mat[curx-1][cury] > 0 and (riched[curx-1][cury] > ind + weig or riched[curx-1][cury] == -2):
            popind = findbyxy(curx-1, cury)
            if popind > -2:
                queind.pop(popind)
                quex.pop(popind)
                quey.pop(popind)
            if len(queind)>0:
                top = queind[len(queind)-1]
                while top > ind + weig and len(queind)>0:#-1+1
                    pqueind.append(queind.pop())
                    pquex.append(quex.pop())
                    pquey.append(quey.pop())
                    if len(queind)>0:
                        top = queind[len(queind)-1]
                    else:
                        break
                queind.append(ind + weig)#-1+1
                quex.append(curx-1)
                quey.append(cury)
                while len(pqueind)>0:
                    queind.append(pqueind.pop())
                    quex.append(pquex.pop())
                    quey.append(pquey.pop())
            else:
                queind.append(ind + weig)#-1+1
                quex.append(curx-1)
                quey.append(cury)
            #arco+=1
    if curx < rows-1:
        weig = max(mat[curx+1][cury], mat[curx][cury])
        if mat[curx+1][cury] > 0 and (riched[curx+1][cury] > ind + weig or riched[curx+1][cury] == -2):
            popind = findbyxy(curx+1, cury)
            if popind > -2:
                queind.pop(popind)
                quex.pop(popind)
                quey.pop(popind)
            if len(queind)>0:
                top = queind[len(queind)-1]
                while top > ind + weig and len(queind)>0:#-1+1
                    pqueind.append(queind.pop())
                    pquex.append(quex.pop())
                    pquey.append(quey.pop())
                    if len(queind)>0:
                        top = queind[len(queind)-1]
                    else:
                        break
                queind.append(ind +weig)#-1+1
                quex.append(curx+1)
                quey.append(cury)
                while len(pqueind)>0:
                    queind.append(pqueind.pop())
                    quex.append(pquex.pop())
                    quey.append(pquey.pop())
            else:
                queind.append(ind + weig)#-1+1
                quex.append(curx+1)
                quey.append(cury)
            #arco+=1
    if cury > 0:
        weig = max(mat[curx][cury-1], mat[curx][cury])
        if mat[curx][cury-1] > 0 and (riched[curx][cury-1] > ind + weig or riched[curx][cury-1] == -2):
            popind = findbyxy(curx, cury-1)
            if popind > -2:
                queind.pop(popind)
                quex.pop(popind)
                quey.pop(popind)
            if len(queind)>0:
                top = queind[len(queind)-1]
                while top > ind + weig and len(queind)>0:#-1+1
                    pqueind.append(queind.pop())
                    pquex.append(quex.pop())
                    pquey.append(quey.pop())
                    if len(queind)>0:
                        top = queind[len(queind)-1]
                    else:
                        break
                queind.append(ind + weig)#-1+1
                quex.append(curx)
                quey.append(cury-1)
                while len(pqueind)>0:
                    queind.append(pqueind.pop())
                    quex.append(pquex.pop())
                    quey.append(pquey.pop())
            else:
                queind.append(ind + weig)#-1+1
                quex.append(curx)
                quey.append(cury-1)
            #arco+=1
    if cury < cols-1:
        weig = max(mat[curx][cury+1], mat[curx][cury])
        if mat[curx][cury+1] > 0 and (riched[curx][cury+1] > ind + weig or riched[curx][cury+1] == -2):
            popind = findbyxy(curx, cury+1)
            if popind > -2:
                queind.pop(popind)
                quex.pop(popind)
                quey.pop(popind)
            if len(queind)>0:
                top = queind[len(queind)-1]
                while top > ind + weig and len(queind)>0:#-1+1
                    pqueind.append(queind.pop())
                    pquex.append(quex.pop())
                    pquey.append(quey.pop())
                    if len(queind)>0:
                        top = queind[len(queind)-1]
                    else:
                        break
                queind.append(ind + weig)#-1+1
                quex.append(curx)
                quey.append(cury+1)
                while len(pqueind)>0:
                    queind.append(pqueind.pop())
                    quex.append(pquex.pop())
                    quey.append(pquey.pop())
            else:
                queind.append(ind + weig)#-1+1
                quex.append(curx)
                quey.append(cury+1)

endtime = time.time()
            #arco+=1
                
    #print queind, curx, cury
    #if len(queind) == 0:
    #    return 0
    #arco-=1
    #return rec(quex.pop(0), quey.pop(0), queind.pop(0))

#succ = rec(quex.pop(), quey.pop(), queind.pop())
print 'Pretraga uspela: ', bool(succ)
print 'Trajanje: ', endtime-starttime
#for x in riched:
#   print x

stack = [(endx, endy)]
if succ:
    x = endx
    y = endy
    while (x != startx) or (y != starty):
        if x > 0:
            if riched[x-1][y] == riched[x][y]-max(mat[x][y], mat[x-1][y]):
                x -= 1
                stack.append((x, y))
                continue
        if x < rows-1:
            if riched[x+1][y] == riched[x][y]-max(mat[x][y], mat[x+1][y]):
                x += 1
                stack.append((x, y))
                continue
        if y > 0:
            if riched[x][y-1] == riched[x][y]-max(mat[x][y], mat[x][y-1]):
                y -= 1
                stack.append((x, y))
                continue
        if y < cols-1:
            if riched[x][y+1] == riched[x][y]-max(mat[x][y], mat[x][y+1]):
                y += 1
                stack.append((x, y))
                continue
    print 'Broj koraka: ', len(stack)-1
    #print 'Koraci: ', stack
    print 'Broj poteza: ', riched[endx][endy]


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

        
def retsucc():
    return succ
