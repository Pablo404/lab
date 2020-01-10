# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:29:52 2019

@author: Celad
"""

valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes: 
	# en este nivel estamos dentro del primer for
	print(">>> estamos dentro del primer for hablando de", estudiante)
	for peli, valoracion in valoraciones.items(): 
		# en este nivel estamos dentro del segundo for
		print(">>> estamos dentro del segundo for hablando de", peli, "y de", estudiante)
		print(estudiante, "vió", peli, "y le puso una nota de", valoracion)