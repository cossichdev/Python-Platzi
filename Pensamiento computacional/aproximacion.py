#veremos de buscar raices cuadradas aproximadas

objetivo = int(input("Escoge un entero: "))  # preguntar al usuario
epsilon = 0.1  # precision, que tan cerca quiero llegar a la respuesta
paso = epsilon ** 2  # que tanto nos vamos a acerar en cada iteracion
respuesta = 0.0 #tendra la respuesta luego de las iteraciones 


# mientras la respuesta al cuadrado sea menor al objetivo, aumentamos la respuesta mas uno (x+1)
while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:  #primer condicion es para acercarse mas al objetivo y la segunda es para evitar numeros negativos y que se pase del objetivo
    print(abs(respuesta ** 2 - objetivo), respuesta ) # aqui miramos que pasa dentro del programa
    respuesta += paso  # cada iteracion ser le suma el paso

# si la respuesta al cuadrado es igual al objetivo, imprimimos...
if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del {objetivo}')

else:  # si no, de lo contrario decimos que...
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')
