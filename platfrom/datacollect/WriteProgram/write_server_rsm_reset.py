import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER

class server_rsm_reset(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_rsm_reset.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "rsm_reset"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                filedemanddata.write(data_format % (topic, timestamp, peer_id))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_rsm_reset.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_rsm_reset')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_rsm_reset')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_rsm_reset['inputtable'])
        print 'data clear done'
