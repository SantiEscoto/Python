"""
PROYECTO FINAL

Creado el Sab Jul 11 09:15:40 2020

@author: Santiago Escoto Rojas
"""
#Importar Librerías
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
        messagebox.showinfo(message="𝓐𝓾𝓽𝓸𝓻: 𝒮𝒶𝓃𝓉𝒾𝒶𝑔𝑜 𝐸𝓈𝒸𝑜𝓉𝑜 𝑅𝑜𝒿𝒶𝓈\n𝐸𝓈𝓉𝑒 𝓅𝓇𝑜𝑔𝓇𝒶𝓂𝒶 𝑒𝓈 𝒸𝒶𝓅á𝓏 𝒹𝑒 𝑔𝑒𝓃𝑒𝓇𝒶𝓇 𝓊𝓃 𝓪𝓻𝓬𝓱𝓲𝓿𝓸.𝓽𝔁𝓽 𝓎 𝑒𝓃 𝑒𝓁 𝓇𝑒𝑔𝒾𝓈𝓉𝓇𝒶𝓇 𝓁𝑜𝓈 𝟧𝟢𝟢 𝒹𝒶𝓉𝑜𝓈 𝓇𝑒𝒸𝒾𝒷𝒾𝒹𝑜𝓈 𝓅𝑜𝓇 𝓊𝓃 𝓼𝓮𝓷𝓼𝓸𝓻 𝒹𝑒 𝒸𝓊𝒶𝓁𝓆𝓊𝒾𝑒𝓇 𝓉𝒾𝓅𝑜 𝒹𝓊𝓇𝒶𝓃𝓉𝑒 𝟦 𝓂𝒾𝓃𝓊𝓉𝑜𝓈 𝒶𝓅𝓇𝑜𝓍𝒾𝓂𝒶𝒹𝒶𝓂𝑒𝓃𝓉𝑒  𝒶𝓁 𝑒𝓈𝓉𝒶𝓇 𝒸𝑜𝓃𝑒𝒸𝓉𝒶𝒹𝑜 𝒶 𝓊𝓃 𝓅𝓊𝑒𝓇𝓉𝑜 𝒹𝑒 𝓉𝓊 𝑜𝓇𝒹𝑒𝓃𝒶𝒹𝑜𝓇, 𝒶𝒹𝑒𝓂á𝓈 𝒹𝑒 𝓰𝓻𝓪𝓯𝓲𝓬𝓪𝓻 𝑒𝓃 𝓁𝒶 𝒸𝑜𝓃𝓈𝑜𝓁𝒶 𝒹𝑒 𝒫𝓎𝓉𝒽𝑜𝓃 𝑒𝓈𝓉𝑜𝓈 𝒹𝒶𝓉𝑜𝓈.\n𝒟𝑒𝒷𝑒 𝒸𝒶𝓇𝑔𝒶𝓇 𝑒𝓁 𝓖𝓻𝓪𝓹𝓱𝓲𝓬𝓢𝓮𝓷𝓼𝓮.𝓲𝓷𝓸 𝒶 𝓈𝓊 𝒜𝓇𝒹𝓊𝒾𝓃𝑜 𝒶𝓃𝓉𝑒𝓈 𝒹𝑒 𝒸𝑜𝓇𝓇𝑒𝓇 𝑒𝓁 𝓅𝓇𝑜𝑔𝓇𝒶𝓂𝒶 𝓎 𝓈𝑒𝑔𝓊𝒾𝓇 𝑒𝓁 𝒹𝒾𝒶𝑔𝓇𝒶𝓂𝒶 𝒹𝑒 𝓁𝒶 𝒾𝓂𝒶𝑔𝑒𝓃 𝓖𝓻𝓪𝓹𝓱𝓲𝓬𝓢𝓮𝓷𝓼𝓮.𝓹𝓷𝓰 𝓅𝒶𝓇𝒶 𝓆𝓊𝑒 𝒻𝓊𝓃𝒸𝒾𝑜𝓃𝑒 𝒸𝑜𝓇𝓇𝑒𝒸𝓉𝒶𝓂𝑒𝓃𝓉𝑒. \n𝓐𝔂𝓾𝓭𝓪 𝓸 𝓼𝓾𝓰𝓮𝓻𝓮𝓷𝓬𝓲𝓪𝓼: 𝒮𝒶𝓃𝓉𝒾𝒶𝑔𝑜.𝐸𝓈𝒸𝑜𝓉𝑜@𝑜𝓊𝓉𝓁𝑜𝑜𝓀.𝒸𝑜𝓂", title="𝓘𝓝𝓕𝓞𝓡𝓜𝓐𝓒𝓘𝓞𝓝")
def ENVIAR():
    lectura=[]
    NAME=str(NOMBRE.get())
    PORT=str(PUERTO.get())
    try:
        arduino = serial.Serial(PORT,9600)
        time.sleep(4)#Estabilizar la conección
        for i in range(500):
            arduino.write(b'1')#Aquí se envían bits
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

#Interfaz Gráfica
SENSOR = Tk()
SENSOR.title("𝕲𝖗𝖆𝖕𝖍𝖎𝖈 𝕾𝖊𝖓𝖘𝖊")
marco = Frame(bg="#145A32")

#Objetos a utilizar
TITTLE = Label(marco,text = "𝕲𝖗𝖆𝖕𝖍𝖎𝖈 𝕾𝖊𝖓𝖘𝖊!", font=("Arial Bold", 30),bg="#145A32", fg="#2ECC71")
ASKNAME = Label(marco,text= "𝐵𝒾𝑒𝓃𝓋𝑒𝓃𝒾𝒹𝑜, ¿𝒬𝓊é 𝓃𝑜𝓂𝒷𝓇𝑒 𝓉𝑒𝓃𝒹𝓇á 𝑒𝓈𝓉𝑒 𝒶𝓇𝒸𝒽𝒾𝓋𝑜 𝓃𝓊𝑒𝓋𝑜?",font=(15),bg="#145A32", fg="#2ECC71")
NOMBRE = Entry(marco,bg="#2ECC71")
ASKPORT = Label(marco,text= "¿𝐸𝓃 𝓆𝓊é 𝓅𝓊𝑒𝓇𝓉𝑜 𝑒𝓈𝓉á 𝒸𝑜𝓃𝑒𝒸𝓉𝒶𝒹𝑜 𝓉𝓊 𝒜𝑅𝒟𝒰𝐼𝒩𝒪 𝒰𝒩𝒪??",font=(15),bg="#145A32", fg="#2ECC71")
PUERTO = Entry(marco,bg="#2ECC71")
ENVIAR= Button(marco, text = "𝓘𝓝𝓘𝓒𝓘𝓐𝓡",font=(20),fg="#2ECC71",bg="#145A32", command = ENVIAR)
INFO= Button(marco, text = "𝓘𝓝𝓕𝓞𝓡𝓜𝓐𝓒𝓘𝓞𝓝 𝓓𝓔𝓛 𝓟𝓡𝓞𝓓𝓤𝓒𝓣𝓞",font=(20),fg="#2ECC71",bg="#145A32", command = INFO)

#Contenido
TITTLE.pack()
INFO.pack()
ASKNAME.pack()
NOMBRE.pack()
ASKPORT.pack()
PUERTO.pack()
ENVIAR.pack()
marco.pack(padx = 0, pady=0)#Tamaño márco

SENSOR.mainloop()