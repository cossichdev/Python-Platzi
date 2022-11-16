#veremos de buscar raíces cuadradas exactas

objetivo = int(input("Escoge un entero: ")) #preguntar al usuario
respuesta = 0 #generar una respuesta inicial con valor inicial

while respuesta ** 2 < objetivo: #mientras la respuesta al cuadrado sea menor al objetivo, aumentamos la respuesta mas uno (x+1)
        print(respuesta) #aquí miramos que pasa dentro del programa
        respuesta += 1 #empieza a probar desde el 0, multiplicando por el mismo y trata de encontrar el numero objetivo, al pasarse del objetivo se detiene

if respuesta ** 2 == objetivo: #si la respuesta al cuadrado es igual al objetivo, imprimimos...
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

else: # si no, de lo contrario decimos que...
    print(f'{objetivo} no tiene raíz cuadrada')
# ----------------------------------------------------------------
