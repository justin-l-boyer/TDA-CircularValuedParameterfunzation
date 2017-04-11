#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:21:04 2017

@author: wilson
"""

# this script computes the circle valued parameterization
#
# Inputs
# data -- a data file with observations in rows, seperated by a space
# max_distance -- the maximum size of balls for computing complex
# skeleton -- maximum persistence group to compute (default = 2)
#
# Outputs
# points-0.pdf
#

# packages
from subprocess import call
import webbrowser
import os
import heapq

def circleValuedParametrization(data, max_distance, skeleton=2, display=True):
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
    data_file = str(data) #'sample2noComma.txt'
    max_distance = str(max_distance)
    skeleton = str(skeleton)
    path = './rips-pairwise-cohomology ' + data_file + ' -m '+ max_distance +' -s ' + skeleton + ' -b points.bdry -c points -v points.vrt -d points.dgm'
    call([path], shell=True)
    print("Built Rips")
    
    # assign each vertex of input to a circle valued function
    a = call(['python2.7 cocycle.py points.bdry points-0.ccl points.vrt'], shell=True)
    call(['python2.7 cocycle.py points.bdry points-1.ccl points.vrt'], shell=True)
    if a==0:
        print("Assigned vertex")
    else:
        print("Vertices not assigned to circle valued function.  Exit")
        
    
    # generate pdf to visulaize values assigned to points
    vis_path = 'python2.7 plot.py points-0.val ' + data_file + ' scatter.py points-0.val points-1.val'
    a = call([vis_path], shell=True)
    if a==0:
        print("Generated graphic")
    
    if display == True:
        # open pdf
        if a==0:
            webbrowser.open_new(r'file:/home/wilson/Documents/17_Spring/TDA/DelayEmbedding/points-0.pdf')
        else:
            print("Unable to construct circle valued parameterization")
    elif a!=0:
        print("Unable to construct circle valued parameterization")
    return