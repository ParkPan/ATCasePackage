import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_fod_report(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_fod_report.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "fod_report"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                fod_type = 'fod_type=' + "hls"  # or channel
                public_ip = 'public_ip=' + '192.168.0.110'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, fod_type, public_ip))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_fod_report.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_fod_report')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_fod_report')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_fod_report['inputtable'])
        print 'data clear done'