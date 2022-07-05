#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:46:15 2019

@author: ferran
"""

from publicacio import Publicacio
import datetime as dt #per afegir 30 dies utilitzem dt.timedelta(days=30)

class Prestec(Publicacio):
    
    def __init__(self,DNI = ' ',codi='',dataPrestec=[]):
        self._DNI = DNI
        self._codi=codi
        self._dataPrestc = dataPrestec
        self._dataRetrn = []
    
    @property
    def DNI(self):
        return(self._DNI)
    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI
    
    @property
    def dataPrestc(self):
        return(self._dataPrestc)
    @dataPrestc.setter
    def dataPrestc(self, data):
        f = dt.datetime.strptime(str(data), "%Y-%m-%d")
        dat = f.date()
        self._dataPrestc = dat
    
    @property
    def dataReturn(self):
        return(self._dataRetrn)
    @dataReturn.setter
    def dataReturn(self, d):
        self._dataRetrn = self._dataPrestc + dt.timedelta(days = int(d))   
        