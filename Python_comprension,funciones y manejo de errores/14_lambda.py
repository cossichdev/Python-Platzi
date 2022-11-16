#la función lambda permiten gran versatilidad a la hora de declarar las funciones:

#------------------------------
# Función básica:
def increment(a):  
    return a + 1

print(increment(5))

#------------------------- función lambda
increment2 = lambda x: x + 1 #la primer X es el argumento de entrada, seguido de la salida
result = increment2(5)

print(result)


#------------------------- función lambda con dos argumentos

full_name = lambda name, lastname: f"Tu nombre completo es {name.title()} {lastname.title()}" #la función se lee: mi variable "full name" posee una función lambda la cual tiene 2 argumentos, siendo "name" y "last name", siempre hay que poner luego de los dos puntos(:) lo que se quiere hacer con los argumentos

text = full_name("glauco", "cossich") #mi variable texto agarra la variable "full name" y asigna sus valores en el orden de los argumentos dados
print(text) #imprimir variable que tiene asignada la variable con función lambda

#--------------------------