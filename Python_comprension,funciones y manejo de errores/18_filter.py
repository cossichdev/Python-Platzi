#la función filter sirve para filtrar elementos de una lista y seleccionarlos para pertenecer en una nueva lista.
#filtrar por una o las condiciones de los elementos de una lista

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = list(filter(lambda number: number % 2 ==0, numbers))
print(numbers)
print(new_numbers)

#creamos una lista donde aplicamos la función FILTER y le asignamos una función lambda, la cual con ayudara a pedirle a la variable NUMBERS, que nos devuelva cada numero o iterable que al dividirlo en dos su residuo sea 0

