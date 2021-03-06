import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_heartbeat(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_heartbeat.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "heartbeat"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                sdk_version = 'sdk_version=' + "2.4.1"
                nat_type = 'nat_type=' + "3"
                public_ip = 'public_ip=' + '192.168.0.110'
                public_port = 'public_port=' + '8888'
                private_ip = 'private_ip=' + '10.5.0.254'
                private_port = 'private_port=' + '8080'
                filedemanddata.write(data_format % (topic, timestamp, sdk_version, nat_type, peer_id, public_ip, public_port, private_ip,
                                                    private_port))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_heartbeat.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_heartbeat')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_heartbeat')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_heartbeat['inputtable'])
        print 'data clear done'