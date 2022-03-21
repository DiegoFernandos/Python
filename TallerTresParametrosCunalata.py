# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:01:32 2022

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

def diasDelAño(año,mes,dia):  
    #numerodeDiasdelAño = [365,366]
    #x=bisiesto(año)
   # if dia in numerodeDiasdelAño:
     #   if x:
       #     return 366
       # else:
        #    return 365
    #else:
      #  return None
      diasAños=[365,366]
      diasBisiesto=[366]
      x=bisiesto(año)
      if dia in diasAños:
          if dia==365:
              if x:
                  return 365
          elif dia in diasBisiesto:
              return 366
          
añosAComprobar = [2020,2022]
mesesAComprobar = [5,2]
diasAComprobar =[366,365]
resultadoTest = [31,28]
  
for i in range(len(añosAComprobar)):
    año = añosAComprobar[i]
    mes = mesesAComprobar[i]
    dia = diasAComprobar[i]
    dias = mesesDelAño(año,mes)
    totalDias= diasDelAño(año,mes,dia)
    
    if dias == resultadoTest[i]:
        print({'AÑO': año,'El NUMERO DEL MES ES': mes,'NUMEROS DE DIAS': dias,'El numero de dias del Año es':dia})
    else:
        print('EL PROCESO ES INCORRECTO.')
     
 