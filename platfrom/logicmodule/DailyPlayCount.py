import os


def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/HourPlayCountDB.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    resultlist = {}
    for line in orglines:
        peerfix,_,count,_= line.split(',')
        resultlist[peerfix]=resultlist.setdefault(peerfix,0)+int(count)

    for peerfix, count in resultlist.items():
        expectedfile.write('%s,%d\n' % (peerfix, count))
    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
