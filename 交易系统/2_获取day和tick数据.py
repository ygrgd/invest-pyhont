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

# 获取目录下所有的文件名称，type为list
a = glob.glob('e:/git/python/交易系统/data-day/*.csv')
type(a)

#获取今日的日期
today =  (time.strftime("%F"))
print(today)

#读取持仓文件，存入mp中，把stock列补充为6位。
mp = pd.read_csv('data-protfolio/myportfolio.csv',index_col =0)
mp.columns = ['name', 'stock', 'buy_date', 'buy_price', 'buy_amount', 'buy_value',
       'now_date', 'now_price', 'now_value', 'now_profit', 'now_percent']

#先把stock列填充为6位，然后再改成字符串格式
mp['stock']=mp['stock'].astype(str).str.zfill(6) 
mp['stock'] = mp['stock'].astype('str')


#df = pd.read_excel ("test.xlsx" , converters={‘类别编码‘:str}) 另一种处理代码方法
######没有找到生成多个df的方法########

#存储持仓数据到源文件，使用uft-8编码
mp.to_csv("data-protfolio/myportfolio.csv",encoding = "utf-8")

#提取股票代码并转换成列表 mystock  ms = mp.stock.tolist()可以用简单方法mp['stock']
for i in mp['stock']:
    print()
    tp = ts.get_k_data('%s' %(i))
    tp.to_csv("e:/git/python/交易系统/data-day/%s.csv" %(i),encoding = "utf-8")

# tp.to_excel("e:/git/python/交易系统/data-day/%s.xlsx" %(i))


     
#########以下为 获取tick数据    
    
#获取今天的日期
date = []
cur_date = datetime.date.today() 

#把前10天的日期生成date列表
for i in range(0,10):
    print()
    day = cur_date - datetime.timedelta(days= i)
    day = day.strftime('%Y-%m-%d')
    print(day)
    date.append(day)
    print(date)
    
#获取tick数据并存储
for day in date:
    for i in mp['stock'][4:]:
        print(type(i))
        tick =ts.get_tick_data(i,date = day,pause=5)
        tick.to_csv("e:/git/python/交易系统/data-tick/%s-%s.csv" %(i,day),encoding = "utf-8")
    
  











