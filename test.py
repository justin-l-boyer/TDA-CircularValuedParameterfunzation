#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:52:18 2017

@author: wilson
"""
from slideWindows import getSlidingWindow
dim = 1
Tau = 1
dT = 1
X = getSlidingWindow(V[:,1], dim, Tau, dT)
#extent = Tau*dim

t = np.linspace(0,2*np.pi, X.shape[0])
for i in range(X.shape[1]):
    plt.plot(t,X[:,i])
