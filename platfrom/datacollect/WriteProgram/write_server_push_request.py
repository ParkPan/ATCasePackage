import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_push_request(dataprovider.Dataprovider):

    def makedata(self):


        data_format = '%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_push_request.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "push_request"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                request_url = 'request_url=' + "http://request.test.com"
                response_status_code = 'response_status_code=' + '200'
                filedemanddata.write(data_format % (topic, timestamp, request_url, response_status_code))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_push_request.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_push_request')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_push_request')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_push_request['inputtable'])
        print 'data clear done'