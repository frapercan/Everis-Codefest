# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:36:29 2018

@author: xaxi
"""

## Año 2016 http://codefest.everis.com/media/Retos-codeFEST-2016.pdf
#Reto 3

def sumar5(num):
    return num+5

def multiplicar3(num):
    return num*3

lista_numeros = set()

def descomponer(i,maximo):
#    print(i)

    if i in lista_numeros:
        return False
    if maximo < i :
        return False
    if i != 1:
        lista_numeros.add(i)
    if maximo/i < 3:
        return descomponer(sumar5(i),maximo)
    if maximo-i < 5:
        return False
        
        
    return descomponer(sumar5(i),maximo),descomponer(multiplicar3(i),maximo)

maximo = 7000
descomponer(1,maximo)
    
print('el resultado del reto3 es: {}'.format(len(lista_numeros)))