# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:23:36 2022

@author: DTIC
"""
switch=[]
lista=["r1","r2","r3","r4","s5","s6"
       ,"t7","t8","t9"]
for item in lista:
    if "s" in item:
        switch.append(item)
        
print(switch)