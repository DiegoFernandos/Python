# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:49:09 2022

@author: DTIC
"""

try:
    x=int(input("ingrese un numero"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("no se puede dividir para cero")
except ValueError:
    print("solo valores enteros")
except:
    print("ocurrio un error")
    print("fin")