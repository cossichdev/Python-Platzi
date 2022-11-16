#Proyecto: Condicionales-------------------------------
#Piedra, papel o tijera
#se importa la función random para que el computador elija una opción al azar

import random #se importa la función random para que el computador elija una opción al azar

#se definen las variables piedra, papel y tijera en una función
def choice(a): #se define la función choice, la cual recibe le parámetro a, que es la opción que elige el usuario
    if a == 1: #si a es igual a 1, entonces la opción del usuario es piedra
        return "piedra" #se retorna la opción piedra
    elif a == 2: #si a es igual a 2, entonces la opción del usuario es papel
        return "papel" #se retorna la opción papel
    elif a == 3: #si a es igual a 3, entonces la opción del usuario es tijera
        return "tijera" #se retorna la opción tijera


user1win = 0 #se crea una variable que se llama user1win y se le asigna el valor de 0, o sea empieza en 0
pcwin = 0 #se crea una variable que se llama pcwin y se le asigna el valor de 0, o sea empieza en 0
rondas = 1
totalrondas = 3

while True: #se crea un ciclo while para que el programa se repita

    print('*' * 40)
    print('Round', rondas, "de", totalrondas) #se imprime el numero de ronda
    print('*' * 40)

    print('I.A:', pcwin) #se imprime el numero de veces que gano el computador
    print('Usuario:', user1win)


    def play(): #función que se encarga de imprimir la opción del computador y la opción del usuario
        print(f'🧠 Has elegido: {choice(user1)}') #se imprime la opción que elige el usuario
        print(f'La I.A 🤖 eligió: {choice(pc)}') #se imprime la opción que el computador elogió

    print("Usuario 1, elige una opción: \n 1) piedra🪨 \n 2) papel🧻 \n 3) tijera✂️") #se imprime el menu de opciones
    pc = random.randint(1,3) #se crea una lista con las opciones que puede elegir el computador

    user1 = int(input("Ingrese el numero de tu opción: ")) #se usa input para que el usuario ingrese un numero

    rondas += 1 #se suma 1 a la variable rondas para que el programa sepa que es la siguiente ronda

    if rondas > totalrondas:
        totalrondas += 2 #se suma 1 a la variable total

    if pc == user1: #se compara la opción que elige el computador con la opción que elige el usuario
        print("Empate 🪢")
    elif (pc == 2 and user1 == 1) or (pc == 3 and user1 == 2) or (pc == 1 and user1 == 3): #se usa elif para que el programa compare las opciones elegidas por el usuario y el computador
        print("Gana la I.A 🤖")
        pcwin += 1
    elif user1 not in range (1,4): #not in es para que el programa sepa que si el usuario ingresa un numero que no esta en el rango, entonces se imprime un mensaje de error
        print("Opción invalida, nadie gana, elige bien la próxima vez 🐒")
    else:
        print("Ganaste 🧠")
        user1win += 1

    play() #se llama a la función play para que se imprima la opción del computador y la opción del usuario

    if pcwin == 3: #si pcwin es igual a 3, entonces el computador gana
        print("El torneo lo gano la I.A 🤖")
        break

    if user1win == 3: #si pcwin es igual a 3, entonces el computador gana
        print("El torneo lo ganaste tu 🧠!")
        break

