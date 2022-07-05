#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:27:07 2019

@author: ferran
"""

llista=[1,2,3,4]
def SumaAcomulada(llista):
    suma=0
    l1=list()
    for i in llista:
        suma+=i
        l1.append(suma)
    return(l1)
r=SumaAcomulada(llista)
print(r)

def factoriallista(llista):
    l1=list()
    fact=1
    for i in llista:
        fact= fact*i
        l1.append(fact)
    return(l1)
a=factoriallista(llista)
print(a)

def primers(llista):
    primers=list()
    n=1
    for i in llista:
        if i!=0 and i!=1:
            primers.append(i)
            n+=1
    return(primers)
n=[1,2,3,4]
b=primers(llista)
print(b)

def eliminarDuplicats(llista):
    for i in llista:
        if i not in llista:
            llista.append(i)
    return(llista)
llista=[1,2,3,4,2,1,5,4]
e=eliminarDuplicats(llista)
print(e)

def binariADecimal(binari):
    num=len(binari)-1
    res=0
    for i in binari:
        if i==0:
            res=res
            num-=1
        else:
            res=res+(int(i)*2**num)
            num-=1
    return(res)

binari=input("Introdueix un nombre en binari: ")
a=binariADecimal(binari)
print(a)
          
        

    
