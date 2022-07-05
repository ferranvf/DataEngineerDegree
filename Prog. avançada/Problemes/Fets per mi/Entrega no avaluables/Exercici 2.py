#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:21:06 2019

@author: ferran
"""

class Assignatura():
    
    def __init__(self, nom = ' ', creditsEstuiant = 0, creditsProfessor = 0):
        self._nom = nom
        self._creditsEstudiant = creditsEstuiant  
        self._creditsProfessor = creditsProfessor
    
    def llegeix(self):
        self._nom = input("Introdueix el nom de l'assignatura: ")
        self._creditsEstudiant = input("Nombre de crèdits del estudiant: ")
        self._creditsProfessor = input("Nombre de crèdits del professor: ")

    def mostra(self):
        return("Nom: " + str(self._nom) +"\nCrèdits alumne: " + str(self._creditsEstudiant) + \
               "\nCrèdits professor: " + str(self._creditsProfessor))
        
        
class Persona():
    def __init__(self, nom = ' ', niu = 0, llistataAssignatura = list()):
        self._nom = nom
        self._niu = niu
        self._llistat = llistataAssignatura
    
    @property
    def nom(self):
        return(self._nom)
        
    @nom.setter
    def nom(self,name):
        self._nom = name
        
    @property
    def niu(self):
        return(self._niu)
    
    @niu.setter
    def niu(self,valor):
        self._niu = valor 
        
    def cercaAssignatura(self,materia = ' '):
        a = input("Nom de l'assignatura: ")
        materia = a
        if materia in self._llistat:
            return (True)
        else:
            return(False)
            
    def afegeixAssignatura(self):
        a = Assignatura()
        a.llegeix()
        if a.llegeix().nom in self._llistat:
            return(True)
                
    
        
        
        
        