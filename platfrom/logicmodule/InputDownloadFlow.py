import os
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/RawDownloadFlow.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()
    expectedformat = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    filterlist = []
    for line in orglines:
        id, timesp, peerid, url, useragent, playtype, p2pdown, cdndown, duration, intime, outtime = line.split(',')
        if (id, peerid) not in filterlist:
            filterlist.append((id, peerid))
            expectedfile.write(expectedformat % (
                peerid, timesp, url, useragent, playtype, p2pdown, cdndown, duration, id, intime))
        else:
            continue

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]