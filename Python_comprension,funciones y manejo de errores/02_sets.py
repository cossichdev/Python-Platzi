#los conjuntos en python son colecciones desordenadas de elementos únicos y no mutables. Tampoco pueden tener elementos duplicados.

#set = conjunto

set_countries = {'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela', 'Brasil', 'Paraguay', 'Uruguay', 'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela', 'Brasil', 'Paraguay', 'Uruguay'} #es similar a un diccionario pero no tiene valores, solo claves
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 2.5, '3', True, "None", } #no se puede tener elementos de diferentes tipos en un conjunto
print(set_types)
print(type(set_types))


set_from_string = set('Hola Mundo') #crea un conjunto a partir de una cadena de texto y cada carácter es un elemento del conjunto
print(set_from_string)
print(type(set_from_string))


set_from_tupla = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) #crea un conjunto a partir de una tupla
print(set_from_tupla)
print(type(set_from_tupla))


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
set_from_list = set(numbers) #crea un conjunto a partir de una lista
print(set_from_list)
print(type(set_from_list))


unique_numbers = list(set_numbers) #crea una lista a partir de un conjunto
print(unique_numbers)
print(type(unique_numbers))

