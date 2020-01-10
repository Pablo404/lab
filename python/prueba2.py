# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:32:26 2019

@author: Celad
"""

nominas = [1900, 2000, 1800, 2400, 1700, 1950, 2000, 1806, 2400, 1700]

gasto_mensual=sum(nominas)
gasto_anual=gasto_mensual*12

#print(gasto_mensual)
#print(gasto_anual)

#print(max(nominas))
#print(min(nominas))

#print(gasto_mensual/len(nominas))


nominas_euro=[]
for nomina in nominas:
    nominas_euro.append(nomina/1.09)
    
#print(nominas_euro)

nominas_euro2=[nomina/1.09 for nomina in nominas]
#print(nominas_euro2)

nominas_dolar=[]
for nomina in nominas_euro:
    if nomina>2000:
        nominas_dolar.append(nomina*1.09)

#print(nominas_dolar)

nominas_dolar2=[nomina*1.09 for nomina in nominas_euro2 if nomina>2000]
#print(nominas_dolar2)

fecha = "10/03/2016"
print("dia:",str(fecha[:2]))
print("mes:",str(fecha[3:5]))
print("año:",str(fecha[6:]))

mes=int(fecha[3:5])
if mes==2:
    dias=28
elif mes>7:
    if (mes % 2)==0:
        dias=31
    else:
        dias=30
else:
    if (mes % 2)==0:
        dias=30
    else:
        dias=31
    
print(dias)

dia1=input("Introduce el dia: ")
mes1=input("Introduce el mes: ")
año1=input("Introduce el año: ")
fecha1=str(dia1)+"/"+str(mes1)+"/"+str(año1)
print(fecha1)
