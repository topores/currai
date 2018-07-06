import csv
import revmethlib as rml
import numpy as np
l=0

def initpars():
    f=open("EURUSD.csv")
    i=0
    O = np.zeros((11700))
    H = np.zeros((11700))
    L = np.zeros((11700))
    C = np.zeros((11700))
    T =[' ']*11700
    for line in f:
        #print(line)
        T[i]=line[0:15]
        line=line[16:len(line)]
        O[i]=line[0:9]
        line = line[10:len(line)]
        H[i] = line[0:9]
        line = line[10:len(line)]
        L[i] = line[0:9]
        line = line[10:len(line)]
        C[i] = line[0:9]
        #print(line)
        i+=1

    return O, H, L, C, T
def getparsdata(O, H, L, C,i):
    o = O[i - 2]


    h3=H[i] - o
    l3=L[i] - o
    c3=C[i] - o

    h2 = H[i-1] - o
    l2 = L[i-1] - o
    c2 = C[i-1] - o

    h1 = H[i - 2] - o
    l1 = L[i - 2] - o
    c1 = C[i - 2] - o

    return o, h1, l1, c1, h2, l2, c2, h3, l3, c3

def getexpected(O, H, L, C,i,k=4096):
    return rml.sigmoid((C[i+1]-O[i+1])*k)


