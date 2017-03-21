#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:17:15 2017

@author: ctraile
"""
# this code computes the sliding window, many thanks to Chris Traile
# 
# Inputs
# x = the 1D signal
# dim = the number of points to sample in each window
# Tau = The amount to skip between each sampled point
# dT = How much we move the window each time
#
# Outputs
# X = 
import numpy as np
import scipy.interpolate as interp

def getSlidingWindow(x, dim, dT):
    N = len(x)
    Tau = N-dim+1
    NWindows = N-dim+1 #int(np.floor((N-dim*Tau)/dT)) #The number of windows
    if NWindows < 0:
        print("Error: Tau too large for signal extent")
        return np.zeros((3, dim))
    X = np.zeros((NWindows, dim)) #Create a 2D array which will store all windows
    idx = np.arange(N)
    IDX = np.zeros((NWindows, dim))
    for i in range(NWindows):
        #Figure out the indices of the samples in this window
        idxx = dT*i + Tau*np.arange(dim) 
        start = int(np.floor(idxx[0]))
        end = int(np.ceil(idxx[-1]))+2
        if end >= len(x):
            X = X[0:i, :]
            break
        #Do spline interpolation to fill in this window, and place
        #it in the resulting array
        X[i, :] = interp.spline(idx[start:end+1], x[start:end+1], idxx)
        IDX[i,:] = idxx
    return X
    #return [X, IDX]