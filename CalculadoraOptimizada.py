# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:00:27 2020

@author: Santiago Escoto
"""
print ("Bienvenido")
while True:
    print("¿Qué operación quieres realizar?")
    print("sumar escribe 1, restar escribe 2, multiplicar escribe 3 y dividir escribe 4")
    
    while True:
        try:
            z=float(input("Operación: "))
            break
        except ValueError:
            print("Por favor escribe un caracter que sea un número")
        
    print("Dame dos números que quieras realizar alguna operación")
    while True:
        try:
            x=float(input("Primer número "))
            break
        except ValueError:
            print("Por favor escribe un caracter que sea un número")
    while True:
        try:
            y=float(input("Segundo número "))
            break
        except ValueError:
            print("Por favor escribe un caracter que sea un número")
            
    resultado = 0
    if z==1:
        resultado=x+y
    elif z==2:
        resultado=x-y
    elif z==3:
        resultado=x*y
    elif z==4:
        while y==0:
            print("No puedo hacer divisiones entre 0, por favor cambia tu segundo valor")
            y=float(input("Segundo número "))
        resultado=x/y
    
    print ("Tu resultado es")
    print (resultado)
    print ("¿deseas hacer otra operación?")
    while True:
        try:
            r=float(input("1 para sí o 0 para no: "))
            break
        except ValueError:
            print("Por favor escribe un caracter que sea un número")
    if r==0:
        print("Hasta pronto!")
        break