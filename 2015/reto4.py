# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Frapercan
"""
## Año 2005 http://codefest.everis.com/media/Retos-codeFEST-2015.pdf
#Reto 4

import numpy as np

campo = np.loadtxt(r'C:\Users\xaxi\Documents\GitHub\Everis-Codefest\2015\reto4.txt')
altura = campo.shape[0]
anchura = campo.shape[1]
posiciones_tablero = np.array([(i,j) for i in range(altura) for j in range(anchura)])
numero_pasos = 3
direcciones = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
mejor_colecta = 0

def busqueda(posicion,cantidad,pasos,direccion):
    if pasos == numero_pasos:
        return cantidad
    if posicion not in posiciones_tablero:
        return cantidad
    if len(direccion)==0:
        return np.max([busqueda(posicion+direccion,cantidad + campo[(posicion+direccion)[0],(posicion+direccion)[1]],pasos+1,direccion) for direccion in direcciones_disponibles(posicion)])
    return busqueda(posicion+direccion,cantidad + campo[(posicion+direccion)[0],(posicion+direccion)[1]],pasos+1,direccion)

def direcciones_disponibles(posicion):
    return [direccion for direccion in direcciones if (posicion[0]+(numero_pasos*direccion[0])>=0 and posicion[0]+(numero_pasos*direccion[0]) < anchura and posicion[1]+ (numero_pasos*direccion[1])>=0 and posicion[1]+(numero_pasos*direccion[1]) < altura )]
        

for i in range(altura):
    for j in range(anchura):
        solucion = busqueda(np.array((i,j)),campo[i,j],0,[])
        if solucion > mejor_colecta:
            mejor_colecta = solucion
       
print('la solucion del reto 3 es: {}'.format(str(mejor_colecta)))

        
