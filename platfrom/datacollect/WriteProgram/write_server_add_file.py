import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import Action.ODPScommand
import GlobalVars.SERVER

class server_add_file(dataprovider.Dataprovider):

    def makedata(self):

        fileids = ReadConstantFlie('fileiddb.txt')
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_add_file.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "add_file"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                url = 'url=' + "test.cloudtropy.com"
                fsize = 'fsize=' + '35536056'
                psize = 'psize=' + '12036'
                ppc = 'ppc=' + '12'
                username = 'username=' + 'tester'
                filedemanddata.write(data_format % (topic, timestamp, file_id, url, fsize, psize, ppc, username))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_add_file.txt'


    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_add_file')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_add_file')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_add_file['inputtable'])
        print 'data clear done'
