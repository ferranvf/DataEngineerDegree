#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:43:38 2019

@author: ferran
"""
def primers(n):
    esPrimer=[True]*(n+1)
    esPrimer[0]=esPrimer[1]=False
    primers=[]
    for i in range(n+1): #fet per mi
        if esPrimer[i]==True:
            primers.append(i)
            for j in range(i,(n+1),i):
                esPrimer[j]=False
        
    return(primers)
n=int(input("Introdueix un numero: "))
a=primers(n)
print(a)
    
#    for index,valor in enumerate(esPrimer):#Fet pel profe
#        if valor:
#            primers.append(index)
#            for i in range(index,n+1,index):
#                esPrimer[i]=False
#    return(primers)