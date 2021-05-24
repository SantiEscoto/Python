"""
Created on Sat Jun 20 19:37:07 2020

@author: Santiago Escoto
"""
#Función
def buscar_repetidos(lista,valor):
    posición=[]
    indice=0

    for elemento in lista:
        if elemento == valor:
            posición.append(indice)
        indice +=1
    return posición

#Presentación
print("Este programa encuentra todos los valores repetidos dentro de una lista y te dicen en que posición están")
print("Primero hay que hacer una lista para eso dime")

#Entrada
while True:
    try:
        elementos=int(input("¿Cuántos elementos tiene esta lista? "))
        break
    except ValueError:
        print("Por favor escribe la cantidad de elementos con caracteres numéricos y enteros")

print("Dime los elementos de esta lista. Pueden ser de cualquier tipo")
lista=[]
contador=0
while contador != elementos:
    valor=input("-> ")
    lista.append(valor)
    contador += 1
#Apartir de aquí ya insertamos una lista con n elementos y nombramos a acada elemento

#Ahora hay que ver si hay valores repetidos
unicos = []
k=0
while k != elementos:
    elemento=lista[k]
    posición=buscar_repetidos(lista,elemento)
    if elemento not in unicos:
        if len(posición)==1:
            print (elemento,"se repite",len(posición),"vez en la posición",posición)
        else:
            print (elemento,"se repite",len(posición),"veces en las posiciones",posición)
        unicos.append(elemento)
    k += 1