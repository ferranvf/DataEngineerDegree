#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:51:56 2019

@author: ferran
"""
def dic(fitxer):
    f=open(fitxer,'r')
    d=dict()
    for line in f:
        a=line.strip()
        llista=a.split(" ")
        d[llista[0]]=llista[1:]
    f.close()  
    return(d)
fitxer=input("Nom del fitxer: ")

def afegir_comandes(dic,nom,llista):
    if nom in dic:
        dic[nom].extend(llista)
    else:
        dic[nom]=llista
    return(dic)
dic=dic(fitxer)
nom=input("Introdueix el teu nom: ")
llista=input("Introdueix el llistat de comandes: ")
llista=llista.split(",")

def eliminar_comandes(dicc,nom,codi):
    if nom in dicc:
        if codi in dicc[nom]:
            dicc[nom].remove(codi)
            return(dicc)
        else:
            raise( Exception('Codi no trobat'))
    else:
        raise(Exception ('Nom no trobat'))
   
dicc=dic(fitxer)
nom=input("Introdueix un nom: ")
codi=input("Introdueix el codi a eliminar: ")

def n_comandes(dic):
    d=dict()
    for i,j in dic.items():
        d[i]=len(j)
    return(d)       
dic=dic(fitxer)

def n_comandestotals(dic):
    cont=0
    for i in dic.values():
        for a in i:
            cont+=1
    return(cont)
dic=dic(fitxer)

def clients(dic):
    l=list()
    for j,i in dic.items():
        if len(i)>1:
            l.append(j)
    return(l)
dic=dic(fitxer)

