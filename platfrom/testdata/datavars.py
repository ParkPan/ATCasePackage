﻿import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import constvars

file_range=('B64D4E2F75514298872DFFB1075E76B1','C5C382A9AA474D5E9F403790DB6095AD','A42E1002267D4B8D99979B170E982DAB',\
'267B51095D5C4E5286C9D9B12C8C8C7D','6486F18DE7C94FBFA9FE84202AF1B4AF','F43C383B71DB4FE39E5B014AE79BC994','CE079B5664244D67BBDFB9BCEE971C3D',\
'D8441F2AC3E24C9885A18A5FC35253B1','5FB30E0C10804DAFA563D28C9212578A','457B90A86C0B439ABB101A703E779D6B')

peeid_range=('0001000109914A48ACB7D3FD0EE1C77A','00010001D18D453381C1B79B663F4519','000100018A9F499890580C791CA1EF00',\
'00010001EB7642069DD10F2342DD23EE','00010001C21B452DB261BE88C715CB39','00010023146046F19AF9B742EABAAA3F','00000002B33648569758C93F94C3C260',\
'000000026F07468C8E510421F53EBB97','00010016B5A6414E95DB2E98C74DE4BC','00010016B21A44159D5504970954CF4C')

publicip_range=('116.231.160.155','1.2.2.7','116.216.192.88','116.217.255.5','116.252.178.195')

id_range=('10.103.0.3:1450165535:24830099','10.103.0.3:1450165535:24830100','10.103.0.3:1450165535:24830101','10.103.0.3:1450165535:24830102','10.103.0.3:1450165535:24830103',\
'10.103.0.3:1450165535:24830104','10.103.0.3:1450165535:24830105','10.103.0.3:1450165535:24830106','10.103.0.3:1450165535:24830107','10.103.0.3:1450165535:24830108',\
'10.103.0.3:1450165535:24830109','10.103.0.3:1450165535:24830110','10.103.0.3:1450165535:24830111','10.103.0.3:1450165535:24830112','10.103.0.3:1450165535:24830113')

url_range=('ciwen.cloutropy.com/v-9/s-33/l-en/r-720x576/1.flv','http://demo.cloutropy.com/ThePenguinsofMadagascar.flv','http://cdn.cloutropy.com/upgrade/v1_2_5/android/2/libys-jni.so',\
'cdn.cloutropy.com/upgrade/v1_2_5/android/7/Android.json','t031.vod09.icntvcdn.com/media/new/20111/10/20/hd_dy_xqnyh_20111024.ts')

type_range=('hls','vod','live_m3u8','live_flv', 'live_ts', '')

ip2isp={'116.231.160.155':'310000,100017', '1.2.2.7':'110000,1000120', '116.216.192.88':'110000,1000143','116.217.255.5':'210000,100020','116.252.178.195':'450000,100017'}

op_and_error=('OP_PUSH_FILES,E_FAILED','OP_DOWNLOAD_FILE,E_FAILED','OP_GET_SEEDS,E_FAILED',\
'OP_PUSH_FILES,E_NOT_FOUND','OP_DOWNLOAD_FILE,E_NOT_FOUND','OP_GET_SEEDS,E_NOT_FOUND',\
'OP_PUSH_FILES,E_TIMEOUT','OP_DOWNLOAD_FILE,E_TIMEOUT','OP_GET_SEEDS,E_TIMEOUT')

os_versions = ('Android,3.0.50-g16cf890','Windows,6.1')

error2type={'P2P':['OP_PUSH_FILES','OP_GET_SEEDS','OP_REPORT_FILE','OP_PUSH_FILES'],'CDN':['OP_DOWNLOAD_FILE'],'START':['OP_START_HLS','OP_START_CHANNEL']}

url_username = {'ciwen.cloutropy.com/v-9/s-33/l-en/r-720x576/1.flv':'ciwen','http://demo.cloutropy.com/ThePenguinsofMadagascar.flv':'demo',\
'http://cdn.cloutropy.com/upgrade/v1_2_5/android/2/libys-jni.so':'leigang','cdn.cloutropy.com/upgrade/v1_2_5/android/7/Android.json':'leigang',\
't031.vod09.icntvcdn.com/media/new/20111/10/20/hd_dy_xqnyh_20111024.ts':''}

name_list={'00010001':'ciwen','00010002':'lutongnet','00010003':'vst','00010004':'allwinnertech','00010005':'actions-semi','00010006':'tena','00010007':'7po',\
'00010008':'znds','00010009':'hooray','00010011':'youja','00010012':'bjzzxd','00010013':'yppl','00010015':'fiber','00010016':'xiaovo','00010017':'duolebo',\
'00010018':'mufan','00010019':'yuntutv','00010020':'togic','00010021':'mrainbow','00010022':'starschina','00010023':'icntv','00010024':'giec-launcher','00010025':'giec-app',\
'00000002':'demo','00010014':'test','00000000':'yunshang'}

peeredrange=('0001000109914A48ACB7D3FD0EE1C77A','00010001D18D453381C1B79B663F4519','000199998A9F499890580C791CA1EF00',\
'00010001EB7642069DD10F2342DD23EE','00010001C21B452DB261BE88C715CB39','00010023146046F19AF9B742EABAAA3F','00000002B33648569758C93F94C3C260',\
'000000026F07468C8E510421F53EBB97','00010016B5A6414E95DB2E98C74DE4BC','00010016B21A44159D5504970954CF4C',\
'00010007844A4806A555D81485974391','00010025EBED40AC91D728E7BFF08615','00010025BFE044D793DBFD27AC896FA5',\
'00010007ECEA48F68D612D58E5FCB837','00010007B6DD47CAA9E83491E60766A2','00010001B05E447D97670BF3B0C23A73','000100256B174C668DEBD0D47EBFB581',\
'000100013CD44A72A23FC097EF2B0FB8','00010007063745C981F9E9D3D547EFB3','0001002549794533883A18D58849F48C')

urls=('http://cdn.cloutropy.com/thunder/phone_demo_ocean_5mbps.ts','http://cdn.cloutropy.com/thunder/phone_demo_ocean_8mbps.ts','cdn.cloutropy.com/thunder/phone_demo_ocean_3mbps.ts',\
'http://cdn.cloutropy.com/thunder/phone_demo_ocean_7mbps.ts','http://t027.vod05.icntvcdn.com/media/new/2011/09/01/hd_dy_mlf_20110901.ts')

peertype=('CDN', 'SEED')

nattype = (1, 0, 4)

time_format = constvars.recorddate + '%02d%02d22'
time_format_with_second = constvars.recorddate + '%02d%02d%02d'

delay_range = (1, 300, 900, 2300, 2800, 2900, 3400, 3700, 3800, 4000, 4300, 4900, 5600, 7700,  9100)

chunkid_range = (1, 2, 4, 8)

macs=(r'[{"name":"XieYM"\,"addr":"9C-5C-8E-87-6A-25"}]', r'[{"name":"WuYY"\,"addr":"3C:7D:2B:69:1A:2E"}]')
