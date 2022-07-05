#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:54:47 2019

@author: ferran
"""

from classSudoku import Sudoku

def main():
    stop=False
    nomFitxer=input("Nom del fitxer: ")
    s=Sudoku(nomFitxer)
    s.mostra()
    while not stop:
        print("------------Menu------------")
        print("1.-Posar número")
        print("2.-Eliminar número")
        print("3.-Sortir")
        opció=input("Introdueix una opció: ")
        if opció=='1':
            valor=int(input("Introdueix un nombre del 0 al 9:"))
            fila=int(input("Número de fila: "))
            columna=int(input("Número de columna: "))
            try:
                s.introduirNum(valor,fila,columna)
            except AssertionError as error:
                print(error)
            s.mostra()
        elif opció=='2':
            fila=int(input("Número de la fila: "))
            columna=int(input("Número de la columna: "))
            try:
                s.eliminar(fila,columna)
            except AssertionError as error:
                print(error)
            s.mostra()
        elif opció=='3':
            stop=True
            print("Has triat sortir del joc \nFins aviat!!!!")
        else:
            print("Aquesta opció no es vàlida")
            opció=input("Introdueix una opció: ")
            s.mostra()
        if s.complete==True:
            stop=True
            
            