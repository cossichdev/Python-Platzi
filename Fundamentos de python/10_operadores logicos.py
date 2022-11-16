#and + or ----------------------------------

x = 1
y = 2

print(x == 1 and y == 2) #se usa la función "and" para saber si las dos condiciones son verdaderas y dará verdadero porque x es igual a 1 y y es igual a 2
print(x == 2 and y == 2) #dará falso porque la primera condición es falsa
print(x == 1 or y == 3) #se usa la función "or" para saber si una de las condiciones es verdadera y dará verdadero porque la primera condición es verdadera
print(x == 2 or y == 3) #dará falso porque ninguna de las condiciones es verdadera

stock = int(input("Ingrese el stock: ")) #se usa int para convertir el input en entero
print(stock >= 100 and stock <= 1000)

role = input("Ingrese el rol: ") #se usa input para que el usuario ingrese el rol
print(role == "admin" or role == "user") #se usa la función "or" para saber si una de las condiciones es verdadera