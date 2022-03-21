# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:29:17 2022

@author: DTIC
"""

def fibonaci(n):
    a,b= 0,1
    while a<=n:
        print(a, end= ' ')
        """ c= a+b
        a=b
        b=c  este codigo hace lo mismo que la linea codigo de abajo"""
        a, b = b, a+b
"""fibonaci(8) ingresa el numero a realizar el fibonaci"""
        