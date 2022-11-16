#los diccionarios son como las listas pero en vez de tener un índice numérico tienen un índice alfanumérico, los diccionarios se crean con llaves y se separan los elementos con comas, los diccionarios se usan para guardar datos y poder manipularlos. Tambien se pueden usar para guardar datos de una base de datos.

my_dict = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 25} #se crea un diccionario con los datos de una persona
print(my_dict) #se imprime el diccionario
print(type(my_dict)) #se imprime el tipo de dato del diccionario

my_dict2 = {
    'nombre': 'Juan',
    'apellido': 'Alvarez',
    'edad': 35
} #los diccionarios también se pueden crear en varias líneas
print(my_dict2)

print(len(my_dict)) #se imprime la cantidad de elementos que tiene el diccionario

print(my_dict['nombre']) #se imprime el valor de la llave nombre

print(my_dict['edad']) #si no se encuentra la llave, se imprime un error
print(my_dict.get('edad')) #.get es un método que se usa para obtener el valor de una llave pero si la llave no existe, no arroja error, previene errores

print ('nombre' in my_dict)  #se imprime si la llave nombre existe en el diccionario, se imprime True o False

print ('hola' in my_dict) #si no existe la llave, se imprime False