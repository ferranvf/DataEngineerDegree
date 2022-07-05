#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:38:04 2019

@author: ferran
"""

def Hamming(b1,b2):
    count=0
    for a,b in zip(b1,b2):
        if a!=b:
            count+=1
    return(count)
    
b1='0100101001'
b2='1101101010'
a=Hamming(b1,b2)
print(a)