# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:11:15 2018

@author: LZ
"""

import requests
from bs4 import BeautifulSoup  as bs
from docx import Document as doc
import pandas as pd
import sqlalchemy as say
from sqlalchemy import create_engine
import MySQLdb
from sqlalchemy import connection

engine = create_engine('mysql://root:@127.0.0.1/csrc?charset=utf8',echo = False)  # 定义引擎
engine.execute('use csrc')
engine.execute('select * from bgczfkyj').fetchall()

conn = engine.connect()

url = engine.execute('select url from bgczfkyj').fetchall()
title = engine.execute('select title from bgczfkyj').fetchall()

sec_pages = pd.read_sql_table('bgczfkyj',engine)


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# =============================================================================
# 定义ORM表格
# =============================================================================
metadata = MetaData()

bgczfkyj = Table('bgczfkyj', metadata,\
Column('index', String,),\
Column('title', String),\
Column('url', String,primary_key=True),\
Column('date', String),\
Column('content', String)\
 )



document = doc()
document.close()
# =============================================================================
# 修改标题，165、472会出问题
# =============================================================================
for i in range(473,497):
    print(i)
    response = requests.get(url[i][0])
    response.encoding = 'utf-8'
    soup = bs(response.text,'lxml')
    title_0 = soup.title.get_text()
    items = soup.find_all('div',{'class':"Custom_UnionStyle"})
    content = items[0].text.replace('\xa0'*8,'\n\n')
    print('正在更新第'+str(i)+'个标题')
    arg = 'UPDATE bgczfkyj SET title=\'%s\' WHERE url=\'%s\''%(title_0,url[i][0])
    engine.execute(arg)
    print('第'+str(i)+'个标题更新完成')
       
# =============================================================================
# 写入content，参数转义会出点问题165、472会出问题
# =============================================================================
    
for i in range(473,497):
    print(i)
    url_0 = url[i][0]
    response = requests.get(url_0)
    response.encoding = 'utf-8'
    soup = bs(response.text,'lxml')
#    title_0 = soup.title.get_text()
    items = soup.find_all('div',{'class':"Custom_UnionStyle"})
    content_0 = items[0].text.replace('\xa0'*8,'\n\n')
    print('正在更新第'+str(i)+'个内容')
    stmt = bgczfkyj.update().where(bgczfkyj.c.url==url_0).values(content=content_0)
    conn.execute(stmt)

# =============================================================================
# 以下是采用 sqy文档中的办法
# =============================================================================


stmt = bgczfkyj.update().where(bgczfkyj.c.url==url_0).values(content=content_0)
conn.execute(stmt)















    arg = 'UPDATE bgczfkyj SET content= \'%s\' WHERE url=\'%s\' ' %(str(content),url_0)
    engine.execute(arg)    
    
    engine.execute('UPDATE bgczfkyj SET content= \'%s\' WHERE url=\'%s\' ' %(content,url_0)).fetchall()
    
    
    
    engine.execute(arg,(repr(content),url_0))
    conn.execute(arg,(repr(content),url_0))

sql=('insert into students(Id,Name) values(%d,"%s")'%(int(Id),name))









    conn.execute(arg)
    engine.execute(arg) 
    engine.execute(('UPDATE bgczfkyj SET content= \''+content + 'WHERE url=\''+ url + '\'').str())
    print('第'+str(i)+'个内容更新完成')
    
    
    
    
# =============================================================================
# 
# =============================================================================
    
    
    arg = ('UPDATE bgczfkyj SET content=\'%s\'' WHERE url=\'%s\'' %(,title_0,url[0][0]))
    engine.execute(arg)
    
update.encode('utf-8)


engine.execute('UPDATE bgczfkyj SET content = '111',title = '关于深圳市新纶科技股份有限公司发行股份购买资产并募集配套资金申请的二次反馈意见' WHERE url = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/201801/t20180119_332842.html'')


engine.execute('UPDATE bgczfkyj SET content = \\\'\n深圳市新纶科技股份有限公司：\n\u3000\u30002017年11月23日，我会受理了你公司发行股份购买资产的申请。12月14日，我会向你公司发出书面反馈意见，2018年1月5日，你公司报送了反馈意见回复。经审核，现提出以下反馈意见：\n\u3000\u30001.申请材料显示，1）中信证券股份有限公司（以下简称中信证券）为本次重组独立财务顾问。2）截至2017年9月30日，中信证券持有深圳市新纶科技股份有限公司（以下简称新纶科）1.49%股份，全部为新纶科技控股股东侯毅及新纶科技核心管理团队通过其所设立的资产管理计划在2015年增持的新纶科技股票。目前，“昊青价值稳健10号投资基金”已将上述股份减持完毕，中信证券不持有新纶科技股份。3）中信证券控制的中信证券投资有限公司（以下简称中信投资）、金石坤享股权投资（杭州）合伙企业（有限合伙）（以下简称金石坤享）为本次重组交易对方，合计持有标的资产9%股权，重组后合计持有上市公司1.07%股份。请你公司补充披露：1）昊青价值稳健10号投资基金的主要信息，包括但不限于管理人、管理人费用率、与中信证券之间的关系、中信证券通过该基金持有新纶科技股票期间及减持后的总体收益、管理机制等。2）中信证券通过上述基金买卖新纶科技股票取得的收益占本次重组财务顾问费的比例，中信投资和金石坤享投资标的资产及参与本次重组的预期收益占本次重组财务顾问费的比例。3）中信证券自营账户、昊青价值稳健10号投资基金、中信投资和金石坤享之间是否独立运行，中信证券是否与上市公司存在利害关系，其担任本次重组独立财务顾问是否符合《上市公司并购重组财务顾问业务管理办法》第十七条的规定。请独立财务顾问和律师核查并发表明确意见。\n\u3000\u30002.申请材料显示，2017年3月，标的公司股东唐千军、劳根洪将持有的部分股份转让给中信投资、金石坤享等四名投资者。标的公司前次交易整体估值与本次交易价格存在较大差异。请你公司进一步补充披露两次交易中标的公司估值差异较大的原因及合理性。请独立财务顾问核查并发表明确意见。\n\u3000\u3000你公司应当在收到本通知之日起30个工作日内披露反馈意见回复，披露后2个工作日内向我会报送反馈意见回复材料。\n\u3000\u3000联系人：孟会恩\xa0010-88061450\xa0zjhczw@csrc.gov.cn' ,title = '关于深圳市新纶科技股份有限公司发行股份购买资产并募集配套资金申请的二次反馈意见' WHERE url = 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/201801/t20180119_332842.html'')






for i in range(1,len(url)):
    xx = str(data[i])
    xxx = xx.split(',')
    name = xxx[0][2:]
    add = xxx[1][:-2]
    print(add)
   # file = urlopen('http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/201801/t20180112_332401.html')
    #file = urlopen('http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/./201801/t20180112_332401.html')
    file = urlopen(add)
    print('现在正在下载第'+str(i+1)+'个')
    print(add)
    b0 = bs(file,'lxml')
    a = b0.find_all('div',{'class':"Custom_UnionStyle"})
    fkyj = a[0].text.replace('\xa0'*8,'\n\n')
    document.add_heading(name, level=1)
    document.add_paragraph(fkyj)
    document.add_page_break()
    print(name)

