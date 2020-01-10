# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:01:35 2019

@author: Celad
"""

for numero in range(10):
	print(numero)

# Segundo ejemplo: range(start: stop: step)
for numero in range(5, 15, 2):
	print(numero)

# Tercer ejemplo
ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
for ninja in ninjas: 
	print(ninja)

# Cuarto ejemplo
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}

for peli in valoraciones.keys(): 
	print("pelicula:" + peli)
	

for valoracion in valoraciones.values(): 
	# str(x) -> convierte x a tipo cadena de caracteres para 
	# poder encadenarla a "valoraciones:"
	print("valoraciones:" + str(valoracion)) 

for peli, puntuacion in valoraciones.items(): 
	print(peli, "tiene una puntuacion de", puntuacion)


# Quinto ejemplo: cálculo de la suma
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
total = 0
for numero in numeros: 
	total += numero
print(total)

# Sexto ejemplo: 
lista = []
for x in range(2, 6): 
	numero = x**2
	lista.append(numero)
print(lista)

# Séptimo ejemplo: Bucle doble
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes: 
	for peli, valoracion in valoraciones.items(): 
		print(estudiante, "vió", peli, "y le puso una nota de", valoracion)   