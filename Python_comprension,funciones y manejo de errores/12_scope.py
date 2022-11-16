#scope significa alcance y se divide en 4, que van de mayor a menor:

# built in = función que esta predefinida en python
# global scope = variable que existe en todo el programa
# enclosing scope = función que esta dentro de otra función
# local scope = variable que solo existe dentro de la función

price = 100 #variable global con alcance global

def increment():
    price = 200 #variable local con alcance local
    result = price + 10 #variable local con alcance local
    print(result)
    return result

print(price) #imprime la variable global
price2 = increment() #imprime la variable local
print(price2) #imprime la variable local
# print(result) #esta variable no podrá ejecutarse debido a que es una variable que solo puede ser usada en la función increment, a menos que se creara una variable global
