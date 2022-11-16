#la sintaxis de diccionarios por comprensión son muy útiles para crear diccionarios, pero también se pueden usar para crear listas y conjuntos.
#las diccionarios_comprehension se leen como: "para cada elemento en una secuencia, hacer algo con ese elemento", por ejemplo:
#{key: value for var in iterable} = key es la llave del diccionario, value es el valor de la llave, var es el elemento que se va a agregar al diccionario, iterable es la secuencia que se va a iterar, y el elemento se agrega al diccionario.


dict1 = {}
for element in range(10): #se lee así: "para cada elemento en la secuencia, hacer algo con ese elemento", en este caso se agrega cada elemento a un diccionario
    dict1[element] = element * 2 #se multiplica por 2 cada elemento de la secuencia
print("1", dict1)  # se imprime la lista
print(type(dict1))

dict2 = {element: element * 2 for element in range(10)} #se crea un diccionario con los números del 0 al 9, el diccionario se lee así: "para cada elemento en la secuencia, hacer algo con ese elemento", en este caso se multiplica por 2 cada elemento de la secuencia y se agrega al diccionario con su llave correspondiente.
#podemos leerlo: en el rango del 0 al 9, para cada elemento, se multiplica por 2 y se agrega al diccionario con su llave correspondiente. esto se lee de derecha a izquierda
print("2", dict2)  # se imprime la lista
print(type(dict2))

#--------------------------------------------------------------------------------------
# iteración con base en una lista

import random

countries = ['Colombia', 'Mexico', 'Peru', 'chile', 'argentina', 'ecuador', 'Venezuela', 'Uruguay', 'Paraguay', 'Bolivia', 'brasil', 'Guatemala']

population = {}
for country in countries: #para country en countries
    population[country] = random.randint(1,100) #population en countries es igual a un numero aleatorio entre 1 y 100
print("1", population)

population2 = {country: random.randint(1,100) for country in countries} # se lee: para cada país en la lista de países, se agrega un numero aleatorio entre 1 y 100 al diccionario con su llave correspondiente
print("2", population2)

#--------------------------------------------------------------------------------------
#iteración con base en dos listas

names = ['Luis','Maria','Jose','Pedro','Juan','Pablo','Luisa','Marta','Sofia','Camila','Andrea','Sara']

ages = [random.randint(1,100) for edad in range(len(names))] #se crea una lista con números aleatorios entre 1 y 100, la lista tiene la misma longitud que la lista de nombres
print(ages)

#tenemos dos listas, una con nombres y otra con edades, queremos crear un diccionario con los nombres como llaves y las edades como valores.
#el algoritmo seria: para cada nombre en la lista de nombres, se agrega al diccionario con su llave correspondiente, y el valor de la llave es la edad correspondiente en la lista de edades.

print(list(zip(names, ages))) #se crea una lista de tuplas con los nombres y las edades, zip ayuda a unir dos listas en una lista de tuplas

people = {name: age for (name, age) in zip(names, ages)} # se lee: para cada nombre en la lista de nombres, se agrega al diccionario con su llave correspondiente, y el valor de la llave es la edad correspondiente en la lista de edades.
print(people)