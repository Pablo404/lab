# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:13:01 2019

@author: e052945
"""

nominas = [1900, 2000, 1800, 2400, 1700, 1950, 2000, 1806, 2400, 1700]

gasto_mensual=sum(nominas)
gasto_anual=gasto_mensual*12

print(gasto_mensual)
print(gasto_anual)

print(max(nominas))
print(min(nominas))

media=gasto_mensual/len(nominas)

print(media)

nominas_euros=[]
for nomina in nominas:
    nominas_euros.append(nomina/1.09)

print(nominas_euros)

nominas_new=[]
for nomina in nominas_euros:
    if nomina>2000:
        nominas_new.append(nomina*1.09)
    else:
        nominas_new.append(nomina)

print(nominas_new)

nominas_new2=[]
for nomina in nominas_euros:
    if nomina>2000:
        nominas_new2.append(nomina*1.09)

print(nominas_new2)



    