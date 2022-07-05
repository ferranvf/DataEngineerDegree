#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:37:22 2019

@author: ferran
"""

from llibre import Llibre
from revista import Revista
from prestec import Prestec
import datetime as dt

class Biblioteca():
    
    def __init__(self):
        self._cataleg = dict()
        self._prestecs = dict()
        
    def llegeixPublicacions(self, fitxer = 'biblioteca.txt'):
        with open (fitxer, 'r') as f:
            for line in f:
                line = line.strip()
                if line == 'L':
                    l = Llibre()
                    l.codi = f.__next__().strip()
                    l.titol = f.__next__().strip()
                    l.autor = f.__next__().strip()
                    l.copies = f.__next__().strip()
                    l.dies = f.__next__().strip()
                    self._cataleg[l.codi] = l
                elif line == 'R':
                    r = Revista()
                    r.codi = f.__next__().strip()
                    r.titol = f.__next__().strip()
                    r.periodicitat = f.__next__().strip() 
                    r.exemplars = f.__next__().strip().split()
                    self._cataleg[r.codi] = r
                    
    def presta(self, DNI, codi, data, ex):
        p = Prestec()
        if codi in self._cataleg:
            if  self._cataleg[codi].tipus == 'L':
                if self._cataleg[codi].copies == 0:
                    return False,False
                else:
                    p.DNI = DNI
                    p.codi = codi
                    p.dataPrestc = data
                    d = self._cataleg[codi].dies
                    p.dataPrestc = data
                    p.dataReturn = d
                    if DNI in self._prestecs:
                        self._prestecs[DNI].append(p)
                    else:
                        self._prestecs[DNI] = [p]
                    self._cataleg[codi].copies = int(self._cataleg[codi].copies)-1
                    return True,p.dataReturn
            elif  self._cataleg[codi].tipus == 'R':
                if self._cataleg[codi].exemplars == [] or str(ex) not in self._cataleg[codi].exemplars:
                    return False,False
                p._DNI = DNI
                p.codi = codi
                p.dataPrestc = data
                p.dataReturn = 30
                self._cataleg[codi].exemplars.remove(str(ex))
                if DNI in self._prestecs:
                    self._prestecs[DNI].append(p)
                else:
                    self._prestecs[DNI] = [p]
                return True,p.dataReturn
        else:
            return False,False

    def retorna(self, DNI, codi, ex, data):       
        if DNI not in self._prestecs:
            return False,False
        else:
            for pres in self._prestecs[DNI]:
                if pres.codi==codi:
                    tmp=pres
                    self._prestecs[DNI].remove(tmp)
                    codi=True
                    continue
            if codi!=True:
                return False,False
            if data < tmp.dataReturn:
                return True,True
            else:
                return True,False            