#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:30:47 2019

@author: ferran
"""

def load_data(filename):
    f=open(filename,'r')    
    l=list()
    for a in f:
        b=a.strip()
        l.append(b)
    return(l)
    f.close()
    
 
llista=['i', 'gos', 'mono', 'cavall', 'gat', 'os', 'gallina', 'tigre', 'cocodril', 'gall', 'rinoceront', 'jirafa', 'elefant', 'porc', 'cangur', 'oca']

