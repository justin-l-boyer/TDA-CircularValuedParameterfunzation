#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:23:23 2017

@author: wilson
"""
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from subprocess import call
#import webbrowser
#import os
#import heapq
##%matplotlib inline
#
from timeDelayEmbedding import embed
from circular_valued_parameterization import circleValuedParametrization

#~~~~~~~~~~~~~~~~~~Noisy Sine~~~~~~~~~~~~~~~~~~~
#
#from generateData import sineData
#wavelength=3
#V = sineData(0, 10, 200, wavelength, std_dev=0.01)
#plt.plot(V[:,0],V[:,1])
#taumax = 140
#elen = 60
#dt = 40 
#X = embed(V[:,1], taumax, elen, dt)
#
#X.astype('float64', order='C')
#np.savetxt('data.txt', X, fmt='%0.19f')
#
#circleValuedParametrization('./data.txt', 8)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~Heartbeat~~~~~~~~~~~~~~~~~~~~~~~
#
#import scipy.io.wavfile
#from sklearn import preprocessing
#
#Fs, X = scipy.io.wavfile.read("./audio/Heartbeat.wav")
#X = preprocessing.scale(X[:len(X)/2].reshape(-1,1))
##plt.plot(X)
#
#V = X[::500]
#plt.plot(np.arange(len(V)), V)
#
#dt = 13 #np.argmin(V[:int(len(V)*0.05)])
#taumax = 355 #int(dt + len(V)*0.01)
#elen = 73
#D = embed(V, taumax, elen, dt) 
#D=D[0]
#
## save file for dionysus
#D.astype('float64', order='C')
#np.savetxt('data.txt', D, fmt='%0.10f')
#
#circleValuedParametrization('./data.txt', 25)
##
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`




#~~~~~~~~~~~~~~~~~~~~~~Beach Waves~~~~~~~~~~~~~~~~~~~~
#
from iterateEmbed import findCircParam
import scipy.io.wavfile
from sklearn import preprocessing

Fs, X = scipy.io.wavfile.read("./audio/Beach Waves.wav")
X = preprocessing.scale(X[:len(X)/2].reshape(-1,1))
#plt.plot(X)

V = X[::1000]
plt.plot(np.arange(len(V)), V)

dt = 60 #np.argmin(V[:int(len(V)*0.05)])

#maxRips = 50
#startWind = 23
#stopWind = 100
#elen, taumax, ep = findCircParam(V[:,0],dt,maxRips,startWind,stopWind)


elen = 150
ep = 60
taumax = V.shape[0] - elen
D = embed(V[:,0], taumax, elen, dt)
D.astype('float64', order='C')
np.savetxt('data.txt', D, fmt='%0.10f')
circleValuedParametrization('./data.txt', ep)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~