#las funciones sirven para reutilizar código, encerrándolo en algo llamado funciones para usar el bloque varias veces.

#siempre se usa la palabra clave "def"
#Dentro del paréntesis de la función, se ponen los parámetros que se van a usar en la función

def my_print(text): #definimos la función con el nombre "my_print"
    print(text * 2) # La función pide que se imprima "Hola mundo"

my_print("este es mi texto") #se llama a la función para que se ejecute
my_print("hola") #se llama a la función para que se ejecute


x = 2
y = 4
c = x + y #se puede usar la función para hacer operaciones y evitar escribir el código repetidamente

def suma (x, y): #la función suma pide dos parámetros (pueda pedir mas o menos)
    my_print(x + y) #la función suma imprime la suma de los dos parámetros

suma (4,6) #se llama a la función para que se ejecute y se le dan dos parámetros
suma (45,6)

#------------------------------------

def imprimir(): #la función print ya existe en python, pero se puede sobre escribir
    print("hola mundo")
