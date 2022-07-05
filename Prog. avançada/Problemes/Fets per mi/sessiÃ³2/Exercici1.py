#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:39:19 2019

@author: ferran
"""
import numpy as np

def vàlidSudoku(sudoku, numero, fila, columna):
    sudoku = np.loadtxt(sudoku, dtype = 'int')
    assert numero>0 and numero<=9
    assert fila>0 and fila<=9
    assert columna>0 and fila<=9
    filaIniciQuadrat=(fila//3)*3
    columnaIniciQuadrat=(columna//3)*3
    valid=numero not in sudoku [fila,:] and numero not in sudoku[:,columna] and numero not in sudoku[filaIniciQuadrat:filaIniciQuadrat+3,columnaIniciQuadrat:columnaIniciQuadrat+3]        
    
        
        
sudoku=input("Introudeix nom fitxer: ")
numero=int(input("Introdueix un número: "))
fila=int(input("Introdueix una fila: "))
columna=int(input("Introdueix una columna: "))
a=vàlidSudoku(arxiu,numero,fila,columna)
print(a) 