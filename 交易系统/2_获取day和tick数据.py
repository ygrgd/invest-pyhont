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
import glob


import datetime


a = glob.glob('e:/git/python/交易系统/data-day/*.csv')
type(a)
#获取今日的日期
today =  (time.strftime("%F"))

#读取股票代码 myportfolio
mp = pd.read_csv('data-protfolio/myportfolio.csv',index_col =0)
mp.columns = ['name', 'stock', 'buy_date', 'buy_price', 'buy_amount', 'buy_value',
       'now_date', 'now_price', 'now_value', 'now_profit', 'now_percent']
mp['stock']=mp['stock'].astype(str).str.zfill(6) #填充为6位

#df = pd.read_excel ("test.xlsx" , converters={‘类别编码‘:str}) 另一种处理代码方法
######没有找到生成多个df的方法########

mp.to_csv("data-protfolio/myportfolio.csv",encoding = "utf-8")

#提取股票代码并转换成列表 mystock  ms = mp.stock.tolist()
# 另一种简单方式 # ms1=mp['stock']
for i in mp['stock']:
    tp = ts.get_k_data('%s' %(i))
    tp.to_csv("e:/git/python/交易系统/data-day/%s.csv" %(i),encoding = "utf-8")

# tp.to_excel("e:/git/python/交易系统/data-day/%s.xlsx" %(i))

for i in mp['stock']:
    print(i)
    df=pd.DataFrame()
    i = df




'''
for i in mp['stock']:
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
 '''       
#########以下为 获取tick数据        
# 日期处理,获取前n天的日期
date = []
cur_date = datetime.date.today() 
for i in range(0,10):
    print()
    day = cur_date - datetime.timedelta(days= i)
    day = day.strftime('%Y-%m-%d')
    print(day)
    date.append(day)
    print(date)
    
for day in date:
    for i in mp['stock'][4:]:
        print(type(i))
        tick =ts.get_tick_data(i,date = day)
        tick.to_csv("e:/git/python/交易系统/data-tick/%s-%s.csv" %(i,day),encoding = "utf-8")
    
    
    
    
for i in mp['stock'][:4]:
    tp = ts.get_k_data('%s' %(i))
    tp.to_csv("e:/git/python/交易系统/data-day/%s.csv" %(i),encoding = "utf-8")
  
    
    
yesterday = cur_date - datetime.timedelta(days=1)



df = ts.get_tick_data('000586',date='2014-01-09')












