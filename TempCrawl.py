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
yesterday = datetime.datetime.now().strftime("%Y%m%d")
# try:
    #     db = pymysql.connect(host='60.249.6.104', port=33060, user='root', passwd='ncutim', db='Listing',
    #                          charset='utf8')
    # except:
    #     pass
    # cursor = db.cursor()
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
res = requests.get('http://opendata.epa.gov.tw/ws/Data/ATM00698/?$skip=0&$top=300&format=json',
                       headers=headers, proxies=proxies)
try:
    allData = json.loads(res.text)
    print allData[0]
        # select = (
        #     '''SELECT * FROM `stockdata` WHERE `date` = "''' + _data[-1][
        #         0] + '''" and `sid`="''' + asid + '''"''')
        # cursor.execute(select)
        # search = cursor.fetchone()
        # if search is not None:
        #     pass
        # else:
        #     insert = (
        #         """INSERT  INTO `stockdata` (`date`, `sid`, `name`,`market`,`coe`, `shareTrades`, `turnover`, `open`, `high`, `low`, `closing`,`grossspread`,`tradingvolume`,`time`) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)""")
        #     da = (_data[-1][0], asid, aname, amarket, acoe, float(st), float(to), float(open), float(high),
        #           float(low),
        #           float(closing),
        #           _data[-1][7], float(tv), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     cursor.execute(insert, da)
        #     db.commit()
        # db.close()
except:
    pass;
end = time.time()
print end - start