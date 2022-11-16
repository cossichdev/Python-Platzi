#los errores en python se manejan con la palabra reservada try, except y finally
try:  # en el bloque try va el codigo que puede lanzar una excepcion, este es un bloque para probar errores
    print(2 / 0)
except ZeroDivisionError: #except es un bloque que se ejecuta cuando el codigo del bloque try lanza una excepcion
    print('No se puede dividir entre 0')
except TypeError:
    print('No se puede dividir un string')
except:
    print('Otro error')
finally:
    print('Esto se ejecuta siempre')

# assert es una palabra reservada que sirve para verificar una condicion, si la condicion es falsa, lanza una excepcion
# assert es una palabra reservada que sirve para verificar una condicion, si la condicion es falsa, lanza una excepcion
# el bloque try except es util cuando no sabemos si el codigo va a lanzar una excepcion, pero si sabemos que puede lanzar una excepcion, lo mejor es usar assert
# assert se utiliza para verificar que se cumpla una condicion, por ejemplo, que un numero sea positivo, o que una variable sea un string, etc
# si la condicion es falsa, se lanza una excepcion

suma = lambda x,y:(x + y)
assert suma(2,2)==4#assertionerror se lanza cuando la condicion del assert es falsa

age = 10
if age <18:
    # raise sirve para #raise sirve para lanzar una excepcion, en este caso lanza una excepcion de tipo Exception
    raise Exception('No se permiten menores de edad')
    # raise Exception('Solo mayores de edad') #raise sirve para lanzar una excepcion, en este caso lanza una excepcion de tipo Exception con un mensaje





# #podemos crear nuestros propios errores con la palabra reservada raise
# 
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('No se puede dividir entre 0')
#     else:
#         return a / b
# 
# 
# print(divide(2, 0))
# 
# 
# #podemos crear nuestros propios errores con la palabra reservada raise
# 
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('No se puede dividir entre 0')
#     else:
#         return a / b
# 
# 
# print(divide(2, 0))
# 
# 
# #si queremos crear un error personalizado, podemos crear una clase que herede de Exception
# 
# class MyError(Exception):
#     def __init__(self, message, errors):
#         super().__init__(message)
#         self.errors = errors
# 
# 
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         raise MyError('Ha ocurrido un error', e)
# 
# 
# print(divide(2, 0))
# 
# 
# #podemos crear nuestros propios errores con la palabra reservada raise
# 
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('No se puede dividir entre 0')
#     else:
#         return a / b
# 
# 
# print(divide(2, 0))
# 
# 
# #si queremos crear un error personalizado, podemos crear una clase que herede de Exception
# 
# class MyError(Exception):
#     def __init__(self, message, errors):
#         super().__init__(message)
#         self.errors = errors
# 
# 
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         raise MyError('Ha ocurrido un error', e)
# 
# 
# print(divide(2, 0))
# 
# 
# #podemos crear nuestros propios errores con la palabra reservada raise
# 
# def divide(a,

