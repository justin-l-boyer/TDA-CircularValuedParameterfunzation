# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# load typical modules
import numpy as np
import pandas as pd
#from dionysus import *
#from dionysus import *
#from dionysus.viewer import *
import matplotlib.pyplot as plt
from subprocess import call
import webbrowser
import os
import heapq
#%matplotlib inline

# load created modules
#from generateData import sineData
#from slideWindowsNoInterp import getSlidingWindow
from plottingPersistence import plotPersistence
from timeDelayEmbedding import embed
#from generateHomology import *

# generate some data

#V = sineData(0, 10, 200, wavelength, std_dev=0.5)
#V=V.transpose().dropna()
#V = V.as_matrix()
plt.plot(V)
dt = 25
stopTau = 30
stopWind = 30
i = dt
j = dt
a=1
for i in np.arange(dt,stopWind):
    elen = i
    print("")
    print(i)
    print("+++++++++++++++++++++++++++")
    a=1
    while a!=0:
        taumax = j
        print(j)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        X = embed(V, taumax, elen, dt) 
        X.astype('float64', order='C')
        np.savetxt('data.txt', X, fmt='%0.19f')
        
        # remove old files
        try:
            os.remove('points-1.val')
        except OSError:
            pass
        try:
            os.remove('points-1.ccl')
        except OSError:
            pass
        try:
            os.remove('points-0.val')
        except OSError:
            pass
        try:
            os.remove('points-0.pdf')
        except OSError:
            pass
        try:
            os.remove('points-0.ccl')
        except OSError:
            pass
        try:
            os.remove('points.vrt')
        except OSError:
            pass
        try:
            os.remove('points.dgm')
        except OSError:
            pass
        try:
            os.remove('points.bdry')
        except OSError:
            pass
        
        print("Removed files")
        
        # run cohomolgy on data
        max_distance = 2
        skeleton = 2
        data_file = 'data.txt' #'sample2noComma.txt'
        max_distance = str(max_distance)
        skeleton = str(skeleton)
        path = './rips-pairwise-cohomology ' + data_file + ' -m '+ max_distance +' -s ' + skeleton + ' -b points.bdry -c points -v points.vrt -d points.dgm'
        call([path], shell=True)
        print("Built Rips")
        
        
        # plot persistence
        dgm = pd.read_table('points.dgm', delim_whitespace=True)
        dgmMax = np.ceil(float(max(dgm.iloc[:,[2]])))
        dgm = dgm.replace('inf', dgmMax*10)
        dgm = dgm.as_matrix()
        print("Top 10 max lifetimes: \n{0}".format("\n".join(str(x) for x in heapq.nlargest(10,dgm[:,2]-dgm[:,1]))))
        #plotPersistence(dgm)
        
        
        # assign each vertex of input to a circle valued function
        a = call(['python2.7 cocycle.py points.bdry points-0.ccl points.vrt'], shell=True)
        call(['python2.7 cocycle.py points.bdry points-1.ccl points.vrt'], shell=True)
        if a==0:
            print("Assigned vertex")
        else:
            print("Vertices not assigned to circle valued function.  Exit")
        j = j +1
        
        if a==0:
            # generate pdf to visulaize values assigned to points
            vis_path = 'python2.7 plot.py points-0.val ' + data_file + ' scatter.py points-0.val points-1.val'
            a = call([vis_path], shell=True)
            if a==0:
                print("Generated graphic")
            
            # open pdf
            webbrowser.open_new(r'file:/home/wilson/Documents/17_Spring/TDA/DelayEmbedding/points-0.pdf')
        elif j==stopTau:
            a=0
            j = dt
    i = i+1

