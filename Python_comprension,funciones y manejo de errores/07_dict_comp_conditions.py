# las condicionales en los diccionarios por comprensión son muy útiles para filtrar datos.
# {key: value for key, value in iterable if condition} = key es la llave del diccionario, value es el valor del diccionario, iterable es la secuencia que se va a iterar, y condition es la condicion que se va a evaluar. iterar significa recorrer una secuencia de datos, por ejemplo una lista, un diccionario, un string, etc.

import random
'''
countries = {country: random.randint(0, 100) for country in ["Colombia", "Peru", "Chile", "Argentina", "Ecuador", "Bolivia", "Venezuela", "Brasil", "Paraguay", "Uruguay"] if random.randint(0, 1) == 0} #se crea un diccionario con los paises de america del sur, la llave es el pais y el valor es un numero aleatorio entre 0 y 100, se agrega una condicion al final de la lista por comprension, el diccionario se lee asi: "para cada elemento en la secuencia, hacer algo con ese elemento, si se cumple una condicion", en este caso se agrega un pais al diccionario si el numero aleatorio es par

print(countries)

'''

names = ['Luis', 'Maria', 'Jose', 'Pedro', 'Juan', 'Pablo','Luisa', 'Marta', 'Sofia', 'Camila', 'Andrea', 'Sara']

people = {name: random.randint(0, 100) for name in names}
print(people) #se crea un diccionario con los nombres de la lista names, la llave es el nombre y el valor es un numero aleatorio entre 0 y 100

result = { name: age for (name, age) in people.items() if age > 60} #se crea un diccionario con los nombres de la lista names, la llave es el nombre y el valor es un numero aleatorio entre 0 y 100, se agrega una condicion al final de la lista por comprension, el diccionario se lee asi: "para cada elemento en la secuencia, hacer algo con ese elemento, si se cumple una condicion", en este caso se agrega un nombre al diccionario si el numero aleatorio es mayor a 50
print(result)
#-----------------------------

text = "Hola, soy Glauco, un programador de Python"
unique = {clave : clave.upper() for clave in text if clave in 'aieou'} # se crea una condición donde solo pedirá las vocales del text y las convertirá en mayúsculas, siendo esta la clave
print(unique)

