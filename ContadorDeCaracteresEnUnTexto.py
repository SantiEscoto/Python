# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 08:54:02 2020

@author: Santiago Escoto
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
#Entrada
texto=str(input("¿Cuál es el texto que quieres introducir? "))
caracter=str(input("¿Cuál es la letra que quieres contar? "))
#Procesamiento
contador = contarLetra(texto,caracter)
posiciones = posición(texto,caracter)
#Salida
print ("El caracter",caracter,"aparece",contador,"veces en la posición",posiciones)