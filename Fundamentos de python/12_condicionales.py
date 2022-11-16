#if----------------------------------

if True: #siempre trabajan con booleanos
    print("Si se ejecuta") #mueve el código a la derecha para que se sepa que esta dentro del if

if False: #siempre trabajan con booleanos
    print("No se ejecuta") #nunca se ejecuta porque el if es falso

pet = input("Ingrese la mascota: ") #se usa input para que el usuario ingrese la mascota
if pet == "perro": #se usa la función "==" para saber si la mascota es igual a perro
    print("Genial, tienes un buen gusto") #si la mascota es igual a perro se ejecuta este print
elif pet == "gato": #se  usa elif para que se ejecute si la primera condición es falsa
    print("Espero tengas suerte") #si la mascota es igual a gato se ejecuta este print
elif pet == "pez": #se  usa elif para que se ejecute si la primera condición es falsa
    print("Espero que no se te muera") #si la mascota es igual a pez se ejecuta este print
else: #se usa else para que se ejecute si ninguna de las condiciones anteriores es verdadera
    print("No me gusta esa mascota") #si ninguna de las condiciones es verdadera se ejecuta este print

#if stock----------------------------------
stock = int(input("Ingrese el stock: ")) #se usa int para convertir el input en entero

if stock >= 100 and stock <= 1000: #se usa if para saber si el stock es mayor o igual a 100 y menor o igual a 1000
    print("El stock es correcto") #si el stock es mayor o igual a 100 y menor o igual a 1000 se ejecuta este print
else: #si no se cumple la condición del if se ejecuta el else
    print("El stock no es correcto") #si el stock no es mayor o igual a 100 y menor o igual a 1000 se ejecuta este print

#if ejercicio----------------------------------
#programa que evalúe si un programa es par o impar

x = int(input("Ingrese un numero: ")) #se usa int para convertir el input en entero
if x % 2 == 0: #se usa if para saber si el numero es par y se divide entre 2 y el resto es 0
    print(f"modulo: {x % 2}") #si el numero es par se ejecuta este print
    print(f"{x} es par") #si el numero es par se ejecuta este print
else: #si no se cumple la condición del if se ejecuta el else
    print(f"{x} es impar") #si el numero no es par se ejecuta este print