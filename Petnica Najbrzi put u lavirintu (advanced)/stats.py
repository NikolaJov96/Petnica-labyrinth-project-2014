import init

def calcstats():
    AStlaps = []
    PRtlaps = []
    PBtlaps = []
    GLtlaps = []
    AStlapssr = 0
    PRtlapssr = 0
    PBtlapssr = 0
    GLtlapssr = 0

    ASsteps = []
    PRsteps = []
    PBsteps = []
    GLsteps = []
    ASstepssr = 0
    PRstepssr = 0
    PBstepssr = 0
    GLstepssr = 0

    PRminsteps = []
    PBminsteps = []
    GLminsteps = []
    PRminstepssr = 0
    PBminstepssr = 0
    GLminstepssr = 0

    AScosts = []
    PRcosts = []
    PBcosts = []
    GLcosts = []
    AScostssr = 0
    PRcostssr = 0
    PBcostssr = 0
    GLcostssr = 0

    dims = []
    mats = []
    resAS = []
    resPR = []

    fr = open('outdata.txt', 'r')
    iters = int(fr.readline())

    iterind = 0
    for i in range(0,iters): # citanje fjla
        rows = int(fr.readline())
        cols = int(fr.readline())
        mats.append([[-1 for i in range(cols)] for j in range(rows)])
        for j in range(0,rows):
            line = fr.readline()
            mats[iterind][j] = line[:]
        line = fr.readline()
        succ = True if line[0] == 'T' else False
        if succ:
            dims.append((rows, cols))
            # A*
            AStlaps.append(float(fr.readline()))
            AStlapssr += AStlaps[iterind]
            ASsteps.append(float(fr.readline()))
            ASstepssr += ASsteps[iterind]
            AScosts.append(float(fr.readline()))
            AScostssr += AScosts[iterind]
            resAS.append([[-1 for i in range(cols)] for j in range(rows)])
            for j in range(0,rows):
                line = fr.readline()
                resAS[iterind][j] = line[:]
            # potraga
            PRtlaps.append(float(fr.readline()))
            PRtlapssr += PRtlaps[iterind]
            PRsteps.append(float(fr.readline()))
            PRstepssr += PRsteps[iterind]
            PRminsteps.append(float(fr.readline()))
            PRminstepssr += PRminsteps[iterind]
            PRcosts.append(float(fr.readline()))
            PRcostssr += PRcosts[iterind]
            resPR.append([[-1 for i in range(cols)] for j in range(rows)])
            for j in range(0,rows):
                line = fr.readline()
                resPR[iterind][j] = line[:]
            # potraga_bezgledanja
            PBtlaps.append(float(fr.readline()))
            PBtlapssr += PBtlaps[iterind]
            PBsteps.append(float(fr.readline()))
            PBstepssr += PBsteps[iterind]
            PBminsteps.append(float(fr.readline()))
            PBminstepssr += PBminsteps[iterind]
            PBcosts.append(float(fr.readline()))
            PBcostssr += PBcosts[iterind]
            # glup_algoritam
            GLtlaps.append(float(fr.readline()))
            GLtlapssr += GLtlaps[iterind]
            GLsteps.append(float(fr.readline()))
            GLstepssr += GLsteps[iterind]
            GLminsteps.append(float(fr.readline()))
            GLminstepssr += GLminsteps[iterind]
            GLcosts.append(float(fr.readline()))
            GLcostssr += GLcosts[iterind]
            
            iterind += 1
        else: mats.pop()
    fr.close()

    AStlapssr /= iterind
    PRtlapssr /= iterind
    PBtlapssr /= iterind
    GLtlapssr /= iterind
    
    ASstepssr /= iterind
    PRstepssr /= iterind
    PBstepssr /= iterind
    GLstepssr /= iterind
    
    AScostssr /= iterind
    PRcostssr /= iterind
    PBcostssr /= iterind
    GLcostssr /= iterind
    
    fw = open('oputstats.txt', 'a')
    # dimenzije i vidokrug
    fw.write(str(dims[0][0])+' '+str(dims[0][1])+' '+str(init.seerange)+' ')
    # tlaps
    fw.write(str(AStlapssr)+' '+str(PRtlapssr)+' '+str(PBtlapssr)+' '+str(GLtlapssr)+' ')
    # steps
    fw.write(str(ASstepssr)+' '+str(PRstepssr)+' '+str(PBstepssr)+' '+str(GLstepssr)+' ')
    # costs
    fw.write(str(AScostssr)+' '+str(PRcostssr)+' '+str(PBcostssr)+' '+str(GLcostssr)+'\n')
    fw.close()

    specco = 0
    fw = open('speccasses.txt', 'a')
    for i in range(0, iterind):
        if AScosts[i] < 0.8*PRcosts[i] or PRcosts[i] < AScosts[i]:
            specco += 1
            # dimenzije i vidokrug
            fw.write('Dimenzije: '+str(dims[i][0])+'x'+str(dims[i][1])+' Vidokrug: '+str(init.seerange)+'\n')
            # tlaps
            fw.write('Vreme izvesavanja za:\n')
            fw.write('- A*: '+str(AStlaps[i])+'\n')
            fw.write('- Potraga: '+str(PRtlaps[i])+'\n')
            fw.write('- Potraga bez gledanja: '+str(PBtlaps[i])+'\n')
            fw.write('- Glup algoritam: '+str(GLtlaps[i])+'\n\n')
            # costs
            fw.write('Potezi za:\n')
            fw.write('- A*: '+str(AScosts[i])+'\n')
            fw.write('- Potraga: '+str(PRcosts[i])+'\n')
            fw.write('- Potraga bez gledanja: '+str(PBcosts[i])+'\n')
            fw.write('- Glup algoritam: '+str(GLcosts[i])+'\n\n')
            # matrica
            for x in mats[i]:
                for y in x:
                    fw.write(y+' ')
            fw.write('\n')
            for x in resAS[i]:
                for y in x:
                    fw.write(y+' ')
            fw.write('\n')
            for x in resPR[i]:
                for y in x:
                    fw.write(y+' ')
            fw.write('\n')
    fw.write('\n'+str(specco)+'\n\n')
    fw.close()
