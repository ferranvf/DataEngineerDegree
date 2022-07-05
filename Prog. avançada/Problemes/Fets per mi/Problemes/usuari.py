

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:30:27 2019

@author: ferran
"""

class Usuari():
    def __init__(self,codi=" ",nom=" ",edat=150):
        self._codi=codi
        self._nom=nom
        self._edat=int(edat)
        assert self._edat>=18,"No pots ser soci del club si ets menor d'edat."
    @property
    def codi(self):
        return(self._codi)
    @codi.setter
    def codi(self,valor):
        self._codi=valor
    @property
    def nom(self):
        return(self._nom)
    @nom.setter
    def nom(self,valor):
        self._nom=valor
    @property
    def edat(self):
        return (self._edat)
    @edat.setter
    def edat(self,valor):
        assert valor >=18, "No ets major d'edat"
        self._edat=valor
    def __str__(self):
        return("Codi: "+str(self._codi)+"\nNom: "+str(self._nom)+"\nEdat: "+str(self._edat))
        
class Activitat():
    def __init__(self,nom=' ',maxParticipants=0,edatMinima=18,edatMaxima=1000,dia=' ',hora=' '):
        self._nom=nom
        self._hora=hora
        assert (edatMinima>=18)
        self._edatMinima=edatMinima
        self._edatMaxima=edatMaxima
        self._dia=dia
        assert (maxParticipants<=40)
        self._maxParticipants=maxParticipants
        self._participants=[]
    @property
    def nom(self):
        return(self._nom)
    @nom.setter
    def nom(self,nom):
        self._nom=nom
    @property
    def hora(self):
        return(self._hora)
    @hora.setter
    def hora(self,hora):
        self._hora=hora
    @property
    def dia(self):
        return(self._dia)
    @dia.setter
    def dia(self,dia):
        self._dia=dia
    @property
    def edatMaxima(self):
        return(self._edatMaxima)
    @edatMaxima.setter
    def edatMaxima(self,eMa):
        self._edatMaxima=eMa
    @property
    def edatMinima(self):
        return(self._edatMinima)
    @edatMinima.setter
    def edatMinima(self,edatMinima):
        assert edatMinima>=18,"Ets massa petiti per apuntarte a aquesta activitat"
        self._edatMinima=edatMinima
    @property
    def maxParticipants(self):
        return(self._maxParticipants)
    @maxParticipants.setter
    def maxParticipants(self,maxPar):
        assert (maxPar<=40)
        self._maxParticipants=maxPar
    @property
    def participants(self):
        return(self._participants)
    @participants.setter
    def participants(self,participants):
        self._participants=participants

    def nParticipants(self):
        return(len(self._participants))
    def buscaParticipant(self,nom):
        for i in self._participants:
            if i.nom==nom:
                return(i)
        return None
    
    def afegeixParticipant(self,usr):
        assert (self._edatMinima<=usr.edat<=self._edatMaxima)
        assert (usr.nom not in [n.nom for n in self._participants])
        assert len(self._participants)<self._maxParticipants,"La activitat està plena"
        self._participants.append(usr)
        
        
        
        
        
        