#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:56:49 2019

@author: ferran
"""

class Film:
    def __init__(self,titol,director,any,actors):
        self.titol=titol
        self.director=director
        self.any=any
        self.actors=actors
    def __ge__(self,m):
        if self.any>=m:
            return(True)
        else:
            return(False)
    def PushActor(self,a):
        self.actors.append(a)
        return(Film(self.titol,self.director,self.any,self.actors))
    def PopActor(self,a):
        for j in self.actors:
            if j==a:
                self.actors.remove(a)
        return(Film(self.titol,self.director,self.any,self.actors))
    def __str__(self):
        missatge=''
        for l in self.actors:
            missatge+=str(l)+" "
        return('{0} {1} {2} {3}'.format(self.titol,self.director,self.any,missatge[:-1]))

titol=input("Titol: ")
director=input("Director: ")
any=input("Any estrena: ")
actor=input("Llistat d'actors: ")
actors=list()
actors.append(actor)

m='2000'
a='Victor'
F=Film(titol,director,any,actors)
print(F)
print(F.__ge__(m))
print(F.PushActor(a))
print(F.PopActor(a))
