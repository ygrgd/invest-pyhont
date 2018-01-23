# -*- coding: utf-8 -*-

"""
@author: LZ
"""

import requests
from bs4 import BeautifulSoup  as bs
from docx import Document as doc
import pandas as pd
import sqlalchemy as say
from sqlalchemy import create_engine
'''
import csv
from urllib.request import urlopen 
import os  
import re  
import sys 
from lxml import etree
from urllib.request import urlopen 
from docx.shared import Inches as inc
'''
'''
http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index.htm
http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index_1.htm
一共到第13页 为17年度数据
'''
# =============================================================================
# 生成目标一级网页列表  url_all
# =============================================================================
#生成列表 urladd 里面有第1到25个网址
url_0 = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index.htm'
url_all = [url_0]
url_start = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index_'

for i in range(1,25):
    url_all.append(url_start+str(i)+'.htm')
    print (url_all)

# =============================================================================
# 获取每个二级网页的 名称和网址
# =============================================================================
#定义二级网页的开头

'''以下 为测试使用
#使用requests获取网页，生成bs对象

response = requests.get(url0)
response.encoding = 'utf-8'
soup = bs(response.text,'lxml')

items = soup.find(id = "myul").find_all('li')

item = items[0]
title = item.find('a').get_text()
title_url = urlstart + item.find('a').attrs['href']
date = item.find('span').get_text()
'''
server = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj'
articles = []
url_test = []

for url in url_all:
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = bs(response.text,'lxml')
    items = soup.find(id = "myul").find_all('li')
    for item in items:
        title = item.find('a').get_text()
        title_url = server + item.find('a').attrs['href'][1:]
        date = item.find('span').get_text()
        if title_url in url_test:
            print('重复了')
        else:
            url_test.append(title_url)
            articles.append([title,title_url,date])
#            print (title,title_url,date)
            
            


# =============================================================================
# 先存入pd，然后存入sql
# =============================================================================
sec_pages = pd.DataFrame(articles)
sec_pages.columns = ['title','url','date']
sec_pages['content']= ''


sec_pages.to_excel('sec_pages1.xlsx')


engine = create_engine('mysql://root:@127.0.0.1/csrc?charset=utf8',echo = False)  # 定义引擎
engine.execute('show databases').fetchall()
engine.execute('use csrc')

sec_pages.to_sql('bgczfkyj', engine, if_exists='append') 


# =============================================================================
# 以上已经成功存入了sql
# =============================================================================
engine.execute('slesct * frome bgczfkyj')




engine = create_engine('mysql://root:@127.0.0.1/stock?charset=utf8',echo = False)


engine.execute('select * from bgczfkyj').fetchall()
url = engine.execute('select url from bgczfkyj').fetchall()
    

















