import revmethlib as rml
import methods1 as mtd
import parsing as prs
import numpy as np
import visualpack as vpk
import logs
import math
import matplotlib.pyplot as plt

import time
#!!!!
learnrate=0.005
#!!!!
errorlog,trueerrorlog,rgratelog=logs.initlogs()

win=1
lose=1

N2hold=np.zeros((4096))
O, H, L, C, T = prs.initpars()

w1=mtd.initw1()
w2=mtd.initw2()
logs.initwightlog(w2)

errorav=0.3
for i in range(3,72380,1):
    #calculation
    N1=mtd.initN1(O,H,L,C,i)
    N2=mtd.initN2(N1,w1)
    actual=mtd.result(N2,w2)
    #loging

    #equaliation
    expected=prs.getexpected(O, H, L, C,i)
    error=actual-expected
    # loging
    if (actual>0.6):
        if (expected>0.5):
            win+=1
        else:
            lose+=1
    elif (actual<0.40):
        if (expected<0.5):
            win+=1
        else:
            lose+=1

    rgrate=win/(win+lose)
    trueerror = rml.antisigmoid(actual) - rml.antisigmoid(expected)
    #printing
    '''
    print('Res')
    print(actual,expected)
    print(error)
    print(rgrate)
    print(' ')
    print(rml.antisigmoid(actual),rml.antisigmoid(expected))
    print(trueerror)
    print(' ')
    '''
    print(i,error,trueerror,rgrate)
    error=((error)**2)
    errorav=(errorav*i+error)/(i+1)
    logs.updatelogs(errorlog, trueerrorlog, rgratelog, errorav, math.fabs(trueerror), rgrate)
    #correction

    #w2 corr
    for j in range(0,4096):
        wd=rml.wdelta(actual,expected)
        w2[j]+=-N2[j]*wd*learnrate
        N2hold[j]=N2[j]
        N2[j]+=-wd*N2[j]
    #w1 corr
    for j in range(0,4096):
        for l in range(0,12):
            wd = rml.wdelta(N2hold[j], N2[j])
            w1[j,l]+=-N1[l]*wd*learnrate

    if (i%10==0):
        logs.checkwightlog(w2)


logs.checkwightlog(w2)
#graphics

logs.closelog(errorlog)
logs.closelog(trueerrorlog)
logs.closelog(rgratelog)




