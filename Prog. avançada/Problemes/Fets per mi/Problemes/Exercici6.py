#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:50:36 2019

@author: ferran
"""

def indexCaracter(nomFitxer):
    f=open(nomFitxer,'r')
    d=dict()
    l=list()
    l1=list()
    for i in f:
        print(i)
        a=i.lower()
        b=a.replace(':',' ').replace(';',' ').replace(',',' ').replace('.',' ').replace('?',' ').replace('!',' ')
        c=b.split()
        for a in c:
            for i in a:
                if i not in l:
                    l.append(i)
                else:
                    l1.append(i)
                    
                
    f.close()
    return(d)

 
nomFitxer='fitxerParaules1.txt'
a=indexCaracter(nomFitxer)
print(a)

#def maxParaulaCaracter(index):