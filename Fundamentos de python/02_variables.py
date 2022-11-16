#Tipos de datos----------------------------------------------------------------------------

#string o STR = cadena de texto
my_name = "Juan" #se puede usar comillas dobles o simples
my_name = 'Juan' #se puede usar comillas dobles o simples
print("my_name", my_name)
print(type(my_name)) #type es una función que dice que tipo de dato es la variable que se le asigna

#int = numero entero
my_age = 13
print("my_age", my_age)
print(type(my_age))

#float = numero decimal
my_score = 8.4 #se usa el punto para los decimales, este es un numero real
print("my_score", my_score)
print(type(my_score))

#boolean o bool = verdadero o falso
is_single = True #True es verdadero, False es falso, para booleanos siempre la primer letra va mayúsculo
print("is_single", is_single)
print(type(is_single))

#inputs
my_age = input("Dime tu edad: ") #al ingresar un input, el valor, aunque sea numero, lo devolverá como un String STR
print("my_age", my_age) #se imprime la edad que se le dio
print(type(my_age)) #se imprime el tipo de dato que es la variable