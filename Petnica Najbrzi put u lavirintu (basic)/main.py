import cProfile
import time
from init import *

poctime = time.time()
reseno = False

print 'Matrica:'
for x in mat:
    for y in x:
        if y==0: print 'x',
        elif y==1: print '_',
        else: print 'O',
    print

#import optimalna_putanja
#reseno = optimalna_putanja.retsucc()
#for x in optimalna_putanja.riched:
#    print x

#if reseno: optimalna_putanja.viz()

"""print
import Astar
if reseno: Astar.viz()
tm = Astar.gettime()"""

print
import Astar_noclass

reseno = Astar_noclass.retsucc()
if reseno: Astar_noclass.viz()
#tm = Astar.gettime()

if reseno:
    
    print
    import potraga
    potraga.viz()
    
    print
    import potraga_bezgledanja
    
    print
    import glup_algoritam
    #for x in glup_algoritam.riched:
    #    print x

krtime = time.time()
print
print
print 'Ukupno vreme rada programa: ', krtime-poctime
