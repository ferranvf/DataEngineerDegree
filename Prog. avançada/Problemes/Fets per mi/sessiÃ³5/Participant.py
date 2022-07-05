# -*- coding: utf-8 -*-

class Participant:
    def __init__(self, nom = "", tlf = ""):
        self._nom = nom
        self._tlf = tlf
    
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, valor):
        self._nom = valor

    @property
    def telefon(self):
        return self._tlf
    @telefon.setter
    def telefon(self, valor):
        self._tlf = valor
    