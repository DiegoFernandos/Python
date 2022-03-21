# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:53:04 2019

@author: UPS
"""
# Extraer un solo valor de la matriz - el valor ubicado en la fila 0 columna 2
import numpy as np
a=np.array([(1,2,3,4),
            (3,4,5,6)])
print (a)
print ("\n"*1)
print(a[1,2])