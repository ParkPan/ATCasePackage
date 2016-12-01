
import sys
import types
import WriteProgram.dataprovider



def writealllog():
    m = sys.modules['WriteProgram.dataprovider']
    attstr = dir(m)
    for str in attstr:
        att = getattr(m, str)
        if type(att) == types.ModuleType:
            subattstr = dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt) == types.TypeType and issubclass(subatt, m.Dataprovider):
                    tmpObj = subatt()
                    tmpObj.cleardata()
                    tmpObj.makedata()
                    tmpObj.writelog()

def writeonelog(taskname):
    m = sys.modules['WriteProgram.dataprovider']
    attstr = dir(m)
    for str in attstr:
        att = getattr(m, str)
        if type(att) == types.ModuleType:
            subattstr = dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt) == types.TypeType and subatt.__name__ == taskname and issubclass(subatt, m.Dataprovider):
                    tmpObj = subatt()
                    tmpObj.cleardata()
                    tmpObj.makedata()
                    tmpObj.writelog()
            else:
                continue
            break


if __name__ == '__main__':
    writealllog()
    # writeonelog("server_push_prefetch_task")