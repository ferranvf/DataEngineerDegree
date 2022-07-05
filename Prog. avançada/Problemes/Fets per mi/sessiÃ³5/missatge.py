#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:09:56 2019

@author: ferran
"""
import re

class Missatge():
    def __init__(self):
        self._nom=""
        self._missatge=""
        self._data=""
        
    def llegeix(self):
        self.emissor=input("Nom de l'emissor: ")
        self.text=input("Text del missatge: ")
        self.data=input("Data del missatge: ")
        
    @property
    def emissor(self):
        return(self._emissor)
    @emissor.setter
    def emissor(self,nom):
        self._emissor=nom
        
    @property
    def text(self):
        return(self._text)
    @text.setter
    def text(self,mi):
        self._text=mi
        return(self._text)
        
    @property
    def data(self):
        return(self._data)
    @data.setter
    def data(self,d):
        assert(re.match("[0-9]{2}/[0-9]{2}/[0-9]{4}",d))
        self._data=d
        
def principal():
    missatges=list()
    stop=False
    while (not stop):
        m=Missatge()
        m.llegeix()
        missatges.append(m)
        sortir=input('Vols afegir mes missatges? ')
        if sortir!='S' or 's':
            stop=True
    nom=input("Introdueix un nom: ")
    mostrarMissatgeEmissor(nom,missatges)
        
        
def mostrarMissatgeEmissor(nom,missatges):
    for m in missatges:
        if (m.emissor==nom):
            print("Text: ",m.text,"Data: ",m.data)
        
        
        