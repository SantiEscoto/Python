# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:02:13 2020

@author: Lenovo
"""
#Manejar archivos

archivo = open("archivo_de_prueba.txt","w") #Abrimos el archivo en modalidad escritura "write"
print("Archivo abierto")
archivo.write("Hola\n"+"Mundo")
archivo.write("Hola")#Escribe todo en una línea
archivo.writelines(["hola","mundo"])#Escribe por líneas
archivo.close()

#'' es lo mismo que ""

archivo = open("archivo_de_prueba.txt","r") #Abrimos el archivo en modalidad escritura "read"
print(archivo.read())
archivo.close()


# lectura[0]=lectura[0].split("L")
# print(lectura)
# # lectura=lectura[0][0].replace("o","a")
# # print(lectura)
# lectura[0][0]=lectura[0][0].replace("a","e")
# print(lectura)