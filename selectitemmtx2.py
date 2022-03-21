# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:56:51 2019

@author: UPS
"""

# Extraer los valores de todas las filas ubicados en la columna 3 
import numpy as np
a=np.array([(1,2,3,4),
            (3,4,5,6)])
print(a[0:1])
print(a[0:,2])

