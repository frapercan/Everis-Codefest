# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:53:08 2018

@author: xaxi
"""

## Año 2016 http://codefest.everis.com/media/Retos-codeFEST-2016.pdf
#Reto 1 



posiciones_medicamentos = [1, 3, 4, 8, 8, 10, 10, 14, 15, 16, 20, 
21, 22, 22, 23, 24, 24, 27, 31, 39]


distancia_optima = float('inf')

for posicion_caja in range(max(posiciones_medicamentos)):
    distancia_recorrida = posicion_caja
    posicion = posicion_caja
    for posicion_medicamento in posiciones_medicamentos:
        distancia_recorrida += abs(posicion_medicamento-posicion)
        posicion = posicion_medicamento
        distancia_recorrida += abs(posicion - posicion_caja)
        posicion = posicion_caja
    distancia_recorrida += posicion
    if distancia_recorrida < distancia_optima:
        distancia_optima = distancia_recorrida
        
        
        
print('la solución es: {} metros recorridos'.format(str(distancia_optima)))
        
        
