#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:36:29 2019

@author: ferran
"""

class NumeroComplex():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def llegir(self):
        self.a=float(input("Introdueix un nombre: "))
        self.b=float(input("Introdueix un nombre: "))        
    def __add__(self,suma):
        return NumeroComplex(self.a+suma.a,self.b+suma.b)
    def __sub__(self,resta):
        return NumeroComplex(self.a-resta.a,self.b-resta.b)
    def conjugar(self):
        return NumeroComplex(self.a,-self.b)
    def __mul__(self,mul):
        a=self.a*mul.a-self.b*mul.b
        b=self.a*mul.b+self.b*mul.a
        return NumeroComplex(a,b)
    def __str__(self):
        if self.b>=0:
            return str(self.a)+'+'+str(self.b)+'i'
        else:
            return str(self.a)+str(self.b)+'i'


