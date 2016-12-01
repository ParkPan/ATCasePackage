import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_rsm_change(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')
        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_rsm_change.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "rsm_change"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                operation = 'operation=' + 'create'  # create, delete, update
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                start_chunk_id = 'start_chunk_id=' + "12345"
                chunk_number = 'chunk_number=' + "1024"
                filedemanddata.write(data_format % (topic, timestamp, peer_id, file_id,
                                                    operation, start_chunk_id, chunk_number))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_rsm_change.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_rsm_change')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_rsm_change')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_rsm_change['inputtable'])
        print 'data clear done'
