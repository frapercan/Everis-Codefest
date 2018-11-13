# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Frapercan
"""
## Año 2005 http://codefest.everis.com/media/Retos-codeFEST-2015.pdf
#reto 2

memoryMap = {}
distancia = 50

def propagacion(secuencia):
  if secuencia in memoryMap:
    return memoryMap[secuencia]
  if secuencia == distancia:
    return 1
  if secuencia > distancia:
    return 0
  memoryMap[secuencia] = propagacion(secuencia+1)+propagacion(secuencia+2)
  return  memoryMap[secuencia]


print('la solucion del reto 2 es: {}'.format(str(propagacion(0))))

        