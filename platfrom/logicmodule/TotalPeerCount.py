import os

def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/PeerInfoRecordingDB.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    resultlist = {}
    for line in orglines:
        peerid, sdkversion, nat_type, pub_ip, pub_port, pri_ip, pri_port, macs, os_version, cpu, province, isp = line.split(',')
        resultlist[peerid[:8]] = resultlist.setdefault(peerid[:8], 0) + 1
    totalcount = 0
    for peerfix, count in resultlist.items():
        totalcount += count
        expectedfile.write('%s,%d\n' % (peerfix, count))
    expectedfile.write('%s,%d\n' % ('99999999', totalcount))
    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
