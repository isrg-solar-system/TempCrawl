# -*- coding: UTF-8_general_ci -*-
import requests
import json
import sys

headers = {'user-agent': "my-app/0.0.1"}
proxies = {'proxy': "http://192.168.2.12:8080"}
tempapi = requests.get('http://opendata.epa.gov.tw/ws/Data/ATM00698/?$skip=0&$top=300&format=json',
                       headers=headers, proxies=proxies)
uviapi= requests.get('http://opendata2.epa.gov.tw/UV/UV.json',
                       headers=headers, proxies=proxies)
tempData = json.loads(tempapi.text)
uviData = json.loads(uviapi.text)
SN_list = []
for q in range(300):#Add locations to the array to search
    SN_list.append(tempData[q]['SiteName'])
# print SN_list.index(u'臺中')#Taichung ID
serdate = sys.argv[1]#107/3/11
sertime = sys.argv[2]#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
if tempData[int(SN_list.index(u'臺中'))]['DataCreationDate']== serdate+" "+sertime+":00:00":
    print tempData[int(SN_list.index(u'臺中'))]
else:
    print 'Error'