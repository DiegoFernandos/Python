# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:32:01 2022

@author: DTIC
"""
space= " "
nombre=input("Ingrese su Nombre: ")
print(nombre)
apellido=input("Ingrese su Apellido: ")
print(apellido)
cedula=input("Ingrese su Numero de Cedula: ")
print(cedula)
direccion=input("Ingrese su direccion: ")
print(direccion)
acl=int (input("Ingrese su edad:"))
if acl>=1 and acl<=10:
    print("niño")
elif acl>=10 and acl<=17:
    print("adolecnete")
elif acl>=18 and acl<=50:
    print("mayor de edad")
else:
    print("tercera edad")
    
print("Almacenes DC le da La Vienvenida SR:"+nombre+space+apellido+space+cedula+space+direccion+space+str(acl))