# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:03:02 2020

@author: Lenovo
"""
#Función
def count_repeated(list,value):
    position=[]
    index=0

    for element in list:
        if element == value:
            position.append(index)
        index +=1
    return position

#Presentation
print("This program find all the repeated values ​​in a list and they tell you in what position they are")
print("First you have to make a list for that tell me")

#Input
while True:
    try:
        elements=int(input("How many items does this list have? "))
        break
    except ValueError:
        print("Please write the number of elements with numeric and integer characters")

print("Tell me the items on this list. They can be of any type")
list=[]
counter=0
while counter != elements:
    value=input("-> ")
    list.append(value)
    counter += 1
#From here we already insert a list with n elements and name each element

#Now we have to see if there are repeated values

unique = []
k=0
while k != elements:
    element=list[k]
    position=count_repeated(list,element)
    if element not in unique:
        if len(position)==1:
            print (element,"repeats once in position",position)
        else:
            print (element,"is repeated",len(position),"times in positions",position)
        unique.append(element)
    k += 1
