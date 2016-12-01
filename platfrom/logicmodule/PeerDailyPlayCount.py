import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/PeerHourPlayCountDB.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    resultlist = {}
    for line in orglines:
        peerid,_,count,_ = line.split(',')
        resultlist[peerid]=resultlist.setdefault(peerid,0)+int(count)

    for peerid, count in resultlist.items():
        expectedfile.write('%s,%d\n' % (peerid,count))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]



