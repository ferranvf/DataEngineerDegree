#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:36:44 2019

@author: ferran
"""
import abc

class Propietat():
    
    def __init__(self, codi = ' ', superficie = 0.0, nHabitacions = 0, nBanys = 0, reserves = ' '):
        self._codi = codi
        self._superficie = superficie
        self._nHabitacions = nHabitacions
        self._nBanys = nBanys
        self._contracte = Contracte
        self._visites = list()
        self._reserves = reserves
        self._firma = ' '
        self._tipus = ' '
        
    @property    
    def visites(self):
        assert self._visites != [], "Aquesta propietat no té visites"
        return(self._visites)
        
    def afegeixVisita(self,DNI):
        self._visites.append(DNI)
    
    def reserva(self,DNI):
        assert self._reserves == ' ', "Aquesta propietat ja està reservada"
        self._reserves = DNI
        
    def anulareserva(self):
        if self._codi.reserva != ' ':
           self._codi.reserva = ' '
        
    def contracta(self, nom):
        nom = int(input("1. Lloguer \n2. Venda \nIntrodueix el tipus de contracte: "))
        assert nom == 'lloguer' or nom == 'Lloguer' or nom == 'venda'\
        or nom == 'Venda' or nom == 1 or nom == 2,\
        "Opció no permesa"
        if nom == 'lloguer' or nom == 'Lloguer' or nom == 1:
            self._contracte = Lloguer()
            self._tipus = 'Lloguer'
        else:
            self._contracte = Venda()
            self._tipus = 'Venda'
        self._contracte.llegeix()    

    def firma(self, firma):
        self._firma = firma
        
    def llegeix(self):
        self._codi = input("Introdueix el codi: ")
        self._superficie = float(input("Superficie: "))
        self._nHabitacions = int(input("Nombre d'habitacions: "))
        self._nBanys = int(input("Nombre de banys: "))
        
    def mostra(self):
        m = "Codi: " + str(self._codi) + "\nSuperficie: " + str(self._superficie) \
        + "\nNombre d'habitacions: " + str(self._nHabitacions) \
        + "\nNombre de banys: " + str(self._nBanys) +"\nVisites: " + str(self._visites) \
        + "\nReserva: " + str(self._reserves)
        return(m)
        
        
class Casa(Propietat):
    
    def __init__(self, codi = ' ', superficie = 0.0, nHabitacions = 0,\
                 nBanys = 0, superficieJardi = 0.0, teGaratge = False):
        super().__init__()
        self._superficieJardi = superficieJardi
        self._teGaratge = teGaratge
        
    def llegeix(self):
        super().llegeix()
        self._superficieJardi = float(input("Superficie del Jardi: "))
        g = input("La casa té garatge? (S/N): ")
        ga = False
        if g == 's' or g == 'S': 
            ga=True
        else:
            ga=False
        self._teGaratge = ga
            
    def mostra(self):
        m = super().mostra()
        m += "\nSuperficie jardi: " + str(self._superficieJardi) + "\nGaratge: " + str(self._teGaratge)
        try:
            m += "\nCaracterístiques contracte: " + str(self._tipus) \
            + "\n" + str(self._contracte.mostra())
            return(m)
        except:
            return(m)
        
        
class Pis(Propietat):
    
    def __init__(self, codi = ' ',superficie = 0.0, nHabitacions = 0, nBanys = 0,terrassa = False,ascensor = False):
        super().__init__()
        self._terrassa = terrassa
        self._ascenor = ascensor
    
    def llegeix(self):
        super().llegeix()
        t = input("El pis te terrassa? (S/N): ")
        te = False
        if t == 's' or t == 'S':
            te = True
        elif t == 'n' or t == 'N':
            te = False
        else:
            print("Error")
        self._terrassa = te
        a = input("El pis te ascensor? (S/N): ")
        asc = False
        if a == 's' or a == 'S':
            asc = True
        elif a == 'n' or a == 'N':
            asc = False
        else:
            print("Error")
        self._ascenor = asc
        
    def mostra(self):
        m = super().mostra()
        m += "\nTerrassa: "+str(self._terrassa)+"\nAscensor: "+str(self._ascenor) 
        try:
            m += "\nCaracterístiques contracte: " + str(self._tipus) \
            + "\n" + self._contracte.mostra() 
            return(m)
        except:
            return m
        
        
class Contracte(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def llegeix(self):
        raise NotImplementedError()
        
    @abc.abstractmethod
    def mostra(self):
        raise NotImplementedError()

        
class Lloguer(Contracte):
    
    def __init__(self, renda = 0.0, despeses = 0.0):
        self._renda = renda
        self._despeses = despeses
   
    @property   
    def visites(self):
        return(self._visites)
         
    def llegeix(self):
        self._renda = float(input("Quina es la renda del lloguer: "))
        self._despeses = float(input("Quines són les despeses del lloguer: "))
        
    def mostra(self):
        return ("\nLa renda del lloguer es: " + str(self._renda) + "€/mes \nLes despeses són: " + str(self._despeses))
   
     
class Venda(Contracte):
    
    def __init__(self, preu = 0.0, impost = 0.0):
        self._preu = preu
        self._impost = impost
    
    @property   
    def visites(self):
        return(self._visites)
        
    def llegeix(self):
        self._preu = float(input("Quin és el preu de venda?: "))
        self._impost = float(input("Quin és l'import de comprar el pis/casa?: "))
        
    def mostra(self):
        return("La propietat comprada val: " + str(self._preu) + "€ amb un import de: " + str(self._impost) +"€")

class Client():
    
    def __init__(self, nom = ' ', telefon = ' ', email = ' ', DNI = ' ' ):
        self._nom = nom
        self._telefon = telefon
        self._email = email
        self._DNI = DNI
        
    def llegir(self):
        self._nom = input("Introdueix el seu nom: ")
        self._telefon = input("Introdueix el seu número de teléfon: ")
        self._email = input("Introdueix el seu email: ")
        self._DNI = input("Introdueix el seu DNI: ")
    
    def mostra(self):
        print("El client: {0} amb número de teléfon: {1}, email: {2} i DNI: {3}". format(self._nom, self._telefon, self._email, self._DNI))
    
class Immobiliaria():
    
    def __init__(self, propietat = dict(), clients = dict()):
        self._propietat = propietat
        self._clients = clients
    
    def afegirPropietat(self):
        p = int(input("1. Casa \n2. Pis\nIntrodueix el tipus de propietat: "))
        assert p == 1 or p == 2, "Opció no correcta"
        if p == 1 or p == 'casa' or p == 'Casa':
            c  = Casa()
            c.llegeix()
        else:
            c = Pis()
            c.llegeix()
        self._propietat[c._codi] = c
               
    def afegirClient(self):
        c = Client()
        c.llegir()
        assert c._DNI not in self._clients, "\nJa existeix aquest client"
        self._clients[c._DNI] = c
        
    def afegeixVisita(self, codi, DNI):
        if DNI not in self._propietat[codi].visites:
            print("No ets client.")
            n = input("Vols fer-te client? (S/N): ")
            if n == 's' or n == 'S':    
                self.afegirClient()
                self._propietat[codi].afegeixVisita(DNI)               
        else:
            self._propietat[codi].afegeixVisita(DNI)
            
    def fesReserva(self, codi, DNI):
        if DNI not in self._clients:
            print("No ets client.")
            n = input("Vols fer-te client? (S/N): ")
            if n == 's' or n == 'S':    
                self.afegirClient()
                self._propietat[codi].reserva(DNI)
        else:
            self._propietat[codi].reserva(DNI)
       
    def anulaReserva(self, codi):
       self._propietat[codi].anulareserva 
      
    def fesContracte(self,codi,DNI):
        if DNI not in self._clients:
            print("No ets client.")
            n = input("Vols fer-te client? (S/N): ")
            if n == 's' or n == 'S':
                self.afegirClient()
        assert self._propietat[codi]._firma == ' ', "Aquesta propietat ja ha estat contractada"
        self._propietat[codi].contracta(DNI)
            
    def mostraPropietats(self):
        for codi in self._propietat:
            print (str(self._propietat[codi].mostra()) + "\n")
        
    def mostraVisitesPro(self, codi): 
        assert self._propietat[codi]._visites != [], "\nAquesta propietat no té visites\n"
        print(self._propietat[codi]._visites)
       
       
    def mostraVisitesClient (self, DNI):
        v = True
        for cod in self._propietat:
            if DNI in self._propietat[cod]._visites:
                print(self._propietat[cod].mostra() + "\n")
                v = False
        if v:
            print("\nAquesta persona no ha fet visites\n")
                
            

        
    