import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_push_prefetch_task(dataprovider.Dataprovider):

    def makedata(self):

        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_push_prefetch_task.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "push_prefetch_task"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                file_size = 'file_size=' + '6553548'
                flag = 'flag=' + 'end'
                filedemanddata.write(data_format % (topic, timestamp, file_id, file_size, flag))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_push_prefetch_task.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_push_prefetch_task')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_push_prefetch_task')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_push_prefetch_task['inputtable'])
        print 'data clear done'
