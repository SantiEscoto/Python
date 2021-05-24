# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:22:39 2020

@author: Lenovo
"""
#Listas

x=[0,7,2,4]
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])

x.append(3) #Añadir un valor al conjunto de elementos
print(x)
print(x[4])

x.remove(3) #Quitar el valor que contenga ese número

nombres =["Miguel", "Joaquín", "Roberto", "Santiago"]
print (nombres)

#arreglos todos del mismo tipo
lista=[0,"pyton",0.76,x,nombres]
print(lista)
print(lista[4][0])
print(lista[4],lista[0],lista[4][2])
lista.insert(2,3)#Recorre e inserta en la posición 2 un 3
print (lista)

print(lista.index(x))#imprime el lugar donde se encuentra el valor

y = [i for i in range(10)]
print (y)

lista.pop()#quita el ultimo elemento de una lista
print(lista)

lista.clear()
print(lista)

for j in x:#x es una lista recorre
    print (j)
    
len(x)
