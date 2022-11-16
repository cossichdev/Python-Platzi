#las sintaxis de listas por comprensión son muy útiles para crear listas, pero también se pueden usar para crear diccionarios y conjuntos.
#las lists_comprehension se leen como: "para cada elemento en una secuencia, hacer algo con ese elemento", por ejemplo:
#[elemento for element in iterable = elemento es el elemento que se va a agregar a la lista, iterable es la secuencia que se va a iterar, y el elemento se agrega a la lista.


#--------------------------------------------------------------------------------------
numbers = [] #se crea una lista vacía para agregar
for element in range(10): #se crea un ciclo for para agregar los números del 0 al 9
    numbers.append(element * 2) #se agrega cada elemento a la lista

print("1", numbers) #se imprime la lista
#--------------------------------------------------------------------------------------

# Para crear una lista se necesitaron 3 líneas de código pero se puede sintetizar a solo una línea de código con listas por comprensión

numbers2 = [element * 2 for element in range(10)] #se crea una lista con los números del 0 al 9, la lista se lee así: "para cada elemento en la secuencia, hacer algo con ese elemento", en este caso se multiplica por 2 cada elemento de la secuencia

print("2", numbers2) #mismo resultado que la lista anterior pero en una sola línea de código

#--------------------------------------------------------------------------------------

#se puede agregar una condición a la lista por comprensión, por ejemplo:

#lista normal:
number3 = []
for element in range(10):
    if element % 2 == 0:
        number3.append(element * 2)
print("3", number3)

#lista por comprensión:

number4 = [element * 2 for element in range(10) if element % 2 == 0] #se agrega una condición al final de la lista por comprensión, la lista se lee así: "para cada elemento en la secuencia, hacer algo con ese elemento, si se cumple una condicion", en este caso se multiplica por 2 cada elemento de la secuencia si el elemento es par
print("4", number4)

#--------------------------------------------------------------------------------------
