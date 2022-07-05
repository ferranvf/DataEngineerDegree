#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:29:06 2019

@author: ferran
"""

def indexParaules(nomFitxer):
    f=open(nomFitxer,'r')
    d=dict()
    for indice,a in enumerate(f):
        b=a.lower()
        c=b.replace('.',' ')
        e=c.replace(',',' ')
        j=e.strip()
        g=j.split()
        for h in g:  
            if h not in d:
                d[h]=[[indice,g.count(h)]]
            elif h in d and [indice,g.count(h)]not in d[h]:
                d[h].append([indice,g.count(h)])                
    f.close()
    return(d)

def cercaParaula(paraula,index,nomFitxer):
    f=open(nomFitxer,'r')
    total=list()
    count=0
    for line in f:
        if paraula in index:
            for element in index[paraula]:
                if count==element[0]:
                    line=line.strip('\n')
                    parcial=[line,element[1]]
                    total.append(parcial)     
            count+=1
        else:
            return([])
    f.close()
    return(total)
    
nomFitxer='fitxerParaules.txt'
paraula=input("Paraula: ")
index=indexParaules(nomFitxer)
a=cercaParaula(paraula,index,nomFitxer)
print(a)