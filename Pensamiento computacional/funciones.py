# # funciones

# # def nombre (parámetros):
# #     <cuerpo>
# #     return <expression>

# def suma (a, b): # nombre de función y la función recibe parámetros
#     total = a + b #cuerpo de la función
#     return total #

# suma (2, 3) #para ejecutar la función la nombramos

# print (suma)


#################################################### opción 1

def enumeración(objetivo):
    respuesta = 0

    while respuesta ** 2 < objetivo:
        print (respuesta)
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')

    else:
        print(f'La raíz cuadrada de {objetivo} no tiene respuesta, intente el método (2) o (3)')

###################################################opción 2
def aproximación(objetivo):
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta ** 2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada del {objetivo}')

    else:  # si no, de lo contrario decimos que...
        print(f'La raíz cuadrada del {objetivo} es {respuesta}')

################################################ opción 3
def binario(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto - bajo) / 2


    while abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return print(f'La raíz cuadrada del {objetivo} es {respuesta}')

#############################################  inicio código

objetivo = int(input("Escoge un numero entero: "))  # preguntar al usuario

print(f'Elige una opción para hallar la raíz cuadrada \n (1) Enumeración exhaustiva \n (2) Aproximación de soluciones \n (3) Búsqueda binaria')

algoritmo = int(input("Escoge un método por su numero: "))  # preguntar al usuario

if  algoritmo == 1:
    enumeración(objetivo)
elif algoritmo == 2:
    aproximación(objetivo)
elif algoritmo == 3:
    binario(objetivo)
else:
    print('Elija 1, 2 o 3')
