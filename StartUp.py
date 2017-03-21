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
#%matplotlib inline

# load created modules
from generateData import cosineData
from slideWindows import getSlidingWindow
from plottingPersistence import plotPersistence
#from generateHomology import *

# generate some data
V = cosineData(0, 10, 100, std_dev=0.001)

# slide ya window 1 0.1713 inf -- 1 0.169524 inf
dim = 8
Tau = 1
dT = 1
X = getSlidingWindow(V[:,1], dim, Tau, dT)
#extent = Tau*dim


# write the data to a txt
X.astype('float64', order='C')
np.savetxt('data.txt', X)

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
max_distance = 1.5
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
plotPersistence(dgm)


# assign each vertex of input to a circle valued function
a = call(['python2.7 cocycle.py points.bdry points-0.ccl points.vrt'], shell=True)
call(['python2.7 cocycle.py points.bdry points-1.ccl points.vrt'], shell=True)
if a==0:
    print("Assigned vertex")

# generate pdf to visulaize values assigned to points
vis_path = 'python2.7 plot.py points-0.val ' + data_file + ' scatter.py points-0.val points-1.val'
a = call([vis_path], shell=True)
if a==0:
    print("Generated graphic")

# open pdf
webbrowser.open_new(r'file:/home/wilson/Documents/17_Spring/TDA/DelayEmbedding/points-0.pdf')
