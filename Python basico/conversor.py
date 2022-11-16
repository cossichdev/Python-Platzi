
def conversor(tipo_moneda, valor_dólar):
    moneda = input("Cuantos " + tipo_moneda + " tienes? ")
    moneda = float(moneda)
    dólares = moneda / valor_dólar
    dólares = round(dólares, 2)
    dólares = str(dólares)
    print("Tienes $" + dólares + " dólares")

menu = """
Bienvenido al conversor de monedas 😊💲

1 - Quetzales
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opción = int(input(menu))

if opción == 1:
    conversor("quetzales",7.74)

elif opción == 2:
    conversor("pesos argentinos", 138.60)

elif opción == 3:
    conversor("pesos mexicanos", 20.14)

else:
    print ("Invalid opción")