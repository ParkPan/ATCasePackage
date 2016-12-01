import os
import lib.platfrom.datacollect.GlobalVars.SERVER

def dropodpsdata(tablename):
    droppartition = 'alter table %s drop if exists partition(recorddate=%s)' % (
        tablename, lib.platfrom.datacollect.GlobalVars.SERVER.server_recorddate)
    commandlines = droppartition
    exec_odps_commands('\"' + commandlines + '\"')


def downloaddatafromodps(taskname, tablename, recorddate):

    filepathname = os.path.dirname(__file__) + "/../Datafile/realdatafile/%s.log" % taskname
    downloaddata = 'tunnel d %s/recorddate=%s %s' % (tablename, recorddate, filepathname)
    commandlines = ';'.join((downloaddata,))
    exec_odps_commands('\"' + commandlines + '\"')

def exec_odps_commands(commandlines):

    javacommand = 'java -jar %s %s' % (os.path.abspath(os.path.dirname(__file__)) + "/../../misc/ODPS/odps_helper.jar", commandlines)
    ret = os.system(javacommand)
    return ret

if __name__ == '__main__':
    downloaddatafromodps('server_peer_info', 'raw_input_peer_info', '20160501')
