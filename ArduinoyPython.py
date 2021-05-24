"""
Created on Sat Jul 11 09:17:44 2020

@author: Santiago Escoto
"""
import matplotlib.pyplot as plt
from tkinter import*
import serial, time


def crearTEXTO(lectura):
    texto=''
    for i in range(len(lectura)):
        lectura_str=lectura[i].decode("utf8")
        texto += str(lectura_str)

    return texto

def graficar(lectura):
    y=[]
    for i in range(len(lectura)):
        lectura_str=lectura[i].decode("utf8")
        y.append(int(lectura_str))
    return y

def ENVIAR():
    NAME=str(NOMBRE.get())
    PORT=str(PUERTO.get())
    try:
        arduino = serial.Serial(PORT,9600)
        time.sleep(4)#Estabilizar la conección
        for i in range(500):
            arduino.write(b'1')#Aquí se envían bits
        lectura=[]
        
        for i in range(500):
            lectura.append(arduino.readline())
        arduino.close()
        
        # for i in range(len(lectura)):
        #     lectura[i][len(lectura[i])-1] = lectura[i][len(lectura[i])-1].replace('b\r\n','')
    except:
        messagebox.showinfo(message="Por favor verifica que el Puerto que pusiste sea el correcto", title="ERROR")

    archivo = open(NAME+".txt","w") #Abrimos el archivo en modalidad escritura "write"
    text=crearTEXTO(lectura)

    archivo.write(text)
    archivo.close()
    print(text)
    y=graficar(lectura)
    plt.plot(y)
    plt.show()



POTENCIOMETRO = Tk()
marco = Frame(POTENCIOMETRO)

#Objetos a utilizar
ASKNAME = Label(marco,text= "Bienvenido, ¿Qué nombre tendrá este archivo nuevo?")
NOMBRE = Entry(marco)
ASKPORT = Label(marco,text= "¿En qué puerto está conectado tu ARDUINO UNO?")
PUERTO = Entry(marco)
ENVIAR= Button(marco, text = "ENVIAR", command = ENVIAR)


#Contenido
ASKNAME.pack()
NOMBRE.pack()
ASKPORT.pack()
PUERTO.pack()
ENVIAR.pack()


#sides TOP LEFT RIGHT CENTER LEFT

marco.pack(padx = 100, pady=150)#Tamaño márco
POTENCIOMETRO.mainloop()