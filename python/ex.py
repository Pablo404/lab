# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:36:00 2019

@author: e052945
"""

print("Cateto 1", "Cateto 2", "      Hipotenusa")

for cateto1 in range(1,11):
    for cateto2 in range(11,21):
        hipotenusa=((cateto1**2)+(cateto2**2))**0.5
        print("    ",cateto1,"    ", cateto2,"     ",hipotenusa)






