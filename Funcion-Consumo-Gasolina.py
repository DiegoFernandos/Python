# -*- coding: utf-8 -*-
"""
@author: lio
"""
#variables globales
milla = 1609.344#metros
galon = 3.785411784#litros

km = milla / 1000

#formulas aplicar 
#MPG = (100 * GALON)/KM * L100KM
#L100KM = (100 * GALON)/KM * MPG

#ejercicios conversion
def l100kmtompg (litros):
    mpg = (100 * galon)/(km * litros)
    return f"El valor en millas por galon es: {mpg} mpg"
    
def mpgtol100km (millas):
    l100km = (100 * galon)/(km * millas)
    return f"El valor en litros/100km: {l100km} l100km"
    
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
