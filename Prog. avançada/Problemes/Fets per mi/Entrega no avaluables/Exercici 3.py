#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:27:59 2019

@author: ferran
"""

class Assignatura():
    def __init__(self):
        self._nom = ' '
        self._creditsEstudiant = 0
        self._creditsProfessor = 0
           
    def llegir(self):
        self._nom = input("Nom de l'assignatura: ")
        self._creditsEstudiant = int(input("Crèdits del estudiant: "))
        self._creditsProfessor = int(input("Crèdits professor: "))
    @property
    def nom(self):
        return(self._nom)
    
    @property
    def creditsEstudiant(self):
        return(self._creditsEstudiant)
    
    @property
    def creditsProfessor(self):
        return(self._creditsProfessor)

        
class Persona():
    def __init__(self):
        self._niu = ' '
        self._Nom = ' '
        self._llistat = list()

   
    @property
    def Nom(self):
        return(self._Nom)
       
    @property
    def niu(self):
        self._niu

    
    def cercaAssignatura(self, n):
        if n.Nom in [x.Nom for x in self._llistat]:
            return (True)
        else:
            return (False)
        
    def afegeixAssignatura(self, a):
        if a.Nom in [x.Nom for x in self._llistat]:
            return False
        else:
            self._llistat.append(a.Nom)
            return True


class Estudiant(Persona):
    
    def __init__(self):
        super().__init__()
        self._titulacio = ' '
        
    @property
    def titulacio(self):
        return (self._titulacio)
    
    def creditsMatriculats(self):
        return (sum([x.creditsEstudiant for x in self._creditsEstudiant]))

class Professor(Persona):
    
    def __init__(self):
        super().__init__()
        self._departament = ' '
        self._maximCredits = 0
    
    @property
    def departament(self):
        return self._departament
    
    @property
    def maxC(self):
        return self._maximCredits 
    
    def creditsImpartits(self):
        return(sum([x.creditsProfessor for x in self._creditsProfessor]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        