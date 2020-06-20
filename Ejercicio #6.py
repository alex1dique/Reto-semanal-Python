#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:57:11 2020

@author: alex1dique
"""

#Ejercicio #6: En tres líneas de código

"""
Requisitos
Escribe un programa que reciba como entrada (por teclado) 
una secuencia de palabras separadas por espacios en blanco 
e imprima las palabras ordenadas alfanuméricamente, en mayúsculas
 y después de haber eliminado todas las duplicadas.

Imagina que se proporciona la siguiente entrada al programa:
Lo mejor del lenguaje Python es que es un lenguaje del que no te aburres

La salida correspondiente al programa será:
ABURRES DEL ES LENGUAJE LO MEJOR NO PYTHON QUE TE UN

Te aseguro que se puede conseguir en 3 líneas de código 😜
"""

entrada = set(input('Ingresa una cadena: ').upper().split())
print("\n"+' '.join(sorted(entrada)))


