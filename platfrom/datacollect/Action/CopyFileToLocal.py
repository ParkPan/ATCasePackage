import os
from ReadFile import *
import time

def remotecopyfile(localfilename):
    command = os.path.dirname(__file__) + r'\tools\pscp.exe -pw YS.test ' \
              r'test@10.5.0.64:/home/test/Testfunnel/logs/report.log ' \
              + os.path.dirname(__file__) + r'\..\Datafile\tempfile\report.log'
    # print command
    os.system(command)

    '''
    make new file save that data we need compare
    '''

    time.sleep(0.05)
    outputfilelines = ReadTempFlie('report.log')
    templist = outputfilelines[-10:]
    filename = os.path.abspath(os.path.dirname(__file__)) + "/../Datafile/realdatafile/%s.log" % localfilename
    testfile = open(filename, 'w')
    testfile.writelines(templist)
    testfile.close()


if __name__ == '__main__':
    remotecopyfile("localfilename")