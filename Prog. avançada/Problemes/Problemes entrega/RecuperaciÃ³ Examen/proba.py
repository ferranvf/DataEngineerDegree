#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:35:30 2019

@author: ferran
"""
actors=['Amador Recio Coke']
a='Maite'
def PushActor(actors,a):
    
    actors.append(a)
    return(actors)
      
p=PushActor(actors,a)
print(p)