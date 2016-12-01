import sys
import constvars
from commonfunc import exec_odps_commands
import os
import MySQLdb


class MysqlDbObj(object):

    dbconn = None

    def __init__(self, h='192.168.1.71', u='ppc', p='yunshang2014', db='test'):
        self.hname = h
        self.user = u
        self.psword = p
        self.dbname = db
        try:
            if MysqlDbObj.dbconn is None:
                MysqlDbObj.dbconn = MySQLdb.connect(self.hname, self.user, self.psword, self.dbname)
        except MySQLdb.MySQLError:
            print 'connect mysql error, please check network or db status ...'
            MysqlDbObj.dbconn = None


    @classmethod
    def selectdatatofile(cls, selectsql, filepath):
        if cls.dbconn is not None:
            try:
                cursor = cls.dbconn.cursor()
                cursor.execute(selectsql)
                if filepath is not None:
                    datas = cursor.fetchall()
                    with open(filepath, 'w') as outputfile:
                        for data in datas:
                            outputfile.write(','.join([str(x) for x in data]) + '\n')
                return True
            except MySQLdb.MySQLError:
                print 'execute mysql query error, please check sql string...'
                return False

        else:
            return None

    @classmethod
    def executesql(cls, execsql):
        if cls.dbconn is not None:
            try:
                cursor = cls.dbconn.cursor()
                cursor.execute(execsql)
                cls.dbconn.commit()
                return True
            except MySQLdb.MySQLError:
                print 'execute mysql query error and db roll back, please check sql string...'
                cls.dbconn.rollback()
                return False
        else:
            return None


def uploaddatatoodps(tablename, filepathname, offsetbasedate=0):
    droppartition = 'alter table %s drop if exists partition(recorddate=%s)' % (
        tablename, str(int(constvars.recorddate) + int(offsetbasedate)))
    addpartition = 'alter table %s add partition(recorddate=%s)' % (
        tablename, str(int(constvars.recorddate) + int(offsetbasedate)))
    uploaddata = 'tunnel u %s %s/recorddate=%s' % (
        filepathname, tablename, str(int(constvars.recorddate) + int(offsetbasedate)))
    commandlines = ';'.join((droppartition, addpartition, uploaddata))
    exec_odps_commands('\"' + commandlines + '\"')


def downloaddatafromodps(tablename, filepathname, offsetbasedate=0, prefixfilepath='default'):
    if prefixfilepath == 'default':
        filepathname = os.path.dirname(__file__) + filepathname
    else:
        filepathname = prefixfilepath + filepathname
    downloaddata = 'tunnel d %s/recorddate=%s %s' % (tablename, str(int(constvars.recorddate) + int(offsetbasedate)), filepathname)
    commandlines = ';'.join((downloaddata,))
    exec_odps_commands('\"' + commandlines + '\"')


def downloaddatafromodpsbypartten(tablename, filepathname, partitionpertten,  prefixfilepath='default'):
    if prefixfilepath == 'default':
        filepathname = os.path.dirname(__file__) + filepathname
    else:
        filepathname = prefixfilepath + filepathname
    downloaddata = 'tunnel d %s/%s %s' % (tablename, partitionpertten, filepathname)
    commandlines = ';'.join((downloaddata,))
    exec_odps_commands('\"' + commandlines + '\"')


def main():
    tablename = sys.argv[1]
    filepathname = sys.argv[2]
    downloaddatafromodps(tablename, filepathname)

if __name__ == "__main__":
    main()
