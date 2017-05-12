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
#from plottingPersistence import plotPersistence
from timeDelayEmbedding import embed
from circular_valued_parameterization import circValAssign
#from generateHomology import *


def findCircParam(time_series, dt, maxRips, startWind, stopWind):
    j = 1
    i = startWind
    a = 1
    stop = 1
    while stop==1:
        elen = i
        print("")
        print(i)
        print("+++++++++++++++++++++++++++")
        a=1
        while a!=0:
            taumax = time_series.shape[0]-elen
            print(j)
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            X = embed(time_series, taumax, elen, dt) 
            X.astype('float64', order='C')
            np.savetxt('data.txt', X, fmt='%0.19f')
            
            circValAssign('./data.txt', j)
            # assign each vertex of input to a circle valued function
            a = call(['python2.7 cocycle.py points.bdry points-0.ccl points.vrt'], shell=True)
            call(['python2.7 cocycle.py points.bdry points-1.ccl points.vrt'], shell=True)
            if a==0:
                print("Assigned vertex")
            else:
                print("Vertices not assigned to circle valued function.  Exit")
                j = j + 1
            
            if a==0:
                stop=0
            elif j==maxRips:
                a=0
                j = 1
        i = i+1
        
    # generate pdf to visulaize values assigned to points
    vis_path = 'python2.7 plot.py points-0.val ' + 'data.txt' + ' scatter.py points-0.val points-1.val'
    a = call([vis_path], shell=True)
    if a==0:
        print("Generated graphic")
    
    # print working embedding length and cutoff parameter
    print("")
    print("The first usable embedding length is {0}".format(i-1))
    print("")
    print("With a maximum Tau of {0}".format(taumax))
    print("")
    print("With a corresponding complex cutoff parameter of {0}".format(j))
    # open pdf
    webbrowser.open_new(r'file:/home/wilson/Documents/17_Spring/TDA/DelayEmbedding/points-0.pdf')
    return(i-1,taumax,j)
