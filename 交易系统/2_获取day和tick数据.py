# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tushare as ts
import matplotlib.finance as mpf  
from matplotlib.pylab import date2num
import datetime
import time
#获取今日的日期
today =  (time.strftime("%F"))

#读取股票代码 myportfolio
mp = pd.read_excel('data-protfolio/myportfolio.xlsx')
mp.columns = ['name', 'stock', 'buy_date', 'buy_price', 'buy_amount', 'buy_value',
       'now_date', 'now_price', 'now_value', 'now_profit', 'now_percent']

#提取股票代码并转换成列表 mystock
ms = mp.stock.tolist()
# 另一种简单方式
# ms1=mp['stock']

for i in ms:
    print(i)
    if i<10000:
        i = ('000%s' %(i))
        print(i)
        tp = ts.get_k_data('%s' %(i))
        tp.to_excel("e:/git/python/交易系统/data-day/%s.xlsx" %(i))
    else:
        print(i)
        tp = ts.get_k_data('%d' %(i))
        tp.to_excel("e:/git/python/交易系统/data-day/%d.xlsx" %(i))
        
#########以下为 获取tick数据        
st = ts.get_today_ticks('ms[4]')

df = ts.get_tick_data('000586',date='2014-01-09')
df.head(10)



for i in ms:
    b = str(i)
    print(b)
    print(type(b))

a= 568

###############新测试

mp.to_csv("data-protfolio/myportfolio.csv",encoding = "utf-8")

mp = pd.read_csv('data-protfolio/myportfolio.csv',index_col =0)
ms1=mp['stock']


mp['stock'] = mp['stock'].map(lambda x : x.strip("'"))

mp

df['b']=df['b'].astype(str).str.zfill(4)

mp['stock']=mp['stock'].astype(str).str.zfill(6)
mp









