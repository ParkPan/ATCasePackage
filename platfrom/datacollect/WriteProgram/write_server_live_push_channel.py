import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_live_push_channel(dataprovider.Dataprovider):

    def makedata(self):

        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_live_push_channel.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "live_push_channel"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                connections = 'connections=' + "1000"
                latest_offset = 'latest_offset=' + '5000'
                latest_chunk_id = 'latest_chunk_id=' + 'idtest10001'
                push_chunk_id = 'push_chunk_id=' + 'idtest9999'
                start_push_time = 'start_push_time=' + '1464191001'
                push_duration = 'push_duration=' + '10'
                filedemanddata.write(data_format % (topic, timestamp, file_id, connections, latest_offset, latest_chunk_id,
                                                    push_chunk_id, start_push_time, push_duration))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_live_push_channel.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_live_push_channel')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_push_channel')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_push_channel['inputtable'])
        print 'data clear done'