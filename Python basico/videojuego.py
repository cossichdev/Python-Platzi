import random


def run():
    aleatorio = random.randint(0, 100)
    elegido = int(input("Elige un numero del 1 al 100: "))
    while elegido != aleatorio:
        if elegido < aleatorio:
            print("Elige un numero mayor")
        else:
            print("Elige un numero menor")
        elegido = int(input("Elige otro numero del 1 al 100: "))
    print("Ganaste")



if __name__ == '__main__':
    run()