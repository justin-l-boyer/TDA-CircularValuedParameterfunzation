#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:15:17 2017

@author: wilson
"""

# this script plots the persistence diagram
import matplotlib.pyplot as plt
import numpy as np
def plotPersistence(dgm, degree=1):
    cluster = dgm[:,0]
    birth = dgm[:,1]
    death = dgm[:,2]
    
    plt.scatter(birth[cluster==degree], death[cluster==degree])
    plt.axis([-0.1,max(birth[cluster==degree])+0.25, 0, max(death[cluster==degree])+0.25])
    return(plt.show())
    