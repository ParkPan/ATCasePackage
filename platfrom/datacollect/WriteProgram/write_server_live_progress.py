import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_live_progress(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')
        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_live_progress.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "live_progress"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                public_ip = 'public_ip=' + '192.168.0.110'
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                chunk_id = 'chunk_id=' + "12345"
                filedemanddata.write(data_format % (topic, timestamp, peer_id, public_ip, file_id, chunk_id))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_live_progress.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_live_progress')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_progress')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_progress['inputtable'])
        print 'data clear done'