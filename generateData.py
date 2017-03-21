#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:52:35 2017

@author: wilson
"""
import numpy as np
import pandas as pd
# this script generates the sin data
def cosineData(start, stop, number_points, Noise=True, mean=0, std_dev=0.25):
    t = np.linspace(start, stop, number_points)
    y = np.cos(2*np.pi*t)
    if Noise==True:
        noise = np.random.normal(mean, std_dev, len(t))
        y = y + noise
    V = pd.DataFrame([t,y]).transpose()
    V = V.as_matrix()
    return(V)
    
