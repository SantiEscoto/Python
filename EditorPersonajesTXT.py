# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:09:25 2020

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
        a=f"( {contador} ) {personajes[contador].Nombre} {personajes[contador].Ataque} {personajes[contador].Defensa} {personajes[contador].Vida}"
        archivo.write(a)
        archivo.write("\n")
        contador += 1
    archivo.close()
    archivo = open("personajes.txt","r")
    print(archivo.read())
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
                ATTACK=int(input("¿De cuanto será su ataque? "))
                break
            except:
                print("por favor pon un valor entero")
        while True:#Defensa
            try:
                DEFENSE=int(input("¿De cuanto será su defensa? "))
                break
            except:
                print("por favor pon un valor entero")
        while True:#Vida
            try:
                HEALTH=int(input("¿Cuanta vida tendrá? "))
                break
            except:
                print("por favor pon un valor entero")
        personajes.append(PLAYER(NAME,ATTACK,DEFENSE,HEALTH))
    elif opción==1:#Editar
        try:
            print("¿Qué personaje quieres editar?")
            ID=int(input("-> "))
            personajes.remove(personajes[ID])
            NAME=input("¿Cuál será su nuevo nombre? ")
            while True:#Ataque
                try:
                    ATTACK=int(input("¿De cuanto será su ataque? "))
                    break
                except:
                    print("por favor pon un valor entero")
            while True:#Defensa
                try:
                    DEFENSE=int(input("¿De cuanto será su defensa? "))
                    break
                except:
                    print("por favor pon un valor entero")
            while True:#Vida
                try:
                    HEALTH=int(input("¿Cuanta vida tendrá? "))
                    break
                except:
                    print("por favor pon un valor entero")     
            personajes.append(PLAYER(NAME,ATTACK,DEFENSE,HEALTH))
            break
        except:
            print("Necesitas tener ese personaje para poderlo editar")
    elif opción==2:#Eliminar
        try:
            print("¿Qué personaje quieres eliminar?")
            ID=int(input("-> "))
            personajes.remove(personajes[ID])
        except:
            print("Necesitas tener ese personaje para poderlo eliminar")
