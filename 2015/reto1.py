# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Frapercan
"""
## Año 2005 http://codefest.everis.com/media/Retos-codeFEST-2015.pdf
#Reto 1 

amount = 10000000

memoria = {} 

def transformar(num):
    return sum([int(d)**2 for d in str(num)])

def ciclo(num):
    if num == 89 :
        memoria[num] = True
    if num == 1:
        memoria[num] = False
    if num in memoria:
        return memoria[num]
    else: 
        memoria[num] = ciclo(transformar(num))
    return memoria[num]
  