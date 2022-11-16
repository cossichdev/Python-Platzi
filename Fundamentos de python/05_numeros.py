#Numbers-----------------------------------

lives = 3
print(type(lives)) #se usa la función "type" para saber que tipo de dato es la variable
age = 12
budget = 100
temperature = 36.5
print(type(temperature)) #se usa la función "type" para saber que tipo de dato es la variable

lives = 12 + 15
print(lives)

lives = lives -1 #se puede usar la variable para hacer operaciones
print(lives)

lives -= 1 #se puede usar la variable para hacer operaciones, en este caso una sustracción
print(lives)

lives += 2 #se puede usar la variable para hacer operaciones, en este caso una suma
print(lives)

number1 = 4000000000000000000000.1 #se puede usar números muy grandes
print(number1) #este print dará la notación científica, ya que el numero es muy grande

number2 = 0.0000000000000000000004 #se puede usar números muy peque;os
print(number2) #este print dará la notación científica, ya que el numero es muy peque;o

#reto-----------------------------------
#crear un programa que calcule el promedio de gastos mensual

x = input("Dime el primer gasto: ")
y = input("Dime el segundo gasto: ")
z = input("Dime el tercer gasto: ")

promedio = round(((int(x) + int(y) + int(z)) / 3),2) #se usa la función "int" para convertir el input en un numero entero y round para redondear el numero a 2 decimales
print("El promedio de gastos es: ", promedio)
print(f'El promedio de gastos es: {promedio}') #se usa la función "f" para imprimir el resultado de la variable
