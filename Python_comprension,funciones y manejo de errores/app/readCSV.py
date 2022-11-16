import csv #el modulo nativo csv sirve para manejar estos archivos

def read_csv(path): #funcion para leer archivo y recibimos su ubicacion
    with open(path, 'r') as csvfile:  #permiso de lectura
        reader = csv.reader(csvfile, delimiter=',') #leer el archivo e indica que delimitador usa el archivo
        for row in reader: #iteramos al final de cada linea
            print("***" * 5)
            print(row)

if __name__ == '__main__':
    read_csv('./app/data.csv')