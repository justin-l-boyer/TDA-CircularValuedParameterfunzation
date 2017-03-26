#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:52:35 2017

@author: wilson
"""
import numpy as np
import pandas as pd
# this script generates the sin data
<<<<<<< HEAD
def sineData(start, stop, number_points, wavelength, Noise=True, mean=0, std_dev=0.25):
    t = np.linspace(start, stop, number_points)
    y = np.sin(2*np.pi/float(wavelength)*t)
=======
def cosineData(start, stop, number_points, Noise=True, mean=0, std_dev=0.25):
    t = np.linspace(start, stop, number_points)
    y = np.cos(2*np.pi*t)
>>>>>>> fed1a1fde26c5cce57ebc7e20921986502c5eddb
    if Noise==True:
        noise = np.random.normal(mean, std_dev, len(t))
        y = y + noise
    V = pd.DataFrame([t,y]).transpose()
    V = V.as_matrix()
    return(V)
    
<<<<<<< HEAD
def incomSineData(start, stop, number_points, wavelength, Noise=False, mean=0, std_dev=0.25):
    t = np.linspace(start, stop, number_points)
    y=np.zeros(len(t))
    y = np.sin(2*np.pi/float(wavelength)*t)+np.sin(20*t/float(wavelength))
    if Noise==True:
        noise = np.random.normal(mean, std_dev, len(t))
        y = y + noise
    V = pd.DataFrame([t,y]).transpose()
    V = V.as_matrix()
    return(V)
=======
>>>>>>> fed1a1fde26c5cce57ebc7e20921986502c5eddb
