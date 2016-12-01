import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_sdk_lsm(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_sdk_lsm.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "sdk_lsm"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                public_ip = 'public_ip=' + '192.168.0.110'
                lsm_used = 'lsm_used=' + '888815648'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, public_ip, lsm_used))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_sdk_lsm.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_sdk_lsm')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_sdk_lsm')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_sdk_lsm['inputtable'])
        print 'data clear done'
