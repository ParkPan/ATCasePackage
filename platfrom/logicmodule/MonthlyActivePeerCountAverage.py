import sys
import os
import pipeofodps
import random

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeerActivity.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    tempfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek1.txt', 'w')
    for line in orglines:
        randomnum = random.randint(150, 300)
        tmpcount = line.split(',')[1]

        newline = line.replace(',%s' % tmpcount, ',%s' % str(int(tmpcount) * randomnum))
        tmpstr1 = newline.split(',')[1]
        newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s\n' % (tmpstr1, 'NULL'))

        tempfile1.write(newline1)
    tempfile1.close()

    tempfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek2.txt', 'w')
    for line in orglines:
        randomnum = random.randint(150, 300)
        tmpcount = line.split(',')[1]

        newline = line.replace(',%s' % tmpcount, ',%s' % str(int(tmpcount) * randomnum))
        tmpstr1 = newline.split(',')[1]
        newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s\n' % (tmpstr1, 'NULL'))

        tempfile2.write(newline1)
    tempfile2.close()

    pipeofodps.uploaddatatoodps(
        'output_daily_peer_activity',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyPeerActivityDBWeek1.txt'),
        3)

    pipeofodps.uploaddatatoodps(
        'output_daily_peer_activity',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyPeerActivityDBWeek2.txt'),
        7)

    resultfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek1.txt', 'r')
    orglines1 = resultfile1.readlines()
    resultfile1.close()

    resultfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek2.txt', 'r')
    orglines2 = resultfile2.readlines()
    resultfile2.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    sumcount = {}

    for line in orglines:
        prefix, actcount = line.split(',')
        actcount = actcount.replace('\n', '')
        if prefix not in sumcount:
            sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)

    for line in orglines1:
        prefix, actcount, _ = line.split(',')
        if prefix not in sumcount:
            sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)
        else:
            sumcount[prefix] = sumcount[prefix] + int(actcount)

    for line in orglines2:
        prefix, actcount, _ = line.split(',')
        if prefix not in sumcount:
            sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)
        else:
            sumcount[prefix] = sumcount[prefix] + int(actcount)

    for pre, count in sumcount.items():
        if (pre != '99999999'):
            expectedfile.write('%s,%d\n' % (pre, int(count/30)))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]







