#función Map: su función principal es hacer transformaciones a una lista dada de elementos

#digamos que tenemos una lista de elementos [vaca, pollo, maíz, papa] y queremos transformar esos elementos, al pasarlo por una función, en este caso llamada "def cocinar()", al cocinarlos podríamos tener el resultado con los elementos del array transformados.

# Lo importante es tener una lista con el mismo numero de elementos transformados

#--------------------ejemplo con transformación normal---------------
numbers = [1, 2, 3, 4, 5] #lista con números
numbers2 = [] # lista 2 vacía que vamos a darle la lista transformada

for elemento in numbers: #iteramos para transformar
    numbers2.append(elemento * 2) #agregamos con ".append" cada elemento multiplicado por 2

print(numbers)
print(numbers2)

# --------------------ejemplo con transformación MAP y lambda---------------
#pasamos de 3 líneas de código a una


numbers3 = list(map(lambda element: element * 2, numbers)) #esto se lee así: dentro de una lista, usamos la función map la cual le podemos agregar una función lambda donde le damos un iterable y le pedimos que a cada elemento le multipliquemos por 2 de la lista numbers.

#De la lista numbers, agarramos cada elemento y lo multiplicamos por 2, usando una función lambda dentro de una función map dentro de una lista.

print(numbers3)

#--------------------------------------------

numbers4 = [1, 2, 3, 4, 5]
numbers5 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers4, numbers5)) #al trabajar con dos listas, siempre se va a predominar la lista con menor numero de elementos 

print(result)

