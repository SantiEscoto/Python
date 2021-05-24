# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 21:05:52 2020

@author: Lenovo
"""
import matplotlib.pyplot as plt

from tkinter import*
import serial, time
def createTEXT(reading):
    text=''
    for i in range(len(reading)):
        text += str(reading[i]) + ' '

    return text

def graph(reading):
    y=[]
    for i in range(len(reading)):
        y.append(reading[i])
    return y

def SEND():
    NAME=str(NOMBRE.get())
    PORT=str(PUERTO.get())
    PORT=str(PUERTO.get())
    try:
        arduino = serial.Serial(PORT,9600)
        time.sleep(4)#Stabilize the connection
        for i in range(25):
            arduino.write(b'1')#Bits are sent here
        reading=[]
        
        for i in range(25):
            reading.append(arduino.readline())
        arduino.close()
        
        # for i in range(len(reading)):
        #     reading[i][len(reading[i])-1] = reading[i][len(reading[i])-1].replace('b\r\n','')
    except:
        messagebox.showinfo(message="Please verify that the Port you put in is the right one", title="ERROR")

    archive = open(NAME+".txt","w") #Open the file in write mode "write" 
    Text=createTEXT(reading)

    archive.write(Text)
    archive.close()
    print(Text)
    y=graph(reading)
    plt.plot(y)

    # plt.show

POTENTIOMETER = Tk()
frame = Frame(POTENTIOMETER)

#Objects to use
ASKNAME = Label(frame,text= "Welcome, what name will this new file have?")
NOMBRE = Entry(frame)
ASKPORT = Label(frame,text= "Which port your ARDUINO UNO is connected to?")
PUERTO = Entry(frame)
SEND= Button(frame, text = "SEND", command = SEND)


#Content
ASKNAME.pack()
NOMBRE.pack()
ASKPORT.pack()
PUERTO.pack()
SEND.pack()
frame.pack(padx = 200, pady=150)#Tamaño márco
POTENTIOMETER.mainloop()

