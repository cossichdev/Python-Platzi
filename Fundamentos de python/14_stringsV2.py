#STRINGS RECARGADOS------------------------------------

text = 'El sabe programar en Python' #se crea una variable con un string
print('JavaScript' in text) # in se usa para saber si un elemento esta en una lista
print('Python' in text) #in se usa para saber si un elemento esta en una lista

if 'Python' in text: #if 'Python' in text: es una condición que se cumple si 'Python' esta en text
    print('Python is in the text') #si la condición se cumple, se imprime el mensaje

if 'JS' in text: #if 'JS' in text: es una condición que se cumple si 'JS' esta en text
    print('JavaScript is in the text') #si la condición se cumple, se imprime el mensaje
else: #si la condición no se cumple, se ejecuta el else
    print('JavaScript is not in the text') #se imprime el mensaje

size = len(text) #se crea una variable size que es igual a la longitud del string text
print(f'La variable tiene {size} caracteres') #se imprime la longitud del string text

print(text) #se imprime el string text
print(text.upper()) #se imprime el string text en mayúsculas, después del punto se pone upper para que el string se imprima en mayúsculas
print(text.lower()) #se imprime el string text en minúsculas, después del punto se pone lower para que el string se imprima en minúsculas
print(text.count("a")) #se imprime el numero de veces que aparece la letra a en el string text, después del punto se pone count para que el programa cuente las veces que aparece la letra a en el string text
print(text.swapcase()) #se imprime el string text con las letras mayúsculas en minúsculas y las letras minúsculas en mayúsculas, después del punto se pone swap Case para que el programa cambie las letras mayusculas por minusculas y viceversa
print(text.startswith("El")) #se imprime True si el string text empieza con la palabra El, después del punto se pone startswith para que el programa sepa que si el string text empieza con la palabra El, entonces se imprime True
print(text.endswith("JavaScript")) #se imprime False si el string text termina con la palabra JavaScript, después del punto se pone end swith para que el programa sepa que si el string text termina con la palabra JavaScript, entonces se imprime False
print(text.replace("Python","JavaScript")) #se imprime el string text con la palabra Python reemplazada por la palabra JavaScript, después del punto se pone replace para que el programa reemplace la palabra Python por la palabra JavaScript

text2 = 'este es el titulo'
print(text2)
print(text2.capitalize()) #se imprime el string text2 con la primera letra en mayúscula, después del punto se pone capitalize para que el programa cambie la primera letra del string text2 a mayuscula
print(text2.title()) #se imprime el string text2 con la primera letra de cada palabra en mayúscula, después del punto se pone title para que el programa cambie la primera letra de cada palabra del string text2 a mayuscula
print(text2.isdigit()) #se imprime False si el string text2 no es un numero, después del punto se pone isdigit para que el programa sepa que si el string text2 no es un numero, entonces se imprime False
print("4568".isdigit())


#ejercicio-----------------------
#transformar un input en minúsculos para no tener error en X programa

user = input("Ingrese Piedra, Papel o Tijera: ")
print(user)

lower = user.lower()
print(lower)