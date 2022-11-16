#veremos de buscar por binarios (partiendo todo por la mitad)

objetivo = int(input("Escoge un entero: "))  # preguntar al usuario
epsilon = 0.001  # precision, que tan cerca quiero llegar a la respuesta
bajo = 0.0 # limite inferior
alto = max(1.0, objetivo)  # limite superior, funcion max regresa el valor mas alto entre dos valores
respuesta = (alto - bajo) / 2 # dividir entre dos el alto y bajo


while abs(respuesta ** 2 - objetivo) >= epsilon: # mientras el valor absoluto de mi respuesta al cuadrado - objetivo , sea mayor o igual a epsilon
    print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}") #ABRIR EL COFRE DEL PROGRAMA Y VER QUE PASA
    if respuesta ** 2 < objetivo: # si la respuesta al cuadrado es menor al objetivo, entonces bajo es nuestra nueva respuesta
        bajo = respuesta
    else:  # si la respuesta al cuadrado es mayor al objetivo, entonces alto es nuestra nueva respuesta
        alto = respuesta

    respuesta = (alto + bajo) / 2 #en cada iteracion estamos dividiendo entre 2 el espacio de busqueda y redefinimos que es alto y bajo para modificar la respuesta, y cambiamos para ir abajo o arriba

print(f'La raiz cuadrada del {objetivo} es {respuesta}')
