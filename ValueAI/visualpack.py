import matplotlib.pyplot as plt


def parsfile(name):
    f = open(name)
    data=[]
    i=0

    for line in f:
        data.append(float(line))
        #print(line)
        i+=1
        #print(i)
    return data

def initgraph():
    fig = plt.figure()

def histogram(data):
    #print(data)
    print(len(data))
    fig = plt.figure()
    x=[]
    for i in range(0,len(data)):
        x.append(i)
    plt.bar(x,data)


def plot(data):
    fig = plt.figure()
    plt.plot(data)

def show():
    plt.show()


