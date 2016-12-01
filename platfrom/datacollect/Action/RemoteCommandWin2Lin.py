import os

def executecommand(command):
    os.system(command)

def startwriterlog(filename):
    command = 'plink -ssh -pw YS.test test@10.5.0.65 "python /home/test/TestInput/Execute.py /home/test/TestInput/%s"' % filename
    os.system(command)

if __name__ == '__main__':
    startwriterlog('server_peer_info')
