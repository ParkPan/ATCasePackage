import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    peeridlist = []
    if os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/MonthlyDistinctPeerID.txt'):
        resultfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/MonthlyDistinctPeerID.txt', 'r')
        orglines1 = resultfile1.readlines()
        resultfile1.close()
    else:
        orglines1 = []

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")

    for line in orglines1:
        peerid,_ = line.split(',')
        if peerid not in peeridlist:
            peeridlist.append(peerid)
            expectedfile.write('%s,%s\n' % (peerid,''))
        else:
            continue

    for line in orglines:
        _,_,peerid,_,_,_,_ = line.split(',')
        if peerid not in peeridlist:
            peeridlist.append(peerid)
            expectedfile.write('%s,%s\n' % (peerid,''))
        else:
            continue

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]








