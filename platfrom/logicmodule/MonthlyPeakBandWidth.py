import sys
import os
import lib.platfrom.pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidth.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    tempfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek1.txt', 'w')
    for line in orglines:
        temp = line.split(',')
        temp[1] = float(temp[1]) + 0.04
        temp[2] = float(temp[2]) + 0.02
        temp[3] = float(temp[3]) + 0.02
        line = ','.join(str(x) for x in temp)
        tempfile1.write(line)
    tempfile1.close()

    tempfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek2.txt', 'w')
    for line in orglines:
        temp = line.split(',')
        temp[1] = float(temp[1]) - 0.04
        temp[2] = float(temp[2]) - 0.02
        temp[3] = float(temp[3]) - 0.02
        line = ','.join(str(x) for x in temp)
        tempfile2.write(line)
    tempfile2.close()

    lib.platfrom.pipeofodps.uploaddatatoodps(
        'output_daily_peak_bandwidth',
        os.path.abspath(os.path.dirname(__file__) + '/../inputdata/DailyPeakBandWidthWeek1.txt'),
        -7)

    lib.platfrom.pipeofodps.uploaddatatoodps(
        'output_daily_peak_bandwidth',
        os.path.abspath(os.path.dirname(__file__) + '/../inputdata/DailyPeakBandWidthWeek2.txt'),
        7)

    resultfile1 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek1.txt', 'r')
    orglines1 = resultfile1.readlines()
    resultfile1.close()

    resultfile2 = open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek2.txt', 'r')
    orglines2 = resultfile2.readlines()
    resultfile2.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    resultlist={}

    for line in orglines:
        username, totalpeakwidth, cdnpeakwidth, p2ppeakwidth, typ= line.split(',')
        typ=typ.replace('\n','')
        if username not in resultlist:
            resultlist[username] = {}
        if typ not in resultlist[username]:
            resultlist[username][typ] = {}
            resultlist[username][typ]['peak'] = {}
            resultlist[username][typ]['cdnpeak'] = {}
            resultlist[username][typ]['p2ppeak'] = {}
            resultlist[username][typ]['peak'] = float(totalpeakwidth)
            resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
            resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)

    for line in orglines1:
        username, totalpeakwidth, cdnpeakwidth, p2ppeakwidth, typ= line.split(',')
        typ=typ.replace('\n','')
        if username not in resultlist:
            resultlist[username] = {}
        if typ not in resultlist[username]:
            resultlist[username][typ] = {}
            resultlist[username][typ]['peak'] = {}
            resultlist[username][typ]['cdnpeak'] = {}
            resultlist[username][typ]['p2ppeak'] = {}
            resultlist[username][typ]['peak'] = float(totalpeakwidth)
            resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
            resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['peak']:
            resultlist[username][typ]['peak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['cdnpeak']:
            resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['p2ppeak']:
            resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)

    for line in orglines2:
        username, totalpeakwidth, cdnpeakwidth, p2ppeakwidth, typ= line.split(',')
        typ=typ.replace('\n','')
        if username not in resultlist:
            resultlist[username] = {}
        if typ not in resultlist[username]:
            resultlist[username][typ] = {}
            resultlist[username][typ]['peak'] = {}
            resultlist[username][typ]['cdnpeak'] = {}
            resultlist[username][typ]['p2ppeak'] = {}
            resultlist[username][typ]['peak'] = float(totalpeakwidth)
            resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
            resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['peak']:
            resultlist[username][typ]['peak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['cdnpeak']:
            resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
        if float(totalpeakwidth) > resultlist[username][typ]['p2ppeak']:
            resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)

    for user, value1 in resultlist.items():
        for typeloc,peaks in value1.items():
            expectedfile.write('%s,%f,%f,%f,%s\n' % (user, peaks['peak'], peaks['cdnpeak'], peaks['p2ppeak'], typeloc))
    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]

if __name__ == '__main__':
    makeexpecteddata()