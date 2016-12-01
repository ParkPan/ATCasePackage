import os


def makeexpecteddata(hour=-1):

    resultfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/HourFilePlayCountAccumulateModeDB.txt', 'r')
    orgdownlines = resultfile.readlines()
    resultfile.close()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w")
    resultlist = {}
    for line in orgdownlines:
        url, username, count, _, play_type = line.split(',')
        play_type = play_type.replace('\n', '')
        if url not in resultlist:
            resultlist[url] = {}
        if username not in resultlist[url]:
            resultlist[url][username] = {}
        resultlist[url][username][play_type] = resultlist[url][username].setdefault(play_type, 0) + int(count)

    for url, users in resultlist.items():
        for user, play_types in users.items():
            for play_type, count in play_types.items():
                expectedfile.write('%s,%s,%d,%s\n' % (url, user, count, play_type))

    expectedfile.close()
    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata()

if __name__ == "__main__":
    main()
