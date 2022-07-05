#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:52:15 2019

@author: ferran
"""

def analitzarFitxer(fitxer):
    f=open(fitxer,'r')
    cont=0
    contador=0
    num=0
    for i in f.readlines():
        cont+=1
        for lletra in i.split(" "):
            a=lletra.strip(" ")
            l=a.split()
            for j in l:
                m=j.lower()
                contador+=1
                for n in m:
                    num+=1
    return(cont,contador,num)
    f.close()
            
fitxer=input("Nom del fitxer: ")
a=analitzarFitxer(fitxer)
print(a)