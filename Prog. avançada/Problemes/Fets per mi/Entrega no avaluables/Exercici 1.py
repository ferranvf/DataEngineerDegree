#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:35:57 2019

@author: ferran
"""
import math

class NombreRacional():
    
    def __init__(self, numerador = 0, denominador = 0):
        self._numerador=numerador
        self._denominador=denominador
    
    @property
    def numerador(self):
        return(self._numerador)
    
    @numerador.setter
    def numerador(self,valor):
        self._numerador = valor
    
    @property
    def denominador(self):
        return(self._denominador)
    
    @denominador.setter
    def denominador(self,nombre):
        self._denominador = nombre
    
    def esValid(self):
        valid = False
        if self._denominador != 0:
            valid = True
        return(valid)
    
    def simplifica(self):
        if self._denominador == 0:
            return(self._numerador)
        return math.gcd(self._denominador, (self._numerador % self._denominador))
    def __add__(self, s):
        return (NombreRacional())
  
        
