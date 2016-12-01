import sys
import os
import constvars
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

time_format = constvars.recorddate + '000001'
timestamp = long(get_timestamp_by_time(time_format)[:-3])

def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/LiveProgressCleaned.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    resultlist={}
    peeridlist=[]
    totallist={}
    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    for line in orglines:
        _,timesp,peerid,_,_,_,_,_= line.split(',')
        if peerid not in peeridlist:
            peeridlist.append(peerid)
            peerfix=peerid[:8]
            resultlist[peerfix]= resultlist.setdefault(peerfix,0)+1
            totallist['99999999']=totallist.setdefault('99999999',0)+1

    for prefix,count in resultlist.items():
        expectedfile.write(("%s,%d\n")%(prefix,count))
    expectedfile.write(("%s,%d\n")%('99999999',totallist['99999999']))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]




