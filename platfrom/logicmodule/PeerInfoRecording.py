import os
import pipeofodps


def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseODPS.txt', 'r')
    orglines = resultfile.readlines()
    resultfile.close()

    pipeofodps.downloaddatafromodps(
        'output_peer_info', os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt', -1)
    oldpeeridlist = []
    if os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt'):
        tempfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt', 'r')
        oldorglines = tempfile.readlines()
        tempfile.close()
        for oldline in oldorglines:
            oldpeeridlist.append(oldline.split(',')[0])
    else:
        oldorglines = []

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    for line in orglines:
        peerid,sdkversion,nat_type,pub_ip,pub_port,pri_ip,pri_port,macs,os_version,cpu,province,isp,_,_= line.split(',')
        if peerid not in oldpeeridlist:
            oldorglines.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                peerid, sdkversion, nat_type, pub_ip, pub_port, pri_ip, pri_port, macs, os_version, cpu, province, isp))

    expectedfile.writelines(oldorglines)
    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
