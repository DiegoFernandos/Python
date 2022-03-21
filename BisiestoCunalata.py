# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:13:53 2022

@author: DTIC
"""


def bisiesto(año):
    
    # ingresamos las condiciones para saber si un año es bisiesto o no
   
    if año % 4 == 0 and  año % 100 !=0:
        
        return True
    
    elif año % 400 == 0:
        
        return True
    
    else:
        
        return False
    
    
añosAComprobar = [1989, 2000, 2016, 1987] #Ingreso de años Verificar

resultadoTest = [False, True, True, False] #resultados eserados del test

for i in range(len(añosAComprobar)):#Bucle comarpativo de los años ingreados

    año = añosAComprobar[i]

    resultado = bisiesto(año)

    if resultado == resultadoTest[i]:#condicion comparativa del test

        if resultado == True: # si el resultado es verdadero imprime año bisisesto

            print(f'{año} Es un año Bisiesto')

        elif resultado == False: # si es falso no es bisiesto

            print(f'{año} No es un año Bisiesto')
    else:
        print('El año ingresado no es correcto!!!')
        #caso contrario el numero ingresado no es el mismo del TEST.