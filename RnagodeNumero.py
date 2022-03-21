# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:52:18 2022

@author: DTIC
"""

def readint (prompt, min, max):
     try:
         prompt=int(input()) #para ingresar un muero entero
         if prompt < min or prompt > max:# permite verificar
         #el numero ingresado si es mayor o menor del rango
             print("el valor no esta dentro del rango permitido->" + str(min) + 'hasta-->' + str (max))
             return readint (print ("el numero ingresado debe ser de -10 a 10", end=''),-10,10)
         
     except ValueError:
         print("Error: entrada incorrecta")
         return readint(print("Ingresa un numero de -10 a 10: " , end=''), -10, 10) 
         
     else:
         return prompt


v = readint(print("Ingresa un numero de -10 a 10: " , end=''), -10, 10)

print("El numero es:", v)