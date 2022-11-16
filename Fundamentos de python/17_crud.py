#crud = leer, crear, actualizar, borrar

# .append(): Añade un ítem al final de la lista.
# .clear(): Vacía todos los ítems de una lista.
# .extend(): Une una lista a otra.
# .count(): Cuenta el número de veces que aparece un ítem.
# .index(): Devuelve el índice en el que aparece un ítem(error si no aparece).
# .insert(): Agrega un ítem a la lista en un índice específico.
# .pop(): Extrae un ítem de la lista y lo borra.
# .remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
# .reverse(): Le da la vuelta a la lista actual.
# .sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #se crea una lista con números del 1 al 10, las listas se crean con corchetes. las listas sirven para guardar datos y poder manipularlos
print(numbers)

print(numbers[1]) #se imprime el primer elemento de la lista numbers

numbers[-1] = 11 #se modifica el ultimo elemento de la lista numbers
print(numbers) #se imprime la lista modificada

numbers.append(12) #se agrega un elemento al final de la lista numbers, append es una función que se usa para agregar un elemento al final de la lista
print(numbers)  # se imprime la lista modificada

numbers.insert(0,5) #se agrega un elemento en la posición 0 de la lista numbers, insert es una función que se usa para agregar un elemento en una posición especifica de la lista
print(numbers)  # se imprime la lista modificada


tasks = [ 'task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8', 'task9', 'task10' ] #se crea una lista con tareas

new = numbers + tasks #se crea una nueva lista que es la suma de las listas numbers y tasks
print(new) #se imprime la nueva lista
print(new.index('task2')) #se imprime la posición de la tarea task2 en la lista new

new.remove('task3') #se elimina la tarea task3 de la lista new, remove es una function que se usa para eliminar un elemento de la lista
print(new)

new.pop() #se elimina el ultimo elemento de la lista new, pop es una función que se usa para eliminar el ultimo elemento de la lista
print(new)

new.pop(0) #se elimina el primer elemento de la lista new, pop es una función que se usa para eliminar un elemento de la lista en una posición especifica
print(new)

new.reverse() #se invierte la lista new, reverse es una función que se usa para invertir la lista
print(new)

#-------------------------

numbers1 = [5,20, 56, 94, 8, 20, 46, 1, 100, 3]
numbers1.sort() #se ordena la lista numbers1, sort es una función que se usa para ordenar la lista
print(numbers1)

string = ['af','gt','fd','sa','ac','ds']
string.sort() #se ordena la lista string, sort es una función que se usa para ordenar la lista
print(string)

# new.sort() #en listas con datos con diferentes tipos de datos no se puede ordenar, da error
# print(new) #da error