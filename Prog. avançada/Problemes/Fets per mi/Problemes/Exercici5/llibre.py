#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:44:06 2019

@author: ferran
"""

from publicacio import Publicacio
import datetime as dt

class Llibre(Publicacio):
    
    def __init__(self, codi = ' ', títol = ' ', autor = ' ', nºcopies = 0, nºdies = 0):
        self._codi = codi
        self._titol = títol
        self._autor = autor
        self._copies = nºcopies
        self._dies  = nºdies
        self._tipus = 'L'
    
    @property 
    def get_codi(self):
        return(self._codi)    
    @get_codi.setter
    def codi(self, codi):
        self._codi = codi
        
    @property
    def get_titol(self):
        return(self._titol)
    @get_titol.setter
    def titol(self, titol):
        self._titol = titol
        
    @property
    def get_autor(self):
        return(self._autor)
    @get_autor.setter
    def autor(self, autor):
        self._autor = autor
    
    @property
    def get_copies(self):
        return(self._copies)
    @get_copies.setter
    def copies(self, copies):
        self._copies = copies
    
    @property
    def get_dies(self):
        return(self._dies)
    @get_dies.setter
    def dies(self, dies):
        self._dies = dies
    @property
    def tipus(self):
        return self._tipus    
        
      
    