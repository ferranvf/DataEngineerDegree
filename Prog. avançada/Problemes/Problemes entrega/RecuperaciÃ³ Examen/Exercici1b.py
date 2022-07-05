#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:16:01 2019

@author: ferran
"""
import random 
llista=['i', 'gos', 'mono', 'cavall', 'gat', 'os', 'gallina', 'tigre', 'cocodril', 'gall', 'rinoceront', 'jirafa', 'elefant', 'porc', 'cangur', 'oca']
def filter_and_select(llista,n):
    l=list()
    for i in llista:
        j=set(i)
        if len(j)>=n:
            l.append(i)
    b=random.randint(0,len(l))
    c=l[b]
    return(c)
n=1
a=filter_and_select(llista,n)
print(a)