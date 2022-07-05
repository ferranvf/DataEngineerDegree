#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:19:45 2019

@author: ferran
"""
sol='python'

def check(sol,chars):
    guions=['- ']*len(sol)
    trobat=False
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
        
        
chars=['o', 'p', 'z', 'a', 'n', 'x', 't', 'y', 'h']
a,b=check(sol,chars)
print(a,b)