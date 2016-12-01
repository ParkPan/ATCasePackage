import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_live_push_error(dataprovider.Dataprovider):

    def makedata(self):


        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_live_push_error.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "live_push_error"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                level = 'level=' + "warn"
                module = 'module=' + 'testmodle'
                err_info = 'err_info=' + 'TESTERROE!!!'
                filedemanddata.write(data_format % (topic, timestamp, level, module, err_info))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_live_push_error.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_live_push_error')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_push_error')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_push_error['inputtable'])
        print 'data clear done'