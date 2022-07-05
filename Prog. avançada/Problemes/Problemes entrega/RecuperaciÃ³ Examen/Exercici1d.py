#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:57:01 2019

@author: ferran
"""
import random

def load_data(filename):
    f=open(filename,'r')    
    l=list()
    for a in f:
        b=a.strip()
        l.append(b)
    return(l)
    f.close()
    
    
def filter_and_select(llista,n):
    l=list()
    for i in llista:
        j=set(i)
        if len(j)>=n:
            l.append(i)
    b=random.randint(0,len(l)-1)
    c=l[b]
    return(c)

def check(sol,chars):
    guions=['- ']*len(sol)
    trobat=False
    t=''
    if chars!=[]:
        for a in chars:
            if a in sol:
                for i in range(len(sol)):
                    if sol[i]==a:
                        guions[i]=str(a)+' '
                        t="".join(guions)[:-1]
        if sol==t.replace(" ",""):
            trobat=True
            return(trobat,str(t))
        else:
            return(trobat,str(t))
             
    else:
        return (trobat,"".join(guions)[:-1])
    
    
    
filename=input("Introdueix el nom del fitxer: ")
n=int(input("Numero mínim de carácters diferents: "))
llista=load_data(filename)
sol=filter_and_select(llista,n)
errors=0
trobat=False
chars=list()
while errors<10 and not trobat:
    caràcter=input("Introdueix lletra: ")
    if caràcter not in chars:
        chars.append(caràcter)
    else:
        caràcter=input("La lletra ja hi es, introdueix una altre lletra: ")  
        chars.append(caràcter)
    ch,chk=check(sol,chars)
    print(ch,chk)
    if caràcter not in sol:
        errors+=1
    if ch==True:
        trobat=True
    print("Número d'errors: ",errors)

if trobat:
    print("HAS GUANYAT!!!")
else:
    print("HAS PERDUT!!! La paraula era ",sol)


