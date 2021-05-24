# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:50:55 2020

@author: Lenovo
"""

resultado=0
from tkinter import*
def sumar():
    try:
        Valor1=float(entrada1.get())
        Valor2=float(entrada2.get())
        resultado=Valor1+Valor2
    except ValueError:
        messagebox.showinfo(message="Por favor escribe un caracter que sea un número", title="ERROR")
           
    messagebox.showinfo(message="Tu resultado es: "+f"{resultado}", title="RESULTADO")

    entrada1.delete(0,len(entrada1.get()))
    entrada2.delete(0,len(entrada2.get()))
def restar():
    try:
        Valor1=float(entrada1.get())
        Valor2=float(entrada2.get())
        resultado=Valor1-Valor2
    except ValueError:
        messagebox.showinfo(message="Por favor escribe un caracter que sea un número", title="ERROR")
           
    messagebox.showinfo(message="Tu resultado es: "+f"{resultado}", title="RESULTADO")

    entrada1.delete(0,len(entrada1.get()))
    entrada2.delete(0,len(entrada2.get()))
def multi():
    try:
        Valor1=float(entrada1.get())
        Valor2=float(entrada2.get())
        resultado=Valor1*Valor2
    except ValueError:
        messagebox.showinfo(message="Por favor escribe un caracter que sea un número", title="ERROR")
           
    messagebox.showinfo(message="Tu resultado es: "+f"{resultado}", title="RESULTADO")

    entrada1.delete(0,len(entrada1.get()))
    entrada2.delete(0,len(entrada2.get()))
def divi():
    try:
        Valor1=float(entrada1.get())
        Valor2=float(entrada2.get())
        resultado=Valor1/Valor2
    except ValueError:
        messagebox.showinfo(message="Por favor escribe un caracter que sea un número", title="ERROR")
    except ZeroDivisionError:
        messagebox.showinfo(message="No se puede dividir entre 0", title="ERROR")
           
    messagebox.showinfo(message="Tu resultado es: "+f"{resultado}", title="RESULTADO")

    entrada1.delete(0,len(entrada1.get()))
    entrada2.delete(0,len(entrada2.get()))

calculadora = Tk()
marco = Frame(calculadora)

#Objetos a utilizar
etiqueta = Label(marco,text= "Bienvenido, ¿Qué operación quieres realizar?")
entrada1 = Entry(marco)
entrada2 = Entry(marco)
boton_suma= Button(marco, text = "+", command = sumar)
boton_resta= Button(marco, text = "-", command = restar)
boton_multi= Button(marco, text = "x", command = multi)
boton_divi= Button(marco, text = "/", command = divi)

#Contenido
etiqueta.pack()
entrada1.pack(side=LEFT)
boton_suma.pack(side=LEFT)
boton_resta.pack(side=LEFT)
boton_multi.pack(side=LEFT)
boton_divi.pack(side=LEFT)
entrada2.pack(side=RIGHT)

#sides TOP LEFT RIGHT CENTER LEFT

marco.pack(padx = 200, pady=150)#Tamaño márco
calculadora.mainloop()