# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:29:09 2020
CALCULADORA
@author: Santiago Escoto
"""
print ("Bienvenido")
while True:
    print("Dame dos números que quieras realizar alguna operación")
    try:
        x=input("Primer número ")
        y=input("Segundo número ")
        a= float(x)
        b= float(y)
    except:
        print("Por favor escribe un caracter que sea un número")
        
    print("¿Que quieres hacer con estos dos numeros? ")
    print("sumarlos escribe 1, restarlos escribe 2, dividirlos escribe 3 y multiplicarlos escribe 4")
    z=float(input("Operación "))

    resultado = 9
    if z==1:
        resultado=a+b
    elif z==2:
            resultado=a-b
    elif z==3:
        while b==0:
            print("No puedo hacer divisiones entre 0, por favor cambia tu segundo valor")
            y=input("Segundo número ")
            b= float(y)
        resultado=a/b
    elif z==4:
        resultado=a*b
          
    print ("tu resultado es")
    print (resultado)
    print ("¿deseas hacer otra operación?")
    R=input("1 para sí o 0 para no: ")
    r=float(R)
    if r==0:
        print("Hasta pronto!")
        break