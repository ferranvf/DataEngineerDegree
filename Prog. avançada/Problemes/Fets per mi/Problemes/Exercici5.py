#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:35:30 2019

@author: ferran
"""

def masterMind(combinacio, intents, maxIntents):
    l=list()
    for intento in range(maxIntents):
        l1=list()
        for i,j in zip(combinacio,intents[intento]):
            if i==j:
                l1.append(1)
            elif i!=j and j in combinacio:
                l1.append(0)
            else:
                l1.append(-1)
        l.append(l1)
        if l1==[1,1,1,1,1]:
            break
    return(l)
 
       
            
        
combinacio=[0,2,4,6,8]
intents=[[1,2,3,4,5],[0,2,4,6,7],[1,2,4,7,8],[7,8,9,7,4],[0,2,4,6,8]]
maxIntents=5
a=masterMind(combinacio,intents,maxIntents)
print(a)