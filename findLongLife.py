#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:46:35 2017

@author: wilson
"""
import numpy as np
# this script finds the outlier lifetimes
def outlierLifetimes(dgm, degree=1, thresh=3.5):
    cluster = dgm[:,0]
    birth = dgm[:,1]
    death = dgm[:,2]
    life = death-birth
    life = life[cluster==degree]
    median = np.median(life, axis=0)
    diff = life-median
    diff = np.abs(life-median)
    med_abs_deviation = np.median(diff)
    modified_z_score = 0.6745 * diff/med_abs_deviation
    return life[modified_z_score > thresh]