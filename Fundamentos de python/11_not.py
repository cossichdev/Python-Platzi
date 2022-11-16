#Not ----------------------------------

x = 1
y = 2

print(not(x == 1 and y == 2)) #se usa la función "not" para negar la condición y dará falso porque x es igual a 1 y y es igual a 2
print(not(x == 2 and y == 2)) #dará verdadero porque la primera condición es falsa
print(not(x == 1 or y == 3)) #se usa la función "not" para negar la condición y dará falso porque la primera condición es verdadera
print(not(x == 2 or y == 3)) #dará verdadero porque ninguna de las condiciones es verdadera

stock = int(input("Ingrese el stock: "))
print(not(stock >= 100 and stock <= 1000)) #se usa la función "not" para negar la condición y dará falso porque el stock es mayor o igual a 100 y menor o igual a 1000

role = input("Ingrese el rol: ")
print(role == "admin" or role == "user")