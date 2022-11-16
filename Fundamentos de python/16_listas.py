numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #se crea una lista con números del 1 al 10, las listas se crean con corchetes. las listas sirven para guardar datos y poder manipularlos

tasks = ["comprar", "vender", "comer", "dormir"] #se crea una lista con strings

types = [1, "dos", 3.0, True] #se crea una lista con diferentes tipos de datos

text = 'hola' # las cadenas no se pueden modificar, pero las listas si; text[0] = w no se puede hacer, pero numbers[0] = 0 si se puede hacer
#-------------------------------------------------

print(tasks) #se imprime la lista tasks
print(type(tasks)) #se imprime el tipo de dato de la lista tasks

print(numbers) #se imprime la lista numbers
print(type(numbers)) #se imprime el tipo de dato de la lista numbers

print(types) #se imprime la lista types
print(type(types)) #se imprime el tipo de dato de la lista types


print (numbers[0]) #se imprime el primer elemento de la lista numbers

tasks[0] = 'comprar comida' #se modifica el primer elemento de la lista tasks
print(tasks) #se imprime la lista modificada

print (numbers[:3]) #se imprime los primeros 3 elementos de la lista numbers
print(True in types) #se imprime si el valor true esta en la lista types