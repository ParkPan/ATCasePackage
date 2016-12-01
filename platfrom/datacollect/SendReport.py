import os
import types
import CaseKey.idc_peer_connection_report
import CaseKey.sdk_exception_version_1
import CaseKey.sdk_flow_download_version_1
import CaseKey.sdk_flow_upload_version_1
import CaseKey.sdk_fod_version_1
import CaseKey.sdk_live_delay_version_1
import CaseKey.sdk_offering_version_1
import CaseKey.sdk_performance_vod_version_1
import CaseKey.sdk_push_state_version_1
import CaseKey.sdk_qos_version_1
import CaseKey.sdk_vf_version_1
import CaseKey.sdk_vv_version_1


def sendreport(taskname):
    for pyfile in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/CaseKey'):
        if pyfile.endswith('.py') and not pyfile.startswith('__init__'):
            tmpmodule = __import__('CaseKey.%s' % pyfile[:-3])

    attstr = dir(tmpmodule)
    # print(attstr)

    for astr in attstr:
        if astr.find(taskname) > -1:
            att = getattr(tmpmodule, astr)

            # print(att)
            # print(type(att))

            if type(att) == types.ModuleType:
                subattstr = dir(att)

                # print dir(att)

                for substr in subattstr:
                    subatt = getattr(att, substr)

                    # print subatt

                    if type(subatt) == types.FunctionType and subatt.__name__ == 'sendlog':
                        subatt()
                        break
                else:
                    continue
                break


if __name__ == '__main__':
    sendreport('idc_peer_connection_report')