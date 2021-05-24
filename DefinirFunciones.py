# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:30:23 2020

@author: Santiago Escoto
"""
n=str(input("¿Cómo te llamas? "))
z=float(input("Dame un número para redondear "))
def saludo(nombre):
    print ("Hola",nombre,"que tengas un buen día")
saludo(n)    
    
def redondeo(valor):
    valor_entero=int(valor)
    criterio_redondeo = valor-valor_entero
    if criterio_redondeo == 0:
        return valor
    elif criterio_redondeo <=0.5:
        return valor_entero
    else:
        return valor_entero+1
redondeado=redondeo(z)
print(redondeado)