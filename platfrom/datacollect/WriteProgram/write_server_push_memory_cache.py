import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_push_memory_cache(dataprovider.Dataprovider):

    def makedata(self):

        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_push_memory_cache.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "push_memory_cache"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                chunk_id = 'chunk_id=' + 'testchunkid1212'
                behavior = 'behavior=' + 'out'
                filedemanddata.write(data_format % (topic, timestamp, file_id, chunk_id, behavior))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_push_memory_cache.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_push_memory_cache')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_push_memory_cache')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_push_memory_cache['inputtable'])
        print 'data clear done'
