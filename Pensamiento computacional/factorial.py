# def factorial (n):
#     """"Calcula el factorial de n.
#     n int > 0
#     returns n!
#     """
#     print(n)
#     if n == 1:
#         return 1

#     return n * factorial (n - 1)

# n = int(input("Escribe un numero entero: "))

# print(factorial(n))



def fibonacci (n):  #con lambda seria como= 
    #print(n)
    if n == 0 or n == 1:
        return 1
    #print(n)
    return fibonacci (n - 1) + fibonacci (n -2)

n = int(input("Escribe un numero entero: "))  # preguntar al usuario

print (f'El numero de fibonacci para {n} es {fibonacci(n)}  ')