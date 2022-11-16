#funcion que se llama inicial y lo que hace es que recibe una lista y toma las primeras letras y regresa una lista llamada iniciales

def inicial(lista):
    iniciales = []
    
    for palabra in lista:
        try:
            assert type(palabra) == str, f"{palabra} no es un string"
            assert len(palabra) > 0, "No se permiten strings vacios"
            iniciales.append(palabra[0])
        except AssertionError as e:
            print(e)

    return iniciales



palabras = ["angelo", "4521", "Hola", 45, True, ""]
print("Las primeras letras son: " , inicial(palabras))