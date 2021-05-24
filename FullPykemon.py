"""

Created on Wed Jul  1 16:54:54 2020

@author: Lenovo
"""
import random
class PKMN:
    def __init__(self,Nombre,Tipo,Ataque,Defensa,Velocidad,Vida):
        self.Nombre=Nombre
        self.Tipo=Tipo
        self.Ataque=Ataque
        self.Defensa=Defensa
        self.Velocidad=Velocidad
        self.Vida=Vida
    #Métodos
    def atacar_yo(self):
        print(self.Nombre,"realizó un ataque")
        PKMNS[his_pykemon].Vida -= PKMNS[my_pykemon].Ataque
    def atacar_el(self):
        print(self.Nombre,"realizó un ataque")
        PKMNS[my_pykemon].Vida -= PKMNS[his_pykemon].Ataque
    def atacar_fallo(self):
        print(self.Nombre,"realizó un ataque pero ha fallado")
        PKMNS[my_pykemon].Vida
    def defender(self):
        print(self.Nombre,"se ha protegido")
    def defender_yo(self):
        print(self.Nombre,"se ha protegido")
        daño=PKMNS[his_pykemon].Ataque/PKMNS[my_pykemon].Defensa*100
        PKMNS[my_pykemon].Vida -= daño
    def defender_el(self):
        print(self.Nombre,"se ha protegido")
        daño=PKMNS[my_pykemon].Ataque/PKMNS[his_pykemon].Defensa*100
        PKMNS[his_pykemon].Vida -= daño
    def morir(self):
        print(self.Nombre,"ha sido derrotado, que deprimente")
    def subirNivel(self,nuevoNivel):
        self.Nivel = nuevoNivel
        print(self.Nombre,"subió de nivel")
PKMNS = [PKMN("Pikapi","Eléctrico",55,40,90,350),PKMN("Charmanuel","Fuego",52,43,65,390),PKMN("Bulbapey","Planta",49,49,45,450),PKMN("Squirre","Agua",48,65,43,440),PKMN("Gastlioso","Fantasma",100,30,80,300),PKMN("Cuboso","Tierra",50,95,35,500)]
print("¡Bienvenido a Pykemon!")
print("Escoje tu pykemon principal:")
options=[0,1,2,3,4,5]
contador=0
while contador != len(PKMNS):#Lista Pykemons
    print("(",contador,")",PKMNS[0+contador].Nombre)
    contador += 1
while True:#Escoje tú pykemon
    try:
        my_pykemon=int(input("Escribe el número de tu Pykemon principal!: "))
        while my_pykemon not in options:
            print("¿Buscas encontrar un legendario?, lo siento amigo, no hay presupuesto para eso")
            my_pykemon=int(input("-> "))
        break
    except ValueError:
        print("Por favor escribe el número entre parentesis del pykemon que quieras escojer")
print("Ahora prueba combatir contra otro pykemon de la lista!")
while contador != len(PKMNS):#Lista rivales
    print("(",contador,")",PKMNS[0+contador].Nombre)
    contador += 1
while True:#Escoje rival
    try:
        his_pykemon=int(input("Escribe el número de Pykemon contra el que quieres pelear!: "))
        while his_pykemon not in options:
            print("¿Buscas encontrar un legendario?, lo siento amigo, no hay presupuesto para eso")
            his_pykemon=int(input("-> "))
        
        while his_pykemon==my_pykemon:
            print("Vamos hay más luchadores, ponte creativo")
            his_pykemon=int(input("-> "))
        break
        break
    except ValueError:#En caso de error
        print("Por favor escribe el número entre parentesis del pykemon que quieras escojer")
            
print("¡Que la gloriosa batalla comienzé!")
while PKMNS[my_pykemon].Vida>0 and PKMNS[his_pykemon].Vida>0 :#Mientras los jugadores sigan con vida
    print("¿Qué quieres hacer?")
    print("Atacar!(1),Defenderme(0)")
    option=[0,1]
    while True:#Definir acción
        try:
            my_action=int(input("-> "))
            while my_action not in option:
                print("¿No estas tratando de huir o si?, ¡Vamos ataca o defiendete!")
                my_action=int(input("-> "))
            break
        except ValueError:
            print("Vamos hombre no pongas caracteres que no sean 0 ó 1")
            
    if PKMNS[my_pykemon].Velocidad>PKMNS[his_pykemon].Velocidad:#Yo más rápido que el
        his_action=random.randrange(2)
        if my_action==1:
            PKMNS[my_pykemon].atacar_yo()
        elif my_action==0:
            PKMNS[my_pykemon].defender()
        his_action=random.randrange(2)
        if his_action==1:
            if my_action!=0:
                PKMNS[his_pykemon].atacar_el()
            else:
                PKMNS[his_pykemon].atacar_fallo()
        elif his_action==0:
            PKMNS[his_pykemon].defender_el()
    elif PKMNS[my_pykemon].Velocidad<PKMNS[his_pykemon].Velocidad:#El más rápido que yo
        his_action=random.randrange(2)
        if his_action==1:
            PKMNS[his_pykemon].atacar_el()
        elif his_action==0:
            PKMNS[his_pykemon].defender()
        if my_action==1:
            if his_action!=0:
                PKMNS[my_pykemon].atacar_yo()
            else:
                PKMNS[my_pykemon].atacar_fallo()
        elif my_action==0:
            PKMNS[my_pykemon].defender_yo()
    else :#Si tienen la misma velocidad
        random.randrange(2)
        if random.randrange(2)==0:
            if my_action==1:
                PKMNS[my_pykemon].atacar_yo()
            elif my_action==0:
                PKMNS[my_pykemon].defender()
            his_action=random.randrange(2)
            if his_action==1:
                if my_action!=0:
                    PKMNS[his_pykemon].atacar_el()
                else:
                    PKMNS[his_pykemon].atacar_fallo()
            elif his_action==0:
                PKMNS[his_pykemon].defender_el()
        else:
            his_action=random.randrange(2)
            if his_action==1:
                PKMNS[his_pykemon].atacar_el()
            elif his_action==0:
                PKMNS[his_pykemon].defender()
            if my_action==1:
                if his_action!=0:
                    PKMNS[his_pykemon].atacar_yo()
                else:
                    PKMNS[his_pykemon].atacar_fallo()
            elif my_action==0:
                PKMNS[my_pykemon].defender_yo()
    if PKMNS[my_pykemon].Vida>0:#Yo sigo con vida
        print(PKMNS[my_pykemon].Nombre," tuyo tiene",PKMNS[my_pykemon].Vida,"puntos de vida")
    else:#Yo he muerto
        PKMNS[my_pykemon].morir()
    if PKMNS[his_pykemon].Vida>0:#Rival sigue con vida
        print(PKMNS[his_pykemon].Nombre,"enemigo tiene",PKMNS[his_pykemon].Vida,"puntos de vida")
    else:#Rival muere
        PKMNS[his_pykemon].morir()
print("Fin del Juego,¡Gracias por jugar esta demo!")