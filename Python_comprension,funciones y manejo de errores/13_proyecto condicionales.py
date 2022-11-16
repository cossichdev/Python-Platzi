#como buena practica de las funciones es necesario que cada función solo haga lo que se le pide y no haga de mas.
# toda función debe ir por bloques
#Trabajaremos el código de la clase pasada y lo reestructuraremos (refactorización) para dejarlo mas estético y comprensible.

import random  #se importa el modulo random para que la pc elija aleatoriamente

def opciones(): #la función "opciones" agarra el valor dado en consola, en numero entero y lo asigna al usuario y uno aleatorio al pc
    pc = random.randint(1, 3) #se usa el modulo para asignar un numero a la pc
    print("Usuario, elige una opción: \n 1) piedra🪨 \n 2) papel🧻 \n 3) tijera✂️") #opciones al usuario en consola
    user1 = int(input("Ingrese el numero de tu opción: ")) #Ingreso de variable desde consola
    print(f'🧠 Has elegido: {opciones_convertir(user1)}') #impresión de elección del usuario
    print(f'La I.A 🤖 eligió: {opciones_convertir(pc)}') #impresión de elección de la pc
    return pc, user1 # retorna el valor a la función.


def opciones_convertir(a): #nuestra función  "opciones_convertir" agarra la variable dada a la función "opción" y la convierte a variable texto para poder trabajar tanto en el retorno de la consola como en el código
    if a == 1: #numero asignado a la variable
        return "piedra"
    if a == 2:  # numero asignado a la variable
        return "papel"
    if a == 3:  # numero asignado a la variable
        return "tijera"


def reglas(pc, user1,pcwin,user1win,empate): #función con 4 variables asignadas, la cual da los lineamientos o condicionales para ganar y perder
    if pc == user1:
        print("Empate 🪢")
        empate += 1
    elif (pc == 1 and user1 == 3) or (pc == 2 and user1 == 1) or (pc == 3 and user1 == 2):
        print("Gana la I.A 🤖")
        pcwin += 1 #conteo de ganada por parte de la pc
    elif user1 not in range(1, 3):
        print("Opción invalida, nadie gana, elige bien la próxima vez 🐒")
    else:
        print("Ganaste 🧠")
        user1win += 1
    return user1win, pcwin, empate #retorna únicamente los valores de interés, siendo las partidas ganadas por cada usuario


def ejecutar (): #función que ejecuta el juego
#variables dadas al juego:
    user1win = 0
    pcwin = 0
    empate = 0
    rondas = 1
    totalrondas = 3

    while True: #Las instrucciones de la ejecución del programa van para abajo y van citando funciones, de las cuales al terminar, siguen su recorrido para abajo.
        print('*' * 40)
        print('Round', rondas, "de", totalrondas)  # se imprimen las variables dadas al juego
        print('*' * 40)
        print('Marcador')
        print('I.A:', pcwin)  # se imprime el numero de veces que gano el computador
        print('Usuario:', user1win)
        print('Empates:', empate)
        print('')

        pc, user1 = opciones() #se ejecuta el bloque de código para ambas variables y se traen sus respuestas
        user1win, pcwin, empate = reglas(pc, user1, pcwin, user1win, empate) #se ejecuta el bloque de código para ambas variables y se traen sus respuestas

        rondas += 1 #variable que se va modificando conforme se ejecute eel juego

        if rondas > totalrondas: #si el numero de rondas pasa el total de rondas asignado se:
            totalrondas += 2 #suman 2 rondas para desempatar

        if pcwin == 3: #victorias necesarias para ganar
            print("El torneo lo gano la I.A 🤖")
            break #se detiene el juego

        if user1win == 3:  # victorias necesarias para ganar
            print("El torneo lo ganaste tu 🧠!")
            break  # se detiene el juego
ejecutar() #se ejecuta el bloque de código