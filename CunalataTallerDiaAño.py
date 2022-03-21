# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:41:54 2022

@author: DTIC
"""

def bisiesto(año):
    
    if año % 4 == 0 and  año % 100 !=0:
         return True
    elif año % 400 == 0:
        return True
    else:
        return False
 
def mesesDelAño(año, mes):
    
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    mesesTreinta=[4,6,9,11]
    x=bisiesto(año)
    if mes in meses:
        if mes==2:
            if x:
                return 29 
            else:
                return 28
        elif mes in mesesTreinta:
            return 30
        else:
            return 31
    else:
        return None
     
añosAComprobar = [1900, 2000, 2016, 1987]
mesesAComprobar = [ 2, 2, 1, 11]
resultadoTest = [28, 29, 31, 30]
 
for i in range(len(añosAComprobar)):
    año = añosAComprobar[i]
    mes = mesesAComprobar[i]
    dias = mesesDelAño(año,mes)
    if dias == resultadoTest[i]:
        print({'AÑO': año,'El NUMERO DEL MES ES': mes,'NUMEROS DE DIAS': dias})
    else:
        print('EL PROCESO ES INCORRECTO.')