#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:09:35 2019

@author: ferran
"""

def analitzaFixer(fitxer):
    f=open(fitxer,'r')
    l=list()
    l1=list()
    for line in f.readlines():
        cont=0
        count=0
        for i in line.split():
            a=i.strip()
            count+=int(a)
            cont+=1
        l.append(cont)
        l1.append(count)
    f.close()
    return ("Numero elements per linia: "+str(l)+"\n" + "Suma elements per linia: ",str(l1))    


fitxer='Numeros.txt'
a=analitzaFixer(fitxer)
print (a)