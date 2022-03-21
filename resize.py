# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:50:43 2019

@author: UPS
"""
# Cambio de forma de una matriz
import numpy as np
a = np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)