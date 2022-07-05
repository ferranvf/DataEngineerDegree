#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 11:16:13 2019

@author: ferran
"""
import numpy as np


def mitjanaLliuraments(notes,estudiant):
    if -1 not in notes[estudiant, ...]:
        for i in notes[estudiant, ...]:
            mean=np.mean(notes[estudiant, ...])
        return(mean)    
    else:
        return(0)
m=mitjanaLliuraments(notes,estudiant)    
print(m)

def nAprovats(notes):
    count=0
    for a in notes:
        if -1 not in a:
            if np.mean(a)>=5:
                count+=1
    return(count)

n=nAprovats(notes)
print(n)

def resultatExercici(notes,ex):
    minim=notes[0,0]
    maxim=notes[0,0]
    ad=0
    count=0
    p=0
    for a in notes:
        if a[ex]!=-1:
            if minim > a[ex]:
                minim=a[ex]
            elif maxim<=a[ex]:
                maxim=a[ex]
            ad+=a[ex]
            count+=1
            p+=1
    return(p,minim,maxim,ad/count)

r=resultatExercici(notes,ex)
print(r)

def abandonamentsSetmanals(notes):
    abandonamentsTotals=list()
    for j in range(len(notes[0, ...])):
        abandonaments_Setmanals=0
        for i in range(len(notes[..., 0])):
            fora=False
            if notes[i,j]==-1 and j==0:
                fora=True
                for k in notes[i,j:]:
                    if k!=-1:
                        fora=False
            elif notes[i,j]==-1 and notes[i,j-1]!=-1:
                fora=True
                for k in notes[i,j:]:
                    if k!=-1:
                        fora=False
            if fora:
                abandonaments_Setmanals+=1
        abandonamentsTotals.append(abandonamentsSetmanals)
    return(abandonamentsTotals)
                
a=abandonamentsSetmanals(notes)
print(a)
