#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:36:04 2019

@author: ferran
"""

from publicacio import Publicacio
import datetime as dt

class Revista(Publicacio):
    
    def __init__(self, títol = ' ', periodicitat = ' ', codi = ' ', exemplars = list()):
        self._titol = títol
        self._periodicitat = periodicitat
        self._codi = codi
        self._exemplars = exemplars
        self._tipus = 'R'
        
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
    def get_periodicitat(self):
        return(self._periodicitat)
    @get_periodicitat.setter
    def periodicitat(self, periode):
        self._periodicitat = periode
    
    @property
    def get_exemplars(self):
        return(self._exemplars)
    @get_exemplars.setter
    def exemplars(self, ex):
        self._exemplars = ex
        
    @property
    def tipus(self):
        return self._tipus
    
        