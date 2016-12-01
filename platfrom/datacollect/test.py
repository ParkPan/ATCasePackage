import SendReport
import GlobalVars.IDC
import GlobalVars.SDK
import GlobalVars.SERVER
import Action.CopyFileToLocal
import Action.Comparefile
import Action.File2DictList
import Action.ODPScommand
import time
import os
import WriteServerLog


SendReport.sendreport(GlobalVars.IDC.idc_peer_connection_report['name'])
Action.CopyFileToLocal.remotecopyfile(GlobalVars.IDC.idc_peer_connection_report['name'])
a = Action.Comparefile.comparefilebyitslist(GlobalVars.IDC.idc_peer_connection_report['name'])
print a

# SendReport.sendreport(GlobalVars.IDC.idc_peer_connection_report['name'])
# Action.CopyFileToLocal.remotecopyfile(GlobalVars.IDC.idc_peer_connection_report['name'])
# a = Action.Comparefile.comparefilebyitslist(GlobalVars.IDC.idc_peer_connection_report['name'])
# print a

# SendReport.sendreport(GlobalVars.SDK.sdk_qos_version_1['name'])
# Action.CopyFileToLocal.remotecopyfile(GlobalVars.SDK.sdk_qos_version_1['name'])
# a = Action.Comparefile.comparefilebycontaintypelist(GlobalVars.SDK.sdk_qos_version_1['name'])
# print a

# SendReport.sendreport(GlobalVars.SDK.sdk_vf_version_1['name'])
# Action.CopyFileToLocal.remotecopyfile(GlobalVars.SDK.sdk_vf_version_1['name'])
# a = Action.Comparefile.comparefilebycontaindurationlist(GlobalVars.SDK.sdk_vf_version_1['name'])
# print a


# SendReport.sendreport(GlobalVars.SDK.sdk_exception_version_1['name'])
# Action.CopyFileToLocal.remotecopyfile(GlobalVars.SDK.sdk_exception_version_1['name'])
# a = Action.Comparefile.comparefilebyexceptionlist(GlobalVars.SDK.sdk_exception_version_1['name'])
# print a

# Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_peer_info['inputtable'])
# WriteServerLog.writelog(GlobalVars.SERVER.server_peer_info['name'])
# time.sleep(30)
# Action.ODPScommand.downloaddatafromodps(GlobalVars.SERVER.server_peer_info['name'], GlobalVars.SERVER.server_peer_info['inputtable'], GlobalVars.SERVER.server_recorddate)
# a = Action.Comparefile.compareODPSdata(GlobalVars.SERVER.server_peer_info['name'])
# print a


# Action.ODPScommand.downloaddatafromodps(GlobalVars.SERVER.server_live_progress['name'], GlobalVars.SERVER.server_live_progress['inputtable'], GlobalVars.SERVER.server_recorddate)
# a = Action.Comparefile.compareODPSdata(GlobalVars.SERVER.server_live_progress['name'])
# print a


# import paramiko
#
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect("10.5.0.64", 22, "test", "YS.test")
#
# stdin, stdout, stderr = ssh.exec_command("python --version")
#
# print stdout.readlines()
#
# ssh.close()

