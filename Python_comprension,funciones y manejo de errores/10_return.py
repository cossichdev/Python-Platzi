#creamos una función, la cual recibe dos parámetros

def sumrange(min, max): #función con dos parámetros
    print(min, max) #imprimimos el valor de min
    suma = 0  #variable con valor cero
    for x in range (min, max): #ciclo for con variable x que esta en rango min y max
        suma += x #suma de la variable suma mas x
    return(suma) #retorna la suma

result = sumrange(1, 10) #variable result que llama a la función sumrange con parámetros 1 y 10
print("result: ", result)
result2 = sumrange(result, result + 10) #llamamos a la función sumrange con los parámetros result y result + 10
print("result2: ", result2)