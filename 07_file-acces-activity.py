# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:54:24 2022

@author: lio
"""
import os
bucle = True


def leerDatosAP():
    archivo = open("AP1.txt", "r")
    for x in archivo:
        x = x.strip()
        print("-> ", x)
    archivo.close()


def aniadirDatosAP(palabra):
    archivo = open("AP1.txt", "a")
    archivo.write(palabra + "\n")
    archivo.close()


while bucle:
    os.system('cls')
    print('''
          **Sistema de manejo de Archivos Planos**
          
                 ***************************
                 *   1.- Leer el Archivo   *
                 *   2.- Añadir datos      *
                 *   3.- Salir             *
                 ***************************
          ''')
    op = input("Ingrese la opcion [1-3]: ")

    if op == '1':
        print()
        leerDatosAP()
    elif op == '2':
        op2 = True
        while op2:
            newItem = input("Ingrese un dato: ")
            aniadirDatosAP(newItem)
            p = (input("Dese seguir ingresando datos [S/N]: ")).upper()
            while p != 'S' and p!='N':
                p = (input("Dese seguir ingresando datos [S/N]: ")).upper()
            if p == 'N':
                print("ALL DONE!")
                op2 = False
    elif op == '3':
        bucle = False
    else:
        print("opcion no valida..")

print("FIN..")