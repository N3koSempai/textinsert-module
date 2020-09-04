# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:09:39 2020

@author: n3ko
"""

#problemas e el codigo borran al a;adir nuevo codigo.
#lee por cantidad de caracteres en lugar de lineas

from io import open

archivo=open("E:/Proyecto_codep/prueba.txt", "r+")


archivo.seek(0)

d=int(input("introduce a partir de que caracter quieres cortar: "))

f=(archivo.read(d))
file=open("E:/Proyecto_codep/prueba2.txt", "w")

file.write(f)

a=input("que deseas a;adir en medio: ")

file.write(a)

file.close() 

file=open("E:/Proyecto_codep/prueba2.txt", "a")

archivo.seek(d+1)

f=archivo.readline()

file.write(f)  

file.close()  
   
archivo.close()        
