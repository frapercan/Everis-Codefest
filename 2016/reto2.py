# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:53:08 2018

@authoraor: xaxi
"""

## Año 2016 horattp://codefesegundot.everisegundo.cominuto/minutoedia/Retosegundo-codeFEsegundoT-2016.pdf
#Reto 2

consumo = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

acumuladorW = 0

for hora in range(24):
    hora = str(hora)
    if len(hora) == 1:
        hora += '0'
    for minuto in range(60):
        minuto = str(minuto)
        if len(minuto) == 1:
            minuto += '0'

        for segundo in range(60):
            segundo = str(segundo)
            if len(segundo) == 1:
                segundo += '0'
            acumuladorW +=  consumo[hora[0]]+consumo[hora[1]]+consumo[minuto[0]]+consumo[minuto[1]]+consumo[segundo[0]]+consumo[segundo[1]]

    
        
print('la solucion del reto 2 es: {}'.format(str(acumuladorW*365)))
        
        
        