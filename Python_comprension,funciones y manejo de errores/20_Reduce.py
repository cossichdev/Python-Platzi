#la función REDUCE nos permite reducir una lista y sacar una conclusion, en este caso un solo valor
#reduce toca importarlo por modulo

import functools #importamos el modulo functools

numbers = [0, 1, 2, 3, 4, 5] #lista de numeros, cual sumatoria da 15

def acumulador(counter, item): #La función "acumulador" recibe dos parametros
    print('counter->', counter) #este print sirve para ver la sumatoria del item con el resultado del mismo item mas item
    print('item->', item) #item se refiere a cada item de nuestra lista numbers
    return counter + item #retorna la sumatoria de ambas variables

result = functools.reduce(acumulador, numbers) #funcion reduce da la sumatoria en este caso

print(result)

#La función reduce() recibe como primer argumento una función que recibe dos argumentos, y como segundo argumento una lista. La función reduce() aplica la función que recibe como primer argumento entre cada elemento de la lista, y el resultado de la operación se aplica entre el siguiente elemento de la lista y el resultado anterior. La función reduce() devuelve el resultado de la operación entre todos los elementos de la lista.
#Si la lista contiene un solo elemento, la función reduce() devuelve ese elemento.
#Si la lista está vacía, la función reduce() devuelve un error.

# counter -> 0
# item -> 1
# counter -> 1
# item -> 2
# counter -> 3
# item -> 3
# counter -> 6
# item -> 4
# counter -> 10
# item -> 5
# 15
