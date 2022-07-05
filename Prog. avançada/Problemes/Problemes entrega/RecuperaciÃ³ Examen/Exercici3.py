#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:31:31 2019

@author: ferran
"""

d={'mama':'Bet','germa':'Roger','papa':'Victor','jo':'Ferran'}
def d_inv(d):    
    d_inv=dict()
    for a,b in d.items():
        d_inv[b]=a
    print(d_inv)