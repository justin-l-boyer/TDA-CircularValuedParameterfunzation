#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 05:12:53 2017

@author: wilson
"""

# this script retrieves stock data and aligns it into a suitable format
import pandas as pd
from pandas_datareader import data
import datetime

# looking at staocks 
start = datetime.datetime(2014,1,1)
end = datetime.datetime(2016,12,30)

# look at s&p500
snp = data.DataReader("GSPC", 'yahoo', start, end)

# check out a picture
import matplotlib.pyplot as plt
%matplotlib inline
%pylab inline
pylab.rcParams['figure.figsize']=(5,3)
snp["Adj Close"].plot(grid=True)

# compute the 20 day moving average
snp["20d"] = np.round(snp["Close"].rolling(window = 20, center=False).mean(),2)

# normalize on the 200 day moving average
snp = snp.reset_index()
Y = snp["20d"][:-1].dropna()
X = pd.Series(range(1,len(Y)+1))
Z = pd.ols(x=X,y=Y, intercept=True)
W = X*0.003+19.8532
V = Y-W
V.plot(grid=True)
V=V.transpose().dropna()
V = V.as_matrix()
