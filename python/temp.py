# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

# Ejemplos de listas. 
numeros = [3,4,3,5,7,4,3,1,1]
ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]

# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3,4,5], [1,2,3], [7,3,2]]

# Para seleccionar un elemento por su índice
print(ninjas[0])
print(ninjas[-1])
print(matriz[0])
print(matriz)

# lista[start: stop: step]
print(ninjas[::2])
print(ninjas[:2])
print(ninjas[1: 4])
print(ninjas[::-1])

# añadir un elemento nuevo al final de un lista
print(ninjas)
ninjas.append('Kakashi')
print(ninjas)

# sumar listas
estudiantes = ['Harry', 'Hermione', 'Ron']
profesores = ['Dumbledore', 'Severus', 'Hagrid']
print(estudiantes)
print(profesores)
hogwards = estudiantes + profesores
hogwards1=estudiantes*2
print(estudiantes)
print(profesores)
profesores.extend(estudiantes)
hogwards2=profesores
print(hogwards)
print(hogwards1)
print(profesores)
print(hogwards2)

# media de un conjunto de números
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
suma = sum(numeros)
print(suma)
longitud = len(numeros)
print(longitud)
media = suma / longitud
print(media)

# mínimo y máximo
minimo = min(numeros)
maximo = max(numeros)
print(minimo)
print(maximo)

# Ordenación
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)


# diccionario de película y valoración dada
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}

# algunos métodos de diccionarios
print(valoraciones['Alien'])
print(valoraciones.keys())
print(valoraciones.values())
print(valoraciones.items())

print(5 + 5 == 10)
print('isla' != 'pantano')
print(100 >= 75)
print(93 <= 80)

# para ver si un elemento se encuentra en un conjunto o lista usaremos in
print(3 in [1,2,3,4,5])
print(3 not in [1,2,3,4,5])

print((5 + 5 == 10) and ('isla' != 'pantano'))
print((100 > 75) and (93 < 80))
print((100 > 75) or (93 < 80))
print((93 < 80) or (3 not in [1,2,3,4,5]))

entrada = input("Introduce un número entero: ")
print(entrada)
# convertimos la cadena de caracteres en entero. Esta operación se llama cast. 
numero = int(entrada)
print(numero)