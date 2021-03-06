import os

def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/VodPerCleaned.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1],"w")
    resultlist = {}
    for line in orglines:
        _,_,_,peerid,_,_,_,_,_,_,type,startdelay,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_ = line.split(',')
        username=peerid[:8]
        if username not in resultlist:
            resultlist[username]={}
        if 1000 > int(startdelay) >= 0:
            resultlist[username][1000]=resultlist[username].setdefault(1000, 0) + 1
        elif 2000 > int(startdelay) >= 1000:
            resultlist[username][2000]=resultlist[username].setdefault(2000, 0) + 1
        elif 3000 > int(startdelay) >= 2000:
            resultlist[username][3000]=resultlist[username].setdefault(3000, 0) + 1
        elif 4000 > int(startdelay) >= 3000:
            resultlist[username][4000]=resultlist[username].setdefault(4000, 0) + 1
        elif 5000> int(startdelay)>= 4000:
            resultlist[username][5000]=resultlist[username].setdefault(5000, 0) + 1
        else:
            resultlist[username][0]=resultlist[username].setdefault(0, 0) + 1

    for user ,value in resultlist.items():
        for per ,count in value.items():
            expectedfile.write('%s,%d,%d,%s\n' % (user, per, count,''))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

