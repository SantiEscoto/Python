"""
PROYECTO FINAL

Creado el Sab Jul 11 09:15:40 2020

@author: Santiago Escoto Rojas
"""
#Importar Librerรญas
import matplotlib.pyplot as plt
from tkinter import*
import serial, time

#Definir Funciones
def DECODE(lectura):#DECODIFICAR
    texto=''                                    
    for i in range(len(lectura)):
        lectura_str=lectura[i].decode("utf8")
        texto += str(lectura_str)
    return texto
def GRAFICAR(lectura):#GENERAR DATOS A GRAFICAR
    y=[]
    for i in range(len(lectura)):
        lectura_str=lectura[i].decode("utf8")
        y.append(int(lectura_str))
    return y
def INFO():
        messagebox.showinfo(message="๐๐พ๐ฝ๐ธ๐ป: ๐ฎ๐ถ๐๐๐พ๐ถ๐๐ ๐ธ๐๐ธ๐๐๐ ๐๐๐ฟ๐ถ๐\n๐ธ๐๐๐ ๐๐๐๐๐๐ถ๐๐ถ ๐๐ ๐ธ๐ถ๐รก๐ ๐น๐ ๐๐๐๐๐๐ถ๐ ๐๐ ๐ช๐ป๐ฌ๐ฑ๐ฒ๐ฟ๐ธ.๐ฝ๐๐ฝ ๐ ๐๐ ๐๐ ๐๐๐๐พ๐๐๐๐ถ๐ ๐๐๐ ๐ง๐ข๐ข ๐น๐ถ๐๐๐ ๐๐๐ธ๐พ๐ท๐พ๐น๐๐ ๐๐๐ ๐๐ ๐ผ๐ฎ๐ท๐ผ๐ธ๐ป ๐น๐ ๐ธ๐๐ถ๐๐๐๐พ๐๐ ๐๐พ๐๐ ๐น๐๐๐ถ๐๐๐ ๐ฆ ๐๐พ๐๐๐๐๐ ๐ถ๐๐๐๐๐พ๐๐ถ๐น๐ถ๐๐๐๐๐  ๐ถ๐ ๐๐๐๐ถ๐ ๐ธ๐๐๐๐ธ๐๐ถ๐น๐ ๐ถ ๐๐ ๐๐๐๐๐๐ ๐น๐ ๐๐ ๐๐๐น๐๐๐ถ๐น๐๐, ๐ถ๐น๐๐รก๐ ๐น๐ ๐ฐ๐ป๐ช๐ฏ๐ฒ๐ฌ๐ช๐ป ๐๐ ๐๐ถ ๐ธ๐๐๐๐๐๐ถ ๐น๐ ๐ซ๐๐๐ฝ๐๐ ๐๐๐๐๐ ๐น๐ถ๐๐๐.\n๐๐๐ท๐ ๐ธ๐ถ๐๐๐ถ๐ ๐๐ ๐๐ป๐ช๐น๐ฑ๐ฒ๐ฌ๐ข๐ฎ๐ท๐ผ๐ฎ.๐ฒ๐ท๐ธ ๐ถ ๐๐ ๐๐๐น๐๐พ๐๐ ๐ถ๐๐๐๐ ๐น๐ ๐ธ๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐ถ๐๐ถ ๐ ๐๐๐๐๐พ๐ ๐๐ ๐น๐พ๐ถ๐๐๐ถ๐๐ถ ๐น๐ ๐๐ถ ๐พ๐๐ถ๐๐๐ ๐๐ป๐ช๐น๐ฑ๐ฒ๐ฌ๐ข๐ฎ๐ท๐ผ๐ฎ.๐น๐ท๐ฐ ๐๐ถ๐๐ถ ๐๐๐ ๐ป๐๐๐ธ๐พ๐๐๐ ๐ธ๐๐๐๐๐ธ๐๐ถ๐๐๐๐๐. \n๐๐๐พ๐ญ๐ช ๐ธ ๐ผ๐พ๐ฐ๐ฎ๐ป๐ฎ๐ท๐ฌ๐ฒ๐ช๐ผ: ๐ฎ๐ถ๐๐๐พ๐ถ๐๐.๐ธ๐๐ธ๐๐๐@๐๐๐๐๐๐๐.๐ธ๐๐", title="๐๐๐๐๐ก๐๐๐๐๐๐")
def ENVIAR():
    lectura=[]
    NAME=str(NOMBRE.get())
    PORT=str(PUERTO.get())
    try:
        arduino = serial.Serial(PORT,9600)
        time.sleep(4)#Estabilizar la conecciรณn
        for i in range(500):
            arduino.write(b'1')#Aquรญ se envรญan bits
            lectura.append(arduino.readline())
        arduino.close()
        archivo = open(NAME+".txt","w") #Abrimos el archivo en modalidad escritura "write"
        text=DECODE(lectura)#DECODIFICAR
        archivo.write(text)#GUARDAR
        archivo.close()#CERRAR
        y=GRAFICAR(lectura)#GENERAR DATOS A GRAFICAR
        plt.plot(y)#GRAFICAR
        plt.show()#MOSTRAR GRAFICA
    except:
        messagebox.showerror(message="Por favor verifica que el Puerto que pusiste sea el correcto", title="ERROR")

#Interfaz Grรกfica
SENSOR = Tk()
SENSOR.title("๐ฒ๐๐๐๐๐๐ ๐พ๐๐๐๐")
marco = Frame(bg="#145A32")

#Objetos a utilizar
TITTLE = Label(marco,text = "๐ฒ๐๐๐๐๐๐ ๐พ๐๐๐๐!", font=("Arial Bold", 30),bg="#145A32", fg="#2ECC71")
ASKNAME = Label(marco,text= "๐ต๐พ๐๐๐๐๐๐พ๐น๐, ยฟ๐ฌ๐รฉ ๐๐๐๐ท๐๐ ๐๐๐๐น๐รก ๐๐๐๐ ๐ถ๐๐ธ๐ฝ๐พ๐๐ ๐๐๐๐๐?",font=(15),bg="#145A32", fg="#2ECC71")
NOMBRE = Entry(marco,bg="#2ECC71")
ASKPORT = Label(marco,text= "ยฟ๐ธ๐ ๐๐รฉ ๐๐๐๐๐๐ ๐๐๐รก ๐ธ๐๐๐๐ธ๐๐ถ๐น๐ ๐๐ ๐๐๐๐ฐ๐ผ๐ฉ๐ช ๐ฐ๐ฉ๐ช??",font=(15),bg="#145A32", fg="#2ECC71")
PUERTO = Entry(marco,bg="#2ECC71")
ENVIAR= Button(marco, text = "๐๐๐๐๐๐๐ก",font=(20),fg="#2ECC71",bg="#145A32", command = ENVIAR)
INFO= Button(marco, text = "๐๐๐๐๐ก๐๐๐๐๐๐ ๐๐๐ ๐๐ก๐๐๐ค๐๐ฃ๐",font=(20),fg="#2ECC71",bg="#145A32", command = INFO)

#Contenido
TITTLE.pack()
INFO.pack()
ASKNAME.pack()
NOMBRE.pack()
ASKPORT.pack()
PUERTO.pack()
ENVIAR.pack()
marco.pack(padx = 0, pady=0)#Tamaรฑo mรกrco

SENSOR.mainloop()