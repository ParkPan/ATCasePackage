import sys
import os
import random
import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeerOnlineTime.txt', 'r')
    orglines1 = resultfile1.readlines()
    resultfile1.close()

    tempfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerOnlineTimeDBWeek1.txt', 'w')
    for line in orglines1:
        tmpstr = line.split(',')[1]
        if float(tmpstr) > 64000:
            newline = line.replace(',%s' % tmpstr, ',%s' % (float(tmpstr) + float(random.randint(0, 120))))
            tmpstr1 = newline.split(',')[2]
            newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s' % ('NULL', tmpstr1))
        else:
            newline = line.replace(',%s' % tmpstr, ',%s' % (float(tmpstr) - float(random.randint(0, 180))))
            tmpstr1 = newline.split(',')[2]
            newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s' % ('NULL', tmpstr1))
        tempfile.write(newline1)
    tempfile.close()

    pipeofodps.uploaddatatoodps(
        'output_daily_peer_online_time',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyPeerOnlineTimeDBWeek1.txt'),
        3)

    resultfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerOnlineTimeDBWeek1.txt', 'r')
    orglines2 = resultfile2.readlines()
    resultfile2.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    countlist={}
    sumcount={}

    for line in orglines1:
        prefix,avatime,actcount = line.split(',')
        actcount = actcount.replace('\n', '')
        if prefix not in countlist:
            countlist[prefix] = countlist.setdefault(prefix,0) + float(avatime) * int(actcount)
        if prefix not in sumcount:
            sumcount[prefix] = sumcount.setdefault(prefix,0) + int(actcount)

    for line in orglines2:
        prefix,avatime,_,actcount = line.split(',')
        actcount = actcount.replace('\n', '')
        if prefix not in countlist:
            countlist[prefix] = countlist.setdefault(prefix,0) + float(avatime) * int(actcount)
        if prefix not in sumcount:
            sumcount[prefix] = sumcount.setdefault(prefix,0) + int(actcount)
        else:
            countlist[prefix] = countlist[prefix] + float(avatime) * int(actcount)
            sumcount[prefix] = sumcount[prefix] + int(actcount)

    for pre, avetime in countlist.items():
        expectedfile.write('%s,%f,%s\n' % (pre,float(avetime/sumcount[pre]),' '))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]






