# -*- coding: UTF-8_general_ci -*-
import requests
import json
import sys
import time
tempFormat = time.strftime("%Y/%m/%d %H", time.localtime())
tempTime = tempFormat.replace(tempFormat[0:4], str(int(tempFormat[0:4])- 1911))#抓temp時間
uviFormat = time.strftime("%Y-%m-%d %H", time.localtime())
proxiesList = ["http://60.249.6.104:8080", "http://60.249.6.105:8080",
               "http://60.249.6.104:8080", "http://192.168.1.3:8080"]
proxies = {'proxy': "http://60.249.6.105:8080"}
headers = {'user-agent': "my-app/0.0.1"}
tempapi = requests.get('http://opendata.epa.gov.tw/ws/Data/ATM00698/?$skip=0&$top=300&format=json',
                       headers=headers,proxies = proxies)
uviapi= requests.get('http://opendata2.epa.gov.tw/UV/UV.json',
                       headers=headers,proxies = proxies)
tempData = json.loads(tempapi.text)
uviData = json.loads(uviapi.text)
serplace = sys.argv[1]#地點
uviSN_list = []
tempSN_list = []


if serplace == 'taichung':
        serplace = u'臺中'

for q in range(33):#Add locations to the array to search
    uviSN_list.append(uviData[q]['SiteName'])
for w in range(300):#Add locations to the array to search
    tempSN_list.append(tempData[w]['SiteName'])
SiteName = tempData[int(tempSN_list.index(serplace))]['SiteName']
WindPower = tempData[int(tempSN_list.index(serplace))]['WindPower']
Gust = tempData[int(tempSN_list.index(serplace))]['Gust']
Temperature = tempData[int(tempSN_list.index(serplace))]['Temperature']
Moisture = tempData[int(tempSN_list.index(serplace))]['Moisture']
Weather = tempData[int(tempSN_list.index(serplace))]['Weather']
Rainfall1day = tempData[int(tempSN_list.index(serplace))]['Rainfall1day']
UVI = uviData[int(uviSN_list.index(serplace))]['UVI']
print '{["SiteName":"'+SiteName+'","WindPower":"'+WindPower+'","Gust":"'+Gust+'","Temperature":"'+Temperature+'","Moisture":"'+Moisture+'","Weather":"'+Weather+'","Rainfall1day":"'+Rainfall1day+'","UVI":"'+UVI+'"]}'
# if tempData[int(SN_list.index("u'"+serplace+"'"))]['DataCreationDate']== serdate+" "+sertime+":00:00":
#     print tempData[int(SN_list.index("u'"+serplace+"'"))]
# else:
#     print 'Error'