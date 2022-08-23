import time
import init

init.reinit()
iters = init.iters
it = 1

fw = open('outdata.txt', 'w')
fw.write(str(iters)+'\n')
fw.close()

poctime = time.time()

while True:
    reseno = False

    print 'Iteracija:', it
    #print 'Matrica:'
    print 'Dimenzije:', init.rows, 'X', init.cols
    """for x in init.mat:
        for y in x:
            if y==0: print 'x',
            elif y==1: print '_',
            else: print 'O',
        print"""

    #write data file
    fw = open('outdata.txt', 'a')
    fw.write(str(init.rows)+'\n'+str(init.cols)+'\n')
    for x in init.mat:
        for y in x:
            if y==0: fw.write('x'),
            elif y==1: fw.write('_'),
            else: fw.write('O'),
        fw.write('\n')
    fw.close()
    

    """import optimalna_putanja
    reseno = optimalna_putanja.retsucc()
    for x in optimalna_putanja.riched:
        print x
    if reseno: optimalna_putanja.viz()"""

    """print
    import Astar
    if reseno: Astar.viz()
    tm = Astar.gettime()"""

    print
    import Astar_noclass
    Astar_noclass.calcAstar()
    reseno = Astar_noclass.retsucc()
    if reseno:
        #Astar_noclass.viz()
        Astar_noclass.vizdata()

    if reseno:
        
        print
        import potraga
        potraga.calcpotraga()
        #potraga.viz()
        potraga.vizdata()
        
        print
        import potraga_bezgledanja
        potraga_bezgledanja.calcpotraga_bezgledanja()
        
        print
        import glup_algoritam
        glup_algoritam.calcglup_algoritam()

    if iters == it: break
    init.reinit()
    it += 1
    
krtime = time.time()
print
print 'Kraj programa - ukupno vreme rada: ', krtime-poctime
print 'Racunanje statistike'
fw = open('outdata.txt', 'a')
fw.write(str(krtime-poctime))
fw.close()

import stats
stats.calcstats()

print 'Kraj'
