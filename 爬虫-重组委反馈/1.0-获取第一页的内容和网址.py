# -*- coding: utf-8 -*-
from urllib.request import urlopen 
from bs4 import BeautifulSoup  as bs
import os  
import re  
import sys 
from lxml import etree
from urllib.request import urlopen 
from bs4 import BeautifulSoup  as bs
import os  
import re  
import sys 
from lxml import etree
from docx import Document as doc
from docx.shared import Inches as inc
import pandas as pd
import csv
'''
http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index.htm

http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index_1.htm

一共到第13页 为17年度数据

'''
#生成列表 urladd 里面有第1到24个网址
url0 = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index.htm'
urladd = [url0]
urlstart = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index_'
for i in range(1,25):
    urladd.append(urlstart+str(i)+'.htm')
    print (urladd)

#定义网页的开头
server = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/'
#生成bs对象
b0 = bs(urlopen(urladd[0]),'lxml')
#找到所有的意见
a_df = b0.find(id = "myul")

#列出所有的 文件名和地址
a = a_df.find_all('a')
articles = []

for each in a:
    name = each.string
    add = server + each.get('href')
    articles.append([name,add])
    print (name ,add)
    
    
    
#w 写入 a添加 newline="" 可以有效删除空行
with open('name_add.csv', 'a',newline='',encoding ="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['公司名字','网址'])
    for row in articles:
        writer.writerow(row)


