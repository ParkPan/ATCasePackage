from File2DictList import *

'''
the method compare list not contain child list and also not contain the key 'type'
'''
def comparefilebyitslist(filename):
    inputlist = inputfile2list(filename + '.txt')
    # inputlist = inputfilecontaindict2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False

'''
the method compare list contain child list and the key 'type'
input key : type or fod_type, startup_delay
output key : play_type, duration
'''

def comparefilebycontaintypelist(filename):
    inputlist = inputfilecontainlist2list(filename + '.txt')
    # inputlist = inputfile2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if inputlist[i][keys[k]] == outputlist[j]['play_type']:
                        keyscount += 1
                    continue
                if keys[k] == 'startup_delay':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['duration']):
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False

'''
the method compare list contain child list and keys 'absolute_time','timestamp','source_type'
input key : 'absolute_time','timestamp','source_type'
output key : 'timestamp','input_time','play_type'
'''

def comparefilebycotainabtimelist(filename):
    inputlist = inputfilecontainlist2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['input_time'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'absolute_time':
                    if inputlist[i][keys[k]] == outputlist[j]['timestamp']:
                        keyscount += 1
                    continue
                if keys[k] == 'source_type':
                    if inputlist[i][keys[k]] == outputlist[j]['play_type']:
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False

'''
the method compare list contain child list and the key 'type'
input key : type or fod_type, duration
output key : play_type, duration(+'000')
'''

def comparefilebycontaindurationlist(filename):
    inputlist = inputfilecontainlist2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if inputlist[i][keys[k]] == outputlist[j]['play_type']:
                        keyscount += 1
                    continue
                if keys[k] == 'duration':
                    if int(inputlist[i][keys[k]] + '000') == int(outputlist[j]['duration']):
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False

'''
the method compare list contain child list
input key : type or fod_type, duration, p2pDown, httpDown, p2pUp
output key : play_type, duration(+'000'), p2p_download, cdn_download, upload
'''

def comparefilebycontaindownloadlist(filename):
    inputlist = inputfilecontainlist2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if inputlist[i][keys[k]] == outputlist[j]['play_type']:
                        keyscount += 1
                    continue
                if keys[k] == 'duration':
                    if int(inputlist[i][keys[k]] + '000') == int(outputlist[j]['duration']):
                        keyscount += 1
                    continue
                if keys[k] == 'p2pDown':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['p2p_download']):
                        keyscount += 1
                    continue
                if keys[k] == 'httpDown':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['cdn_download']):
                        keyscount += 1
                    continue
                if keys[k] == 'p2pUp':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['upload']):
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False


'''
the method compare list not contain child list and also not contain the key 'type'
input key :name, osVersion, osType, coreVersion, cpuModel, publicPort, natType, privateIP, privatePort
output key :None, os_version, os_type, core_version, cpu_model, public_port, nat_type, private_ip, private_port
'''
def comparefilebyexceptionlist(filename):
    inputlist = inputfilecontainlist2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'name':
                    keyscount += 1
                    continue
                if keys[k] == 'osVersion':
                    if inputlist[i][keys[k]] == outputlist[j]['os_version']:
                        keyscount += 1
                    continue
                if keys[k] == 'osType':
                    if inputlist[i][keys[k]] == outputlist[j]['os_type']:
                        keyscount += 1
                    continue
                if keys[k] == 'coreVersion':
                    if inputlist[i][keys[k]] == outputlist[j]['core_version']:
                        keyscount += 1
                    continue
                if keys[k] == 'cpuModel':
                    if inputlist[i][keys[k]] == outputlist[j]['cpu_model']:
                        keyscount += 1
                    continue
                if keys[k] == 'publicPort':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['public_port']):
                        keyscount += 1
                    continue
                if keys[k] == 'natType':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['nat_type']):
                        keyscount += 1
                    continue
                if keys[k] == 'privateIP':
                    if inputlist[i][keys[k]] == outputlist[j]['private_ip']:
                        keyscount += 1
                    continue
                if keys[k] == 'privatePort':
                    if int(inputlist[i][keys[k]]) == int(outputlist[j]['private_port']):
                        keyscount += 1
                    continue
                if keys[k] == 'addr':
                    if inputlist[i][keys[k]] == outputlist[j]['macs']:
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                    inputlist.remove(inputlist[i])
                    keyscount = 0
                    comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    print len(inputlist)
    if len(inputlist) == 0:
        return True
    else:
        return False

'''
the method compare list not contain child list ,it method create for case sdk_performace
'''
def comparefilebyperformancelist(filename):
    inputlist = inputfilecontaindict2list(filename + '.txt')
    outputlist = funneloutputfile2list(filename + '.log')
    comparenum = len(inputlist)
    i = 0
    while i < comparenum:
        keys = inputlist[i].keys()
        print len(keys)
        keyscount = 0
        for j in range(len(outputlist)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    #inputlist[i]['timestamp'] = inputlist[i]['timestamp']
                    longnum = long(inputlist[i]['timestamp'])
                    longnum2 = long(outputlist[i]['timestamp'])
                    if abs(longnum - longnum2) < 3000:
                        keyscount += 1
                    continue
                if keys[k] == 'httpDown':
                    if inputlist[i][keys[k]] == outputlist[j]['http_download']:
                        keyscount += 1
                    continue
                if keys[k] == 'p2pDown':
                    if inputlist[i][keys[k]] == outputlist[j]['p2p_download']:
                        keyscount += 1
                    continue
                if keys[k] == 'startDelay':
                    if inputlist[i][keys[k]] == outputlist[j]['start_delay']:
                        keyscount += 1
                    continue
                if keys[k] == 'fwdSeeks':
                    if inputlist[i][keys[k]] == outputlist[j]['fwd_seeks']:
                        keyscount += 1
                    continue
                if keys[k] == 'bwdSeeks':
                    if inputlist[i][keys[k]] == outputlist[j]['bwd_seeks']:
                        keyscount += 1
                    continue
                if keys[k] == 'seekDelay':
                    if inputlist[i][keys[k]] == outputlist[j]['seek_delay']:
                        keyscount += 1
                    continue
                if keys[k] == 'bufferCnt':
                    if inputlist[i][keys[k]] == outputlist[j]['buffer_cnt']:
                        keyscount += 1
                    continue
                if keys[k] == 'bufferDelay':
                    if inputlist[i][keys[k]] == outputlist[j]['buffer_delay']:
                        keyscount += 1
                    continue
                if inputlist[i][keys[k]] == outputlist[j][keys[k]]:
                    keyscount += 1
            if keyscount == len(keys):
                inputlist.remove(inputlist[i])
                keyscount = 0
                comparenum -= 1
        if (j + 1) == len(outputlist):
            break
    if len(inputlist) == 0:
        return True
    else:
        return False

def compareODPSdata(filename):
    inputlists = agentoutputfile2list(filename + '.txt')
    outputlists = ODPSoutputfile2list(filename + '.log')
    inputlen = len(inputlists)
    outputlen = len(outputlists)
    listcount = 0
    itemcount = 0
    for i in range(inputlen):
        del inputlists[i]['topic']
        keys = inputlists[i].keys()

        for j in range(outputlen):
            for key in keys:
                if inputlists[i][key] in outputlists[j]:
                    itemcount += 1
            if itemcount == len(inputlists[i]):
                itemcount = 0
                listcount += 1
                break
            else:
                itemcount = 0

    if listcount == inputlen:
        return True
    else:
        return False

def compareODPSdataOutputwithoutPIP(filename):
    inputlists = agentoutputfile2list(filename + '.txt')
    outputlists = ODPSoutputfile2list(filename + '.log')
    inputlen = len(inputlists)
    outputlen = len(outputlists)
    listcount = 0
    itemcount = 0
    for i in range(inputlen):
        del inputlists[i]['topic']
        del inputlists[i]['public_ip']
        keys = inputlists[i].keys()

        for j in range(outputlen):
            for key in keys:
                if inputlists[i][key] in outputlists[j]:
                    itemcount += 1
            if itemcount == len(inputlists[i]):
                itemcount = 0
                listcount += 1
                break
            else:
                itemcount = 0

    if listcount == inputlen:
        return True
    else:
        return False


if __name__ == '__main__':
    # c = comparefilebyperformancelist('sdk_performance_vod_version_1')
    c = compareODPSdata('server_peer_info')

    # c = comparefilebyexceptionlist('sdk_exception_version_1')
    # c = comparefilebycotainabtimelist('sdk_live_delay_version_1')
    if c:
        print "EQUAL!"
    else:
        print "NOT EQUAL!!!"