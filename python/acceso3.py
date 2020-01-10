# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:41:11 2019

@author: e052945
"""

padrino = {"name": "El padrino", "year": 1972, "genre": "Drama"}
lista = {"name": "La lista de Schindler", "year": 1993, "genre": "Drama"}
doce = {"name": "12 hombres sin piedad", "year": 1957, "genre": "Drama"}
vida = {"name": "La vida es bella", "year": 1997, "genre": "Comedy"}
bueno = {"name": "El bueno, el feo y el malo", "year": 1966, "genre": " Western"}
cadena = {"name": "Cadena perpetua", "year": 1994, "genre": "Drama"}
siete = {"name": "Los siete samuráis", "year": 1954, "genre": " Adventure"}

netflix = [padrino, lista, doce, vida, bueno, cadena, siete]

print(netflix[0]["year"])
print(netflix[0]["genre"])

for peli in netflix:
    if peli["name"]=="El padrino":
        print(peli["year"])
        print(peli["genre"])

print(len(netflix))

pelis_drama=[]
for peli in netflix:
    if peli["genre"]=="Drama":
        pelis_drama.append(peli)

print(pelis_drama)
print(len(pelis_drama))

pelis_drama_1990=[]
for peli in netflix:
    if (peli["genre"]=="Drama") and (peli["year"]<1990):
        pelis_drama_1990.append(peli)

print(pelis_drama_1990)
print(len(pelis_drama_1990))

lenght=0
for peli in netflix:
    if len(peli["name"])>lenght:
        lenght=len(peli["name"])
        titulo=peli["name"]

print(lenght)
print(titulo)
        
