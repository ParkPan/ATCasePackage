import os

__constantfilepath = os.path.dirname(__file__) + '/../Datafile/constantfile/'
__expectdatafilepath = os.path.dirname(__file__) + '/../Datafile/expectdatafile/'
__realdatafilepath = os.path.dirname(__file__) + '/../Datafile/realdatafile/'
__tempfilepath = os.path.dirname(__file__) + '/../Datafile/tempfile/'

def ReadConstantFlie(filename):
    with open(__constantfilepath + filename) as file:
        filedata = file.readlines()
    return filedata

def ReadExpectFile(filename):
    with open(__expectdatafilepath + filename) as file:
        filedata = file.readlines()
    return filedata

def ReadRealFlie(filename):
    with open(__realdatafilepath + filename) as file:
        filedata = file.readlines()
    return filedata

def ReadTempFlie(filename):
    with open(__tempfilepath + filename) as file:
        filedata = file.readlines()
    return filedata