#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:30:05 2017

@author: wilson
"""
from dionysus import *
from dionysus import *
from dionysus.viewer import *

def genRips(data, skelton, cutoff):
    distances = PairwiseDistances(data) # construct pairwise distance
    rips = Rips(distances) # initialize rips with distance1
    simplices = Filtration()
    rips.generate(skelton, cutoff, simplices.append) # generate rips for each simplice
    print("Number of simplices", len(simplices))
    show_complex(data,simplices)
    return(rips, simplices)

def genPersistenceDiagram(simplices, rips):
    simplices.sort(rips.cmp) # sort the filtration with respect to comparision of simplices
    p = StaticPersistence(simplices) # initilize boundary matrix
    p.pair_simplices() # reduce boundary matrix

    dgms = init_diagrams(p, simplices, rips.eval)
    show_diagram(dgms[:2])
    return(p)
