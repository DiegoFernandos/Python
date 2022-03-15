# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:25:07 2022

@author: DTIC
"""

acl=int (input("ingrese el numero de ACL:"))
if acl>=1 and acl<=99:
    print("la acl es estandar")
elif acl>100 and acl<=99:
    print("la acl es extendida")
else:
    print("el numero ingresado es normal")

