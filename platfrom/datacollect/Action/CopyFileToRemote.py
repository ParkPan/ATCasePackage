import os


def localcopyfile(filename):
    command = os.path.dirname(__file__) + r'\tools\pscp.exe -pw YS.test ' \
        + os.path.dirname(__file__) + r'/../Datafile/expectdatafile/%s.txt test@10.5.0.65:/home/test/TestInput/' % filename
    # print command
    os.system(command)

def localcopyexecutefile():
    command = os.path.dirname(__file__) + r'\tools\pscp.exe -pw YS.test ' \
        + os.path.dirname(__file__) + r'/Execute.py test@10.5.0.65:/home/test/TestInput/'
    # print command
    os.system(command)

if __name__ == '__main__':
    localcopyexecutefile()
