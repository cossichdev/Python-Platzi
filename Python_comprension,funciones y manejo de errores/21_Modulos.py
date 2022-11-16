#los modulos permiten modular una app, pueden ser archivos directamente pero python viene con varios modulos. por ejemplo functools y su funcion reduce.

#random ayuda a asignar valores aleatorios

import sys #sys pregunta sobre el sistema operativo
print(sys.path) #imprime el array de toda la ruta a correr y nos da demasiados detalles

import re #expresiones regulares,
text = 'Mi numero de telefono es 321467878 el codigo del pais es 57 y mi numero de la suerte es 9'
result = re.findall('[0-9]+', text) #este modulo tiene su propia sintaxis y es necesario aprenderlo por aparte
print(result) #buscara todos los numeros en esta variable

import time #modulo para trabajar con fechas y horas (tiempo)
timestamp = time.time() #timestamp da el formato de hora actual en formato unix
print(timestamp) #formato de computadora
result = time.asctime(time.localtime()) #formato de lectura para humanos "localtime" y asctime recibe la forma en la que queremos el formato
print (result) #formato humanos

import collections #sirve para manejar listas
numbers = [0,1,1,2,3,3,3,4,5,6,21] #lista con numeros repetidos
counter = collections.Counter(numbers) #funcion Counter sirve para ver la frecuencia de un numero en una lista
print(counter)