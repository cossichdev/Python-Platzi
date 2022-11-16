#los ciclos anidados son ciclos que se encuentran dentro de otros ciclos y sirven para que el programa se repita varias veces

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] #se crea una matriz de 3x3, una lista dentro de otra lista


print(matriz[0]) # se imprime la primera lista
print(matriz[0][0]) #se imprime el primer elemento de la primera lista
# print(matriz[3][2]) # se imprime el tercer elemento de la cuarta lista, esto da error porque no existe la cuarta lista print(matriz[3][2])
print(matriz[2][2]) #se imprime el tercer elemento de la tercera lista

for fila in matriz: #se crea un ciclo for para que se imprima cada lista
    print(fila) #se imprime cada lista
    for columna in fila: #se crea un ciclo for para que se imprima cada elemento de cada lista
        print(columna) #se imprime cada elemento de cada lista

