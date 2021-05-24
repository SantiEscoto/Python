# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:00:22 2020

@author: Lenovo
"""
class PLAYER:
    def __init__(self,Nombre,Ataque,Defensa,Vida):
        self.Nombre=Nombre
        self.Ataque=Ataque
        self.Defensa=Defensa
        self.Vida=Vida
    
options=[0,1,2,3]
personajes=[]

while True:
    contador=0
    archivo = open("personajes.txt","w")
    print("ID|NOMBRE|ATAQUE|DEFENSA|VIDA")
    while contador != len(personajes):
        print("(",contador,")", personajes[contador].Nombre,personajes[contador].Ataque,personajes[contador].Defensa,personajes[contador].Vida)
                
        contador += 1
    print("Gestor de Personajes")
    print("( 0 ) Crear")
    print("( 1 ) Editar")
    print("( 2 ) Borrar")
    print("( 3 ) Salir")
    while True:#Escoje tú opción
        try:
            opción=int(input("-> "))
            while opción not in options:
                print("¿Buscas encontrar más opciones?, lo siento amigo, no hay presupuesto para eso")
                opción=int(input("-> "))
            break
        except ValueError:
            print("Por favor escribe el número entre parentesis de la opción que quieras hacer")
    if opción==3:#Cerrar
        archivo.close()
        break
    elif opción==0:#Crear
        NAME=input("¿Cuál será su nombre? ")
        while True:#Ataque
            try:
                ATACK=int(input("¿De cuanto será su ataque? "))
                break
            except:
                print("por favor pon un valor entero")
        while True:#Defensa
            try:
                DEFENSE=input("¿De cuanto será su defensa? ")
                break
            except:
                print("por favor pon un valor entero")
        while True:#Vida
            try:
                HEALTH=input("¿Cuanta vida tendrá? ")
                break
            except:
                print("por favor pon un valor entero")
        personajes.append(PLAYER(NAME,ATACK,DEFENSE,HEALTH))
    elif opción==1:#Editar
        print("¿Qué personaje quieres editar?")
        ID=int(input("-> "))
        personajes.remove(personajes[ID])
        NAME=input("¿Cuál será su nuevo nombre? ")
        while True:#Ataque
            try:
                ATACK=int(input("¿De cuanto será su ataque? "))
                break
            except:
                print("por favor pon un valor entero")
        while True:#Defensa
            try:
                DEFENSE=input("¿De cuanto será su defensa? ")
                break
            except:
                print("por favor pon un valor entero")
        while True:#Vida
            try:
                HEALTH=input("¿Cuanta vida tendrá? ")
                break
            except:
                print("por favor pon un valor entero")     
        personajes.append(PLAYER(NAME,ATACK,DEFENSE,HEALTH))
    elif opción==2:#Eliminar
        print("¿Qué personaje quieres eliminar?")
        ID=int(input("-> "))
        personajes.remove(personajes[ID])
