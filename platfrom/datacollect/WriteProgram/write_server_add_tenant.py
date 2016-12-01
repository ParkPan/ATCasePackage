import os
import random
from lib.platfrom.datacollect.Action.GetTimeStamp import *
from lib.platfrom.datacollect.GlobalVars.SERVER import *
from lib.platfrom.datacollect.Action.ReadFile import *
import dataprovider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_add_tenant(dataprovider.Dataprovider):


    def makedata(self):

        peerids = ReadConstantFlie('peeriddb.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/'\
                                                               'server_add_tenant.txt', 'w') as filedemanddata:
            for i in range(10):
                topic = "topic=" + "add_tenant"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                tenant_id = 'tenant_id=' + "testtenantid" + str(random.randint(1, 100000))
                tenant_name = 'tenant_name=' + "testusename"
                groups = 'groups=' + 'TG1'
                peer_prefix = 'peer_prefix=' + peerids[random.randint(0, 2500)][0:8]
                domain = 'domain=' + 'mail.Mytest.com'
                filedemanddata.write(data_format % (topic, timestamp, tenant_id, tenant_name, groups, peer_prefix, domain))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expectdatafile/server_add_tenant.txt'

    def writelog(self):
        Action.CopyFileToRemote.localcopyfile('server_add_tenant')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_add_tenant')

    def cleardata(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_add_tenant['inputtable'])
        print 'data clear done'