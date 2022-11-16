#archivo para leer texto
'''
file = open('./text.txt') #funcion open mas la ruta del archivo
# print(file.read())  # imprime el texto completo
# print(file.readline()) # imprime la primera linea

#el texto siempre hay que cerrarlo debido a que ocupa mucha memoria
#se cierra con:
# file.close()

#se puede iterar 

for line in file:  # se puede iterar por cada linea
    print(line)  # imprime cada linea

file.close()
'''

#se puede usar el with para no tener que cerrar el archivo-----------------------
with open('./text.txt') as file: #se abre el archivo con with y se cierra automaticamente
    for line in file:  # se puede iterar por cada linea
        print(line)  # imprime cada linea
# Path: 26_files.py
#archivo para leer texto
#se puede iterar