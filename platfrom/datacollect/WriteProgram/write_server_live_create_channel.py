import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_live_create_channel(dataprovider.Dataprovider):

    def makedata(self):

        fileids = ReadConstantFlie('fileiddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_live_create_channel.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "live_create_channel"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                file_url = 'file_url=' + "www.resource.test"
                date_file_url = 'date_file_url=' + "rtmp://live.hkstv.hk.lxdns.com/live/hks"
                rate = 'rate=' + '20000'
                input_video_format = 'input_video_format=' + 'RTMP'
                output_video_format = 'output_video_format=' + 'FLV'
                ppc = 'ppc=' + '2048'
                psize = 'psize=' + '65532'
                filedemanddata.write(data_format % (topic, timestamp, file_id, file_url, date_file_url, rate, input_video_format
                                                    , output_video_format, ppc, psize))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_live_create_channel.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_live_create_channel')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_create_channel')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_create_channel['inputtable'])
        print 'data clear done'