#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:17:07 2019

@author: ferran
"""

with open ('biblioteca.txt','r') as f:
    Llibre = dict()
    Revista = dict()
    for line in f:
        line = line.strip()
        if line == 'L':
            codi = f.__next__().strip()
            titol = f.__next__().strip()
            autor = f.__next__().strip()
            copies = f.__next__().strip()
            dies = f.__next__().strip()
            Llibre[codi] = titol, autor, copies, dies
        elif line == 'R':
            codi = f.__next__().strip()
            titol = f.__next__().strip()
            periodicitat = f.__next__().strip() 
            exemplar = f.__next__().strip().split()
            Revista[codi] = titol, periodicitat, exemplar
            
    print(Revista)