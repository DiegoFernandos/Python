# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:38:09 2022

@author: DTIC
"""
def bisiesto(ano):

    if ano % 4 == 0  and  (ano % 100 == 0  or  ano % 400 == 0):
        # ingresamos las condiciones para saber si un año
        # es o no bisiesto al año ingresado le dividimos para 4
        # si es divisible pasa a la segunda condicion, 
        #le dividimos para 100 si es divisible pasa a la 
        #siguiente condicion si es divisible para 400 
        # es bisisesto caso contrario no.
        
        return 'El año %d es bisiesto.' % ano
        # retornamos el año con la respuesta visiesto o no

    else:

        return 'El año %d no es bisiesto.' % ano

try:

    ano = int(input('Ingrese el Año a verificar: '))

    print (bisiesto(ano))

except:

    print ('El valor es erroneo')