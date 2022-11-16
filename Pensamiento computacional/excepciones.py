
def dividelista(lista, divisor): #funcion que recibe dosparametros
    try:
        return [indice / divisor for indice in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista
    #va a tratar de dividir y si se divide dentro de 0 va a regresar la lista original

lista = list(range(10))
divisor = 0

print(dividelista(lista, divisor))