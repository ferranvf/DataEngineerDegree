#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:32:36 2019

@author: ferran
"""
llista=[[1],[1,2],[1,2,3]]
vector_v=[1,2]
class Vector:
    def __init__(self,llista):
        self.llista=llista
    def __str__(self):
        res='['
        for j,i in enumerate(self.llista):
            if j!=0:
                res+=','+str(i)
            else:
                res+=str(i)
        return(res+']')

    def __add__(self,vector_v):
        res=list()
        if len(self.llista)!=len(vector_v.llista):
            raise ValueError
        else:
            for i,j in zip(self.llista,vector_v.llista):
                res.append(i+j)
        return(Vector(res))
                       
    def __mul__(self,n):
        res=list()
        for i in self.llista:
            res.append(i*n)
        return(Vector(res))
        
    def __sub__(self,vector_n):
        res=list()
        if len(self.llista)!= len(vector_n.llista):
            raise ValueError
        else:
            for i,j in zip(self.llista,vector_n.llista):
                res.append(i-j)
            suma=0
            for i in res:
                suma+=i*i
            return(suma**(0.5))     
            
v=Vector(llista)
print(v+vector_v)
print(v)

