### Escribir archivos en python
### Ejemplo 1
# Abrir un archivo
# f = open(file, mode)
# file: Nombre del archivo
# mode: Modo de apertura del archivo
# r: Solo lectura
# w: Solo escritura
# a: Añadir al final
# r+: Lectura y escritura
# w+: Escritura y lectura (reemplaza)
# a+: Añadir y lectura
# b: Modo binario
# t: Modo texto
# +: Actualizar

with open('./text.txt', 'w+') as file:  # se abre el archivo con with y se cierra automaticamente
    for line in file:  # se puede iterar por cada linea
        print(line)  # imprime cada linea
    file.write('Nuevas cosas en este archivo \n') #la funcion write es para escribir en el archivo
    file.write('segunda linea \n') #se agrega un salto de linea
    file.write('tercera linea \n') #se agrega un salto de linea
