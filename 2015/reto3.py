# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Frapercan
"""
## Año 2005 http://codefest.everis.com/media/Retos-codeFEST-2015.pdf
#reto3

contenedores = [[465,19981,9879],[6113,8849,161130],[1261,81610,6849]]

combinaciones = [[i,j,k]  for i in range(3) for j in range(3) 
                            for k in range(3) 
                                if ((i != j) and (j != k) and (i != k)) ]

min_movimientos = float('inf')

for combinacion in combinaciones:
    movimientos = 0
    for (i,tipo) in enumerate(combinacion):
        movimiento  = 0
       
        for (j,contenedor) in enumerate(contenedores):
            if i != j:
                movimiento += contenedor[tipo]
        movimientos += movimiento
    if movimientos < min_movimientos:
        min_movimientos = movimientos
        
print('La solución del resto 3 es {}'.format(str(min_movimientos)))
            
        

        