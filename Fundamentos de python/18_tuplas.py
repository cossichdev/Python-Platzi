#las tuplas son inmutables, es decir, y sirven para guardar datos que no se van a modificar

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #se crea una tupla con números del 1 al 10, las tuplas se crean con paréntesis. las tuplas sirven para guardar datos que no se van a modificar

strings = ('af','gt','fd','sa','ac','ds') #se crea una tupla con strings

print(numbers)
print(strings)
print(type(strings)) #se imprime el tipo de dato de la variable strings
print(type(numbers)) #se imprime el tipo de dato de la variable numbers

#las tuplas son solo de lectura, no se pueden modificar pero tienen métodos que se pueden usar como el método count, index, etc.

my_list = list(strings) #se convierte la tupla strings en una lista
print(type(my_list))
print(my_list)