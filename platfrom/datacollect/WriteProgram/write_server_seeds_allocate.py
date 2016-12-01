import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER

class server_seeds_allocate(dataprovider.Dataprovider):

    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_seeds_allocate.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "seeds_allocate"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                seed_peer_id = 'seed_peer_id=' + "2.4.0.1"
                slice_map = 'slice_map=' + '3'
                public_ip = 'public_ip=' + '192.168.0.110'
                public_port = 'public_port=' + '8888'
                # private_ip = 'private_ip=' + '10.5.0.254'
                private_port = 'private_port=' + '8080'
                ppc = 'ppc=' + '1024'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, public_ip, public_port,
                                                    private_port, seed_peer_id, slice_map, ppc))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_seeds_allocate.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_seeds_allocate')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_seeds_allocate')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_seeds_allocate['inputtable'])
        print 'data clear done'
