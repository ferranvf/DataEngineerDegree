#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:02:49 2019

@author: ferran
"""

import punt

class Poligon():
    maxim=1000
    def __init__(self):
        self._vertexs=list()
        self._topLeft=punt.Point()
        self._bottomRight=punt.Point()
        
    def afegirVertex(self,pt):
        self._vertexs.append(pt)
        self._topLeft.x=min([p.x for p in self._vertexs])
        self._topLeft.y=max([p.y for p in self._vertexs])
        self._bottomRight.x=max([p.x for p in self._vertexs])
        self._bottomRight.y=min([p.y for p in self._vertexs])
    @property
    def topLeft(self):
        return(self._topLeft)
    @property 
    def bottomRight(self):
        return(self._bottomRight)
    
    def __str__(self):
        return(self._bottomRight)
    
    def perimetre(self):
        a=self._vertexs[1:]
        for i,j in zip(self._vertexs,a):
            costat=i-j
        self.perimetre+=costat
        return(self.perimetre)
    
                