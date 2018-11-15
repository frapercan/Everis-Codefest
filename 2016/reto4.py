# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:20:06 2018

@author: xaxi
"""

## Año 2016 http://codefest.everis.com/media/Retos-codeFEST-2016.pdf
#Reto 4

import numpy as np

datos = np.array([[7000,150000],
                  [200,7000],
                  [620,40000],
                  [3440,3000],
                  [220,2000],
                  [1777,10000],
                  [800,3000],
                  [950,3000],
                  [2300,8000],
                  [1250,150000],
                  [1987,30000],
                  [5000,699099],
                  [2300,100050],[800,10000],
                  [5300,20000],
                  [4300,30000],
                  [2100,1500]])

pesos = datos[:,0]
precios = datos[:,1]
#ejemplo2
#pesos = np.array([5000,100,3000,300,1500,500,900,800])
#precios = np.array([900000,750000,300000,50000,500000,400000,10000,8000])
capacidad = 8000
numero_pedidos = len(pesos)

numero_combinaciones = 2**numero_pedidos

combinaciones = ['0'*(numero_pedidos-len(bin(n)[2:]))+(bin(n)[2:]) for n in range(numero_combinaciones)]
combinaciones = [[int(n)  for n in combinacion] for combinacion in combinaciones]
combinaciones = np.array(combinaciones)

resultado = max([sum(combinacion*precios) for combinacion in combinaciones if sum(combinacion*pesos) <= capacidad ])

print('el resultado del reto 4 es:{}'.format(str(resultado)))