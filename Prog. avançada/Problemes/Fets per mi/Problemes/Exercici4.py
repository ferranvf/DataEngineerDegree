#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:07:02 2019

@author: ferran
"""
l=[1,2,3,4]
k=[2,3,5]
def inteseccio(l,k):
    I=list()
    for i in l:
        for j in k:
            if i in k and j in l:
                if i not in I:
                    I.append(i)
    return(I)
i=inteseccio(l,k)
print(i)

def unio(l,k):
    u=list()
    for i in l:
        if i not in u:
            u.append(i)
    for j in k:
        if j not in u:
            u.append(j)
    return(u)
u=unio(l,k)
print(u)

def multiplicacioLlistes(l,k):
    m=list()
    for i,j in zip(l,k):
        u=i*j
        m.append(u)
    return(m)
m=multiplicacioLlistes(l,k)
print(m)      

def multiplicacioElements(l,k):
    n=0
    h=list()
    l1=list()
    for n in range(len(l)-1):
        for i in k:
            a=i*l[n]
            h.append(a)
    l1+=list(h)
    return(l1)
m=multiplicacioElements(l,k)
print(m)