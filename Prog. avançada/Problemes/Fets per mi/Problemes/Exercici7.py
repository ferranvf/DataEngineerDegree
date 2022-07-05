#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:39:02 2019

@author: ferran
"""
import random

diccionari={'feta':['realitzada','produida','elaborada'],'content':['encantat','satisfet','cofoi'],'molt':['força'],'feina':['tasca','ocupació']}
frase = ['està', 'molt', 'content', 'de', 'la', 'feina', 'feta']           

def afegeixSinonim(diccionari, paraula, sinonim):
    l=list()
    if paraula not in diccionari.keys():
        l.append(sinonim)
        diccionari[paraula]=l
    elif paraula in diccionari.keys():
        a=diccionari[paraula]
        for b in a:
            print(' ')
        if sinonim!=b:    
            diccionari[paraula].append(sinonim)
        else:
            diccionari=diccionari
        
    return(diccionari)

paraula=input("Paraula: ")
sinonim=input("Sinònim: ")
a=afegeixSinonim(diccionari,paraula,sinonim)
print(a)

def conversioSinonims(frase,diccionari):
    for index,i in enumerate(frase):
        if i in diccionari:
            a=random.randrange(0,1)
            b=diccionari[i]
            c=b[a]            
    return(frase)
b=conversioSinonims(frase,diccionari)
print(b)
