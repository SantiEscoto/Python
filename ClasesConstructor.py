# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:38:24 2020

@author: Lenovo
"""



class Personaje:
    
    #Atributos
    Ataque=0
    Velocidad=0
    Tipo= ""
    Defenza=0
    Nombre = ""
    
    #Método
    def golpe(self):
        print("El personaje realizó un golpe")
    def defenza(self):
        print("El personaje se defendió")
        
personaje_1 = Personaje()
personaje_1.Ataque=5

print(personaje_1.Ataque)
personaje_1.golpe()

personaje_2 = Personaje()
personaje_2.Ataque=6
print(personaje_2.Ataque)  