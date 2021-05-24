# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:00:26 2020

@author: Lenovo
"""
class Personaje():
    
    #Constructor
    def __init__(self,Ataque,Defenza,Velocidad,Tipo,Nombre,Nivel):
        
        self.Ataque=Ataque
        self.Defenza=Defenza
        self.Velocidad=Velocidad
        self.Tipo=Tipo
        self.Nombre=Nombre
        self.Nivel=Nivel
        
    #Método (Accede a atributos)
    def golpe(self):
        print("El personaje realizó un golpe de poder",self.Ataque)
    def defenza(self):
        print("El personaje se defendió")
    def subirNivel(self,nuevoNivel):
        self.Nivel = nuevoNivel
        print("Subió de nivel")
    def LanzarFuego(self):
        print("Lanzó fuego")    
#Creación de objeto
personaje_1 = Personaje(5,2,3,"Fuego","charmander",1)
personaje_1.golpe
