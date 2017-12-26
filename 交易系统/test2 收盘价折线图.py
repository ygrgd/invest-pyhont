# -*- coding: utf-8 -*-
import matplotlib as mpl
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
# %matplotlib inline
wdyx = ts.get_k_data('002739','2017-01-01')
wdyx.close.plot(legend=True,figsize=(10,4))
wdyx.volume.plot(legend=True,figsize=(10,4))

fig = plt.figure()