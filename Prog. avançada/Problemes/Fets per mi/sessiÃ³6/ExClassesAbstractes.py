#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:46:17 2019

@author: ferran
"""

import abc
from punt import Point
import numpy as np

class Figura(metaclass = abc.ABCMeta): #Ens indica que es una classe abstracta
    @abc.abstractclassmethod
    def area(self):
        raise NotImplementedError
    @abc.abstractclassmethod
    def perimetre(self):
        raise NotImplementedError
    @abc.abstractclassmethod
    def llegeix(self):
        raise NotImplementedError
    @abc.abstractclassmethod
    def __str__(self):
        raise NotImplementedError

class Cercle(Figura):
    def __init__(self):
        self._centre=Point()
        self._radi=0.0
    def area(self):
        return np.pi*self._radi**2
    def perimetre(self):
        raise NotImplementedError
    def llegeix(self):
        x=float(input("Coordenada x del cercle: "))
        y=float(input("Coordenada y del cercle: "))
        self._centre=Point(x,y)
        self._radi=float(input("radi del cercle: "))
    def __str__(self):
        resultat="Centre: "+str(self._centre)+"\n"
        resultat+="Radi: "+str(self._radi)+"\n"
        return(resultat)
class Rectangle(Figura):
    def __init__(self):
        self._topLeft=Point(0.0,0.0)
        self._alçada=0.0
        self._allargada=0.0
        self._area=0.0
        self._perimetre=0.0
    def area(self):
        self._area=(self._alçada*self._allargada)
        return(self._area)
    def perimetre(self):
        self._perimetre=(2*self._alçada+2*self._allargada)
        return(self._perimetre)
    def llegeix(self):
        x=float(input("Coordenada x del rectangle: "))
        y=float(input("Coordeanda y del rectangle: "))
        self._topLeft=Point(x,y)
        self._alçada=y
        self._allargada=x
    def __str__(self):
        resultat="Origen: "+str(self._topLeft)+"\nAlçada: "+str(self._alçada)+"\nAllargada: "+str(self._allargada)
        resultat+="\nArea: "+str(self._area)+"\nPerimetre: "+str(self._perimetre)
        return(resultat)
        
        
        
        