import os
import tornado.httpclient
import json
import random
import Action.ReadFile
import Action.GetTimeStamp
import GlobalVars.SDK_REPORT
import GlobalVars.URL

def sendlog():
    prefix = "/sdk/qos/version/1"
    peerids = Action.ReadFile.ReadConstantFlie("peeriddb.txt")
    fileids = Action.ReadFile.ReadConstantFlie("fileiddb.txt")
    exceptfile = open(os.path.abspath(os.path.dirname(__file__)) +
                      "/../Datafile/expectdatafile/%s.txt" % __name__.split('.')[-1], 'w')
    body_data = GlobalVars.SDK_REPORT.sdk_qos_version_1

    for i in range(10):
        randindex = random.randint(0, 2500)
        url = GlobalVars.URL.Funnelhost + prefix
        body_data["id"] = fileids[randindex].replace("\n", "")+":"+str(random.randint(1000, 1000000))
        body_data["peer_id"] = peerids[randindex].replace("\n", "")
        body_data['timestamp'] = Action.GetTimeStamp.get_timestamp_now()
        jdata = json.dumps(body_data)
        exceptfile.write(jdata + "\n")
        client = tornado.httpclient.HTTPClient()
        resp = client.fetch(url, method="POST", body=jdata, headers={'Content-Type': 'application/json'})
        print "response from " + str(i) + " request: " + resp.body
    exceptfile.close()

    print "sdkofferingversion1 script execute finish..."
    return os.path.abspath(os.path.dirname(__file__)) + "../Datafile/outputdatafile/%s.txt" % __name__.split('.')[-1]

if __name__ == '__main__':
    sendlog()
