import os
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/RawClientException.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()
    expectedformat = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    filterlist = []
    for line in orglines:
        id, timesp, peerid, ostype, osver, cpu, corever, nattype, publicip, pubport, priip, priport, macs1, macs2, op, errcode, errmsg, intime, outtime, type  = line.split(',')
        type = type.replace('\n','')
        if (id, peerid) not in filterlist:
            filterlist.append((id, peerid))
            expectedfile.write(expectedformat % (
                id, timesp, peerid, ostype, osver, cpu, corever, nattype, publicip, pubport, priip, priport, macs1, macs2, op, errcode, errmsg, intime, outtime, type))
        else:
            continue

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
