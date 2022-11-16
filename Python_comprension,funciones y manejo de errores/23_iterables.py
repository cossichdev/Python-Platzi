#Hay otro tipo de iterables que se pueden controlar manualmente desde el codigo y no solo desde un ciclo
#nosotros ya hemos hechos iteraciones con range 

for iterable in range(0,11): #iterable es el nombre que le damos a la variable que va a tomar los valores de range
    print(iterable)


my_iter = iter(range(0, 11))  # iter es una funcion que convierte un objeto iterable en un iterador
print(my_iter)
print(next(my_iter)) #next es una funcion que devuelve el siguiente valor del iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) #cuando ya no hay mas datos en el iterador, lanza una excepcion

