# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:05:43 2019

@author: ferran
"""

class Producte:
    def __init__(self, codi = "", preu = 0.0):
        self._codi = codi
        self._preu = preu
        
    @property
    def codi(self):
        return self._codi
    @codi.setter
    def codi(self, valor):
        self._codi = valor
        
    @property
    def preu(self):
        return self._preu
    @preu.setter
    def preu(self, valor):
        self._preu = valor
    
    def llegeix(self):
        self.codi=input("Codi: ")
        self.preu=float(input("Preu: "))
        
    def __str__(self):
        resultat="Codi: "+self.codi+"\nPreu: "+str(self.preu)
        return(resultat)
        
    def despesesEnviament(self):
        if self.preu<100:
            despeses=1
        else:
            if despeses<5:
                despeses=0.01*self.preu
        return(despeses)
            
class Llibre(Producte):#al possar podructe li estic dient que producte és la superclasse
    def __init__(self, codi = "", preu = 0.0,titol = "", autor = "", nPagines = 0):
        super().__init__(codi,preu)#hem retorna la part comuna de la classe
        self._titol = titol
        self._autor = autor
        self._nPagines = nPagines
        
    def llegeix(self):
        super().llegeix()
        self.titol=input("Titol: ")
        self.autor=input("Autor: ")
        self.nPagines=int(input("N. pagines: "))
    
    def __str__(self):
        resultat=super().__str__()#per cridar el __str__ del Producte
        resultat+="\nTitol: "+self.titol+"\nAutor: "+self.autor+"\nnPagines: "+str(self.nPagines)
        return(resultat)  
        
    def despesesEnviament(self):
        despeses=super().despesesEnviament()
        if self.nPagines>500:
            despeses+=1
        return(despeses)
    
    @property
    def titol(self):
        return self._titol
    @titol.setter
    def titol(self, valor):
        self._titol = valor

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def nPagines(self):
        return self._nPagines
    @nPagines.setter
    def nPagines(self, valor):
        self._nPagines = valor
        
class Electrodomestic(Producte):
    def __init__(self, codi = "", preu = 0.0,marca = "", model = "", volum = 0.0):
        super().__init__(codi,preu)
        self._marca = marca
        self._model = model
        self._volum = volum
    def llegeix(self):
        super().llegeix()
        self.marca=input("Marca: ")
        self.model=input("Model: ")
        self.volum=float(input("Volum: "))
    def __str__(self):
        resultat=super().__str__()#per cridar el __str__ del Producte
        resultat+="\nMarca: "+self.marca+"\nModel: "+self.model+"\nVolum: "+str(self.volum)
        return(resultat)  
    def despesesEnviament(self):
        despeses=super().despesesEnviament()
        despeses+=int(self.volum/20)
        return(despeses)
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, valor):
        self._model = valor

    @property
    def volum(self):
        return self._volum
    @volum.setter
    def volum(self, valor):
        self._volum = valor



continuar = True
productes = []
while (continuar):
    tipus = input("Tipus de producte (l: llibre - e: electrodomestic - altres: sortir): ")
    if (tipus == 'l'):
        l=Llibre()
        l.llegeix()
        productes.append(l)
    elif (tipus == 'e'):
        e=Electrodomestic()
        e.llegeix()
        productes.append(e)
    else:
        continuar = False
for p in productes:
    print(p)
    print("Despeses: ",p.despesesEnviament())


        
        
        
        