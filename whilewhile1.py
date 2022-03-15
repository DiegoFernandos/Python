# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:26:33 2022

@author: DTIC
"""

while True:
    x=input("ingrese el numero a contar: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break