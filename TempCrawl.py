# -*- coding: UTF-8_general_ci -*-
#上傳今天的個股資料到stockdata資料表
import requests
import request
import json
import pymysql
import datetime
import pandas as pd
import lxml,html5lib
from pandas import Series, DataFrame
import time
from headers import header



start = time.time()
starttime = int(time.strftime("%M", time.localtime()))
now = datetime.datetime.now().strftime("%Y%m%d")

conntime = b = int(time.strftime("%M", time.localtime()))
proxiesList = ["http://60.249.6.104:8080", "http://60.249.6.105:8080",
                   "http://60.249.6.104:8080", "http://192.168.1.3:8080", "http://192.168.2.12:8080",
                   "http://140.168.80.254:8080"] * 1000
if conntime - starttime >= 1:
    headers = {'user-agent': header[l]}
    proxies = {'proxy': proxiesList[l]}
else:  # 找可用IP塞到list
    headers = {'user-agent': "my-app/0.0.1"}
    proxies = {'proxy': "http://192.168.2.12:8080"}
tempapi = requests.get('http://opendata.epa.gov.tw/ws/Data/ATM00698/?$skip=0&$top=300&format=json',
                       headers=headers, proxies=proxies)
uviapi= requests.get('http://opendata2.epa.gov.tw/UV/UV.json',
                       headers=headers, proxies=proxies)
# 地點(SiteName)
# 風力(WindPower)
# 陣風(Gust)
# 溫度(Temperature)
# 相對溼度(Moisture)
# 天氣狀況(Weather)
# 日累積雨量(Rainfall1day)
# UVI
tempData = json.loads(tempapi.text)
uviData = json.loads(uviapi.text)
print tempData[0]['SiteName']
print uviData[2]['UVI']
# select = (
#     '''SELECT * FROM `stockdata` WHERE `date` = "''' + _data[-1][
#         0] + '''" and `sid`="''' + asid + '''"''')
# cursor.execute(select)
# search = cursor.fetchone()
# if search is not None:
#     pass
# else:
db = pymysql.connect(host='60.249.6.104', port=33060, user='root', passwd='ncutim', db='projectiot',
                     charset='utf8')
cursor = db.cursor()
insert = (
    """INSERT  INTO `Temp` (`SiteName`, `WindPower`, `Gust`,`Temperature`,`Moisture`, `Weather`, `Rainfall1day`, `UVI`,`date`,`time`) VALUES (%s,%s,%s,%s, %s, %s, %s, %s,%s,%s)""")
da = (tempData[0]['SiteName'], tempData[0]['WindPower'], tempData[0]['Gust'], tempData[0]['Temperature'],
      tempData[0]['Moisture'], tempData[0]['Weather'], tempData[0]['Rainfall1day'], uviData[2]['UVI'],
      tempData[0]['DataCreationDate'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
cursor.execute(insert, da)
db.commit()
db.close()
end = time.time()
print end - start