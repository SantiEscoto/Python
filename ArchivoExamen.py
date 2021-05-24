# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:11:56 2020

@author: Lenovo
"""

#Funciones
def contarLetra(string,caracter):
    contador = 0
    for elemento in string:
        if elemento == caracter:
            contador = contador + 1
    return contador

def posición(string,caracter):
    posición = 1
    posiciones = []
    for elemento in string:
        if elemento == caracter:
            posiciones.append(posición)
        posición += 1
    return posiciones

#Presentación
print("Este programa puede contar cuantas veces se repite un caracter en un texto")
print("¿Qué deseas hacer? \n1-Buscar y contar un caracter\n2-Salir")
elección=0
opciones=[1,2]

while True:#Opción
    try:
        elección=int(input("Elige la opción escribiendo el número al inicio de esta: "))
        while elección not in opciones:
            print("Por ahora este programa solo puede realizar dos acciónes, por favor vuelve a escoger")
            elección=int(input("-> "))
        break
    except ValueError:
        print("Por favor elige la opción escribiendo el número al inicio de esta: ")

while True:
    if elección==2:
        print("¡Hasta pronto!")
        break
    else:
        #Entrada
        archivo = open("ArchivoExamen.txt","r")
        texto=str(archivo.read())
        caracter=str(input("¿Cuál es el caracter que quieres contar? "))
        #Procesamiento
        contador = contarLetra(texto,caracter)
        posiciones = posición(texto,caracter)
        #Salida
        
        if len(caracter) != 1:
            print("Debes de ingresar un solo caracter")
        elif contador==0:
            print("El caracter",caracter," no aparece en ninguna posición")
        elif contador==1:
            print("El caracter",caracter,"aparece",contador,"vez en la posicion",posiciones)
        else:
            print("El caracter",caracter,"aparece",contador,"veces en las posiciones",posiciones)
            
        print("Deseas buscar y contar otro número\n1-Si\n2-No, quiero salir")
        while True:#Opción
            try:
                elección=int(input("Elige la opción escribiendo el número al inicio de esta: "))
                while elección not in opciones:
                    print("Por ahora este programa solo puede realizar dos acciónes, por favor vuelve a escoger")
                    elección=int(input("-> "))
                break
            except ValueError:
                print("Por favor elige la opción escribiendo el número al inicio de esta: ")
        if elección==2:
            print("¡Hasta pronto!")
            break
        
