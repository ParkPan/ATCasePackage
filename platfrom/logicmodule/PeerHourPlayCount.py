import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars

def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/FileOnDemandCleaned.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()


    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    resultlist = {}
    for line in orglines:
        _,peerid,timesp,_,_,_,_,_,type = line.split(',')
        type=type.replace('\n','')
        for i in range(24):
            if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                if i not in resultlist:
                    resultlist[i]={}
                if peerid not in resultlist[i]:
                    resultlist[i][peerid] = 1
                else:
                    resultlist[i][peerid] = resultlist[i][peerid] + 1
                break

    for hour, values in resultlist.items():
        for peeid, count in values.items():
            expectedfile.write('%s,%s,%d\n' % (peeid,hour,count))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]


