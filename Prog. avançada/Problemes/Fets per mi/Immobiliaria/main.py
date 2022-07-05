#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:35:29 2019

@author: ferran
"""

import ClassImmobiliaria

def main():
    imm=ClassImmobiliaria.Immobiliaria()
    opcio = ' '
    while opcio != '10':
        print("--------------Menú-------------")
        print("1. Afegir propietat\n2. Client\n3. Visita\n4. Reserva\n5. Anul·lar reserva \
              \n6. Formalització contracte\n7. Llista de les propietats \n8. Llistat de tots els clients \
              \n9. Dades de les propietats visitades per un clients\n10. Sortir")
        print("-------------------------------")
        opcio = input("Tria una opció del menú: ")       
        if opcio == '1':     
            try:
                imm.afegirPropietat()
            except AssertionError as error:
                print(error)        
        elif opcio == '2':
            try:
                imm.afegirClient()
            except AssertionError as error:
                print(error)                
        elif opcio == '3':
            codi = input("Introdueix el codi de la propietat que es vol visitar: ")
            DNI  = input("El seu DNI si us plau: ")
            try:
                imm.afegeixVisita(codi,DNI)
            except AssertionError as error:
                print(error)
        elif opcio == '4':
            codi = input("Introdueix el codi de la propietat que es vol reservar: ")
            DNI  = input("El seu DNI si us plau: ")
            try:
                imm.fesReserva(codi,DNI)
            except AssertionError as error:
                print(error)
        elif opcio == '5':
            codi = input("Introdueix el codi de la propietat que es anul·lar reserva: ")
            try:
                imm.anulaReserva(codi)
            except AssertionError as error:
                print(error)
        elif opcio == '6':
            codi = input("Introdueix el codi de la propietat que es vol contractar: ")
            DNI  = input("El seu DNI si us plau: ")
            try:
                imm.fesContracte(codi,DNI)
            except AssertionError as error:
                print(error)
        elif opcio == '7':
            imm.mostraPropietats()
        elif opcio == '8':
            codi = input("Introdueix el codi de la propietat per veure les visites que ha tingut: ")
            imm.mostraVisitesPro(codi)
        elif opcio == '9':
            DNI = input("DNI del client per veure quines propietas ha vistat: ")
            imm.mostraVisitesClient(DNI)
        elif opcio != '10':
            print("Ha triat una opció que no es correcte, trïï una altre")
    
    if opcio == '10':
        print("Ha triat la opció sortir, gràcies i fins aviat")

main()            
             
                
                
                