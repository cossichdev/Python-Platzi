#transforma los diferentes tipos de datos a otros datos-----------------------------------
name = "Juan"
print(type(name)) #se usa la función "type" para saber que tipo de dato es la variable

name = 12
print(type(name))

name = 12.5
print(type(name))

name = True
print(type(name))

age = 12
print(f"mi edad es: {age}") #se usa la función "f" para imprimir el resultado de la variable
print("mi edad es: " + str(age)) #se usa la función "str" para convertir el numero en un string

age = input("Dime tu edad: ")
print(type(age)) #esta variable es un string
print(f"Tu edad en 10 años sera: {int(age) + 10}") #se usa la función "int" para convertir el input en un numero entero
