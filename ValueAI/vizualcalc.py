import visualpack as vpk

errorl=vpk.parsfile("errorlog.txt")
vpk.histogram(errorl)
#print(errorl)

rg=vpk.parsfile("trueerrorlog.txt")
vpk.histogram(rg)
#print(errorl)


dataw1=vpk.parsfile("w2logstart.txt")
dataw2=vpk.parsfile("w2loglast.txt")
data=[]
for i in range(0,len(dataw2)):
    data.append(dataw2[i]-dataw1[i])
vpk.histogram(data)
vpk.show()


