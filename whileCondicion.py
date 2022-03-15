# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:19:57 2022

@author: DTIC
"""

numero=input("ingrese el numero a contar: ")
numero=int(numero)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>numero:
        break