# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:29:22 2020

@author: Lenovo
"""
class PLAYER:
    def __init__(self,Name,Attack,Defense,Health):
        self.Name=Name
        self.Attack=Attack
        self.Defense=Defense
        self.Health=Health

options=[0,1,2,3]
characters=[]

while True:
    counter=0
    archive = open("players.txt","w")
    print("ID|NAME|ATTACK|DEFENSE|HEALTH")
    while counter != len(characters):
        a=f"( {counter} ) {characters[counter].Name} {characters[counter].Attack} {characters[counter].Defense} {characters[counter].Health}"
        archive.write(a)
        archive.write("\n")
        counter += 1
    archive.close()
    archive = open("players.txt","r")
    print(archive.read())
    print("Character Manager")
    print("( 0 ) Create")
    print("( 1 ) Edit")
    print("( 2 ) Delete")
    print("( 3 ) Exit")
    while True:#Choose the option
        try:
            option=int(input("-> "))
            while option not in options:
                print("Are you looking to find more options? Sorry, friend, there is no budget for that")
                option=int(input("-> "))
            break
        except ValueError:
            print("Please write the number in parentheses of the option you want to do")
        
    if option==3:#Exit
        archive.close()
        break
    elif option==0:#Crear
        NAME=input("What will his name be? ")
        while True:#Ataque
            try:
                ATTACK=int(input("How much attack will it have? "))
                break
            except:
                print("please put an integer value")
        while True:#Defensa
            try:
                DEFENSE=input("How much will your defense be? ")
                break
            except:
                print("please put an integer value")
        while True:#Vida
            try:
                HEALTH=input("How much life will it have?")
                break
            except:
                print("please put an integer value")
        characters.append(PLAYER(NAME,ATTACK,DEFENSE,HEALTH))
    elif option==1:#Edit
        print("Which character do you want to edit?")
        ID=int(input("-> "))
        characters.remove(characters[ID])
        NAME=input("What will be his new name? ")
        while True:#Ataque
            try:
                ATTACK=int(input("How much attack will it have? "))
                break
            except:
                print("please put an integer value")
        while True:#Defensa
            try:
                DEFENSE=input("How much will your defense be?")
                break
            except:
                print("please put an integer value")
        while True:#Vida
            try:
                HEALTH=input("How much life will it have?")
                break
            except:
                print("please put an integer value") 
        characters.append(PLAYER(NAME,ATTACK,DEFENSE,HEALTH))
    elif option==2:#Delete
        print("¿Qué personaje quieres eliminar?")
        ID=int(input("-> "))
        characters.remove(characters[ID])