#Strings-----------------------------------

name = "Juan" 
Last_name = "Perez"
print(name + Last_name) #se puede sumar strings, si es un str hay que dejar espacio en blanco
print(name, Last_name) #se pueden imprimir varias variables en una sola línea

full_name = name + " " + Last_name #se puede guardar el resultado de una operación en una variable
print(full_name) #se imprime la variable, la cual contiene dos variables mas

quote = "I'm Juan Perez" #si estamos escribiendo en idioma ingles, este idioma usa apostrofes (comilla simple) para las contracciones, para que el string no devuelva error, se usan comillas dobles
print("v1)", quote)  # se imprime la variable

quote = 'I\'m Juan Perez' #para que el string no devuelva error, se usa la barra invertida para escapar el carácter
print("v3)", quote)  # se imprime la variable

quote_2 = "I'm \"Juan\" Perez" #para que el string no devuelva error, se usa la barra invertida para escapar el carácter
print("v3)", quote_2)  # se imprime la variable

quote_3 = "she said 'Juan' Perez" #para que el string no devuelva error, se usan comillas dobles
print("v4)", quote_3)  # se imprime la variable


#Format----
template = f"hola, mi nombre es {name} y mi apellido es {Last_name}" #se usa la llave para indicar que se va a reemplazar por una variable y siempre se pone la letra "f" antes de las comillas
print("v1)", template)  # se imprime la variable

template = "hola, mi nombre es {} y mi apellido es {}".format(name, Last_name) #se usa la llave para indicar que se va a reemplazar por una variable y .format() para indicar que se va a reemplazar por una variable en el orden que queremos los valores ".format(x, y, z)""
print("v2)", template)  # se imprime la variable


#Formato mas usado en la comunidad----
x = input("Dime tu nombre: ")
y = input("Dime tu apellido: ")
z = input("Dime tu edad: ")

print(f"hola, mi nombre es {x} y mi apellido es {y} y tengo {z} años") #se usa la llave para indicar que se va a reemplazar por una variable y siempre se pone la letra "f" antes de las comillas