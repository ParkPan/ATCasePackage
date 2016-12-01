import sys
import os
import random
import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyStartTimeCountDB.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    tempfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyStartTimeCountDBWeek1.txt', 'w')
    for line in orglines:
        tmpstr = line.split(',')[1]
        tmpcount = line.split(',')[2]
        if int(tmpstr) > 3000:
            newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) + random.randint(0, 10)))
        else:
            newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) - random.randint(0, 6)))
        tempfile1.write(newline)
    tempfile1.close()

    tempfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyStartTimeCountDBWeek2.txt', 'w')
    for line in orglines:
        tmpstr = line.split(',')[1]
        tmpcount = line.split(',')[2]
        if int(tmpstr) < 3000:
            newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) + random.randint(0, 10)))
        else:
            newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) - random.randint(0, 6)))
        tempfile2.write(newline)
    tempfile2.close()

    pipeofodps.uploaddatatoodps(
        'output_daily_start_time_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyStartTimeCountDBWeek1.txt'),
        -7)

    pipeofodps.uploaddatatoodps(
        'output_daily_start_time_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyStartTimeCountDBWeek2.txt'),
        -13)

    resultfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyStartTimeCountDBWeek1.txt', 'r')
    orglines1 = resultfile1.readlines()
    resultfile1.close()

    resultfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyStartTimeCountDBWeek2.txt', 'r')
    orglines2 = resultfile2.readlines()
    resultfile2.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    resultlist={}

    for line in orglines:
        username,period,count,_ = line.split(',')
        if username not in resultlist:
            resultlist[username]={}
        if period not in resultlist[username]:
            resultlist[username][period]=int(count)
        else:
            resultlist[username][period]=resultlist[username][period]+int(count)

    for line in orglines1:
        username,period,count,_ = line.split(',')
        if username not in resultlist:
            resultlist[username]={}
        if period not in resultlist[username]:
            resultlist[username][period]=int(count)
        else:
            resultlist[username][period]=resultlist[username][period]+int(count)

    for line in orglines2:
        username,period,count,_ = line.split(',')
        if username not in resultlist:
            resultlist[username]={}
        if period not in resultlist[username]:
            resultlist[username][period]=int(count)
        else:
            resultlist[username][period]=resultlist[username][period]+int(count)

    for username, value in resultlist.items():
        for period, count in value.items():
            expectedfile.write('%s,%s,%d,%s\n' % (username,period,count,''))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]







