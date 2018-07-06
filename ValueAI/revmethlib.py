import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def antisigmoid(x):
    if x==1:
        x=0.990
    y=-(x/(x-1))
    return math.log(y,math.e)

def wdelta(actual,expected):
    error=actual-expected
    wd=error*(actual*(1-actual))
    return wd
'''def Ndelta(actual,expected, prevoutput, weight):
    wd = wdelta(actual,expected, prevoutput)
    return wd*weight

'''

