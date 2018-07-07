
def initlogs():
    errorlog= open('errorlog.txt', 'w')
    trueerrorlog = open('trueerrorlog.txt', 'w')
    rgratelog= open('rgratelog.txt', 'w')
    return errorlog,trueerrorlog,rgratelog
def updatelogs(errorlog,trueerrorlog,rgratelog,error,trueerror,rgrate):
    errorlog.write(str(error)+'\n')
    trueerrorlog.write(str(trueerror)+'\n')
    rgratelog.write(str(rgrate)+'\n')

def initwightlog(w2):
    w2logstart= open('w2logstart.txt', 'w')
    for i in range(0,len(w2)):
        w2logstart.write(str(w2[i])+'\n')
    w2logstart.close()
def checkwightlog(w2):
    w2loglast = open('w2loglast.txt', 'w')
    for i in range(0, len(w2)):
        w2loglast.write(str(w2[i]) + '\n')
    w2loglast.close()
def closelog(f):
    f.close()
