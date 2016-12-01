import ReadFile

def inputfile2list(filename):
    inputfilelines = ReadFile.ReadExpectFile(filename)
    inputlist = []
    for inputfileline in inputfilelines:
        inputfileline = inputfileline.replace('\n','')
        inputfileline = inputfileline.replace('\"','')
        inputfileline = inputfileline.replace('{','')
        inputfileline = inputfileline.replace('}','')
        inputfileline = inputfileline.replace(': ','=')
        inputfileline = inputfileline.replace(' ','')

        inputtemplist = inputfileline.split(',')
        inputdict = {}
        for i in range(len(inputtemplist)):
            inputtemplist2 = inputtemplist[i].split('=')
            inputdict[inputtemplist2[0]] = inputtemplist2[1]
        inputlist.append(inputdict)
    return inputlist

def inputfilecontainlist2list(filename):
    inputfilelines = ReadFile.ReadExpectFile(filename)
    inputlist = []
    for inputfileline in inputfilelines:
        inputfileline = inputfileline.replace('\n','')
        inputfileline = inputfileline.replace('\"','')
        inputfileline = inputfileline.replace('{','')
        inputfileline = inputfileline.replace('}','')
        inputfileline = inputfileline.replace(': ','=')
        inputfileline = inputfileline.replace(' ','')

        inputtemplist = inputfileline.split(",")
        inputdict = {}
        for i in range(len(inputtemplist)):
            if inputtemplist[i].find('=[') != -1:
                inputtemplist[i] = inputtemplist[i].split("=[")[1]
            if inputtemplist[i].find(']') != -1:
                inputtemplist[i] = inputtemplist[i][:-1]
            inputtemplist2 = inputtemplist[i].split('=')
            inputdict[inputtemplist2[0]] = inputtemplist2[1]
        inputlist.append(inputdict)
    return inputlist

def inputfilecontaindict2list(filename):
    inputfilelines = ReadFile.ReadExpectFile(filename)
    inputlist = []
    for inputfileline in inputfilelines:
        inputfileline = inputfileline.replace('\n','')
        inputfileline = inputfileline.replace('\"','')
        inputfileline = inputfileline.replace(': ','=')
        inputfileline = inputfileline.replace(' ','')
        inputfileline = inputfileline.replace('={','=@')
        inputfileline = inputfileline.replace('},','**,')
        inputfileline = inputfileline.replace('{','')
        inputfileline = inputfileline.replace('}','')
        inputfileline = inputfileline.replace('[0,0,1,0,0,0,0,0]','###')
        # print inputfileline

        inputtemplist = inputfileline.split(",")
        inputdict = {}
        for i in range(len(inputtemplist)):
            if inputtemplist[i].find('=@') != -1:
                inputtemplist[i] = inputtemplist[i].split("=@")[1]
            if inputtemplist[i].find('**') != -1:
                inputtemplist[i] = inputtemplist[i].split('**')[0]
            if inputtemplist[i].find('###') != -1:
                inputtemplist[i] = inputtemplist[i].replace("###",'[0,0,1,0,0,0,0,0]')
            inputtemplist2 = inputtemplist[i].split('=')
            inputdict[inputtemplist2[0]] = inputtemplist2[1]
        inputlist.append(inputdict)
    return inputlist

def funneloutputfile2list(filename):

    outputfilelines = ReadFile.ReadRealFlie(filename)
    outputlist = []

    for outputfileline in outputfilelines:
        outputfileline = outputfileline.replace('\n', '')
        outputfilelinelist = outputfileline.split("\x1f")
        outputdict = {}
        for i in range(len(outputfilelinelist)):
            outputtemplist = outputfilelinelist[i].split('=')
            outputdict[outputtemplist[0]] = outputtemplist[1]
        outputlist.append(outputdict)
    return outputlist[-10:]

def agentoutputfile2list(filename):

    outputfilelines = ReadFile.ReadExpectFile(filename)
    outputlist = []

    for outputfileline in outputfilelines:
        outputfileline = outputfileline.replace('\n', '')
        outputfilelinelist = outputfileline.split("\x1f")
        outputdict = {}
        for i in range(len(outputfilelinelist)):
            outputtemplist = outputfilelinelist[i].split('=')
            outputdict[outputtemplist[0]] = outputtemplist[1]
        outputlist.append(outputdict)
    return outputlist

def ODPSoutputfile2list(filename):
    outputfilelines = ReadFile.ReadRealFlie(filename)
    outputlist = []

    for outputfileline in outputfilelines:
        outputfileline = outputfileline.replace('\n', '')
        outputfilelinelist = outputfileline.split(",")
        outputlist.append(outputfilelinelist)
    return outputlist

if __name__ == '__main__':
    # a = funneloutputfile2list('idc_peer_connection_report.log')
    # b = inputfile2list('idc_peer_connection_report.txt')
    # c = inputfilecontainlist2list('sdk_vf_version_1.txt')
    # c = inputfilecontainlist2list('sdk_flow_download_version_1.txt')
    # c = inputfilecontainlist2list('sdk_flow_upload_version_1.txt')
    # c = inputfilecontainlist2list('sdk_exception_version_1.txt')
    # c = inputfilecontaindict2list('sdk_performance_vod_version_1.txt')
    # d = funneloutputfile2list('sdk_performance_vod_version_1.log')
    # d = agentoutputfile2list('server_peer_info.txt')
    d = ODPSoutputfile2list('server_live_progress.log')
    # for i in range(len(c)):
    #     print c[i]
    # print c
    for i in range(len(d)):
        print d[i]
    print d
    # print len(d)
    # print d[0]

