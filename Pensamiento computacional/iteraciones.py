# bucles

#1) while = mientras

#while <condición>:
#     <expresión>
contador = 0

while contador <= 10:
    print (contador)
    contador += 1 #esta linea es igual a contador = contador x1


# ----------------------------------------------------------------

#2) loops dentro de loops; bucles, funciona como un reloj

#while <condición>:
#     <expresión>
contador_1 = 0
contador_2 = 0

while contador_1 < 5:
    while contador_2 < 6:
        print(contador_1, contador_2)
        contador_2 += 1
        if contador_2 >=3:
            break #cuando el contador_2 sea menor a 3 nos vamos a salir del bucle 2
    contador_1 += 1 #se maneja afuera debido a que, cuando el contador_2 llega al break, deja continuar al contador_1
    contador_2 = 0