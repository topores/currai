import revmethlib as rml
import numpy as np
import random
import parsing as prs
def initN1(O,H,L,C,i):
    N1=np.zeros((12))
    N1[0],N1[1],N1[2],N1[3],N1[4],N1[5],N1[6],N1[7],N1[8],N1[9], = getinput(O,H,L,C,i)
    N1[10] = N1[6] - N1[3]
    N1[11] = N1[9] - N1[6]
    #2**10=1024
    return N1
def getinput(O,H,L,C,i):
    o, h1, l1, c1, h2, l2, c2, h3, l3, c3 = prs.getparsdata(O,H,L,C,i)
    return o,h1,l1,c1,h2,l2,c2,h3,l3,c3

def initw1():
    w1 = np.zeros((4096,12))
    for i in range(0,4096):
        random.seed()
        s=genstring(i)
        for j in range(0,12):
            if (s[j]=='1'):
                w1[i,j]=0.6+random.random()*0.1
            else:
                w1[i, j] = -0.6 - random.random()*0.1
    return w1

def initw2():
    w2 = np.zeros((4096))
    for i in range(0,4096):
        random.seed()
        w2[i] = (random.random()-0.5)*2/10
    return w2

def genstring(i):
    s=bin(i)
    s=s[2:len(s)]
    l=12-len(s)
    for j in range(0,l):
        s='0'+s
    return s


def initN2(N1,w1):
    N2 = np.zeros((4096))
    for i in range(0,4096):
        for j in range(0,12):
            N2[i]+=w1[i,j]*N1[j]
        N2[i]=rml.sigmoid(N2[i])
    return N2

def result(N2,w2,k=1):
    res=0
    for i in range(0,4096):
        res+=w2[i]*N2[i]
    res*=k
    return rml.sigmoid(res)



