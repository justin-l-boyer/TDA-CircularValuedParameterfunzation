#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:42:13 2017

@author: wilson
"""
import numpy as np
from scipy import sparse
def embed(time_series, tau_max, embedding_length, delay=1):
    out=[]
<<<<<<< HEAD
    for tau in range(delay, tau_max+1):
=======
    for tau in range(delay, tau_max):
>>>>>>> fed1a1fde26c5cce57ebc7e20921986502c5eddb
        #unlagged = time_series[:-tau]
        lagged = np.roll(time_series, -tau, axis=0)[:-tau]
        lagged = lagged[0:embedding_length]
        out.append(lagged.tolist())    
<<<<<<< HEAD
    out = np.array(out, dtype=float).transpose()
=======
    out = np.array(out).transpose()
>>>>>>> fed1a1fde26c5cce57ebc7e20921986502c5eddb
    return(out)
        