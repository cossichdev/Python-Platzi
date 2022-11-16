x = int(input("Ingrese la altura (cm): ")) #pedimos al usuario que ingrese la altura
y = int(input("Ingrese la base (cm): ")) #pedimos al usuario que ingrese la base
# pedimos al usuario que ingrese la profundidad
z = int(input("Ingrese la profundidad (cm): "))

def volumen(altura = 1, ancho = 1, profundidad = 1): #función con 3 parámetros, en caso no reciba parámetros, se le asigna 1 a cada uno
    return altura * ancho * profundidad #retorna el producto de los 3 parámetros

result = volumen (x, y, z) #llamamos a la función volumen e ingresamos los parámetros, Tambien la asignamos a una variable nueva

print(f'El volumen es de {result} cm cúbicos!') #se imprímela función con los parámetros