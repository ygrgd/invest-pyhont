# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tushare as ts
import matplotlib.finance as mpf  
# os.getcwd()
# myportfolio = pd.read_json('data-protfolio/myportfolio.csv') 
mp = pd.read_excel('data-protfolio/myportfolio.xlsx')
mp.columns = ['name', 'stock', 'buy_date', 'buy_price', 'buy_amount', 'buy_value',
       'now_date', 'now_price', 'now_value', 'now_profit', 'now_percent']
'''
ms = mp.stock
a =ms.values
b =  a.tolist()
type(b)
'''

ms = mp.stock.tolist()

mp.buy_value = mp.buy_price * ms

for k in a:
    print(k)
    
    
    