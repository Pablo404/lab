# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:15:17 2019

@author: e052945
"""

fecha = "10/12/2016"

print("dia:",fecha[:2])
print("mes:",fecha[3:5])
print("año:",fecha[-4:])

dia=int(fecha[:2])
mes=int(fecha[3:5])
año=int(fecha[-4:])

if mes==2:
    dias_mes=28
else:
    if mes>7:
        if (mes % 2)==0:
            dias_mes=31
        else:
            dias_mes=30
    else:
        if (mes % 2)==0:
            dias_mes=30
        else:
            dias_mes=31

print(dias_mes)

input_dia=input("Introduzca el dia: ")
input_mes=input("Introduzca el mes: ")
input_año=input("Introduzca el año: ")

fecha2=str(input_dia)+"/"+str(input_mes)+"/"+str(input_año)

print("dia:",fecha2[:2])
print("mes:",fecha2[3:5])
print("año:",fecha2[-4:])
