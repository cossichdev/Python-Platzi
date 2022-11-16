# los ciclos son para repetir una acción o código varias veces hasta que se cumpla una condición o se llegue a un limite
#while es un ciclo que se repite mientras se cumpla una condición y for es un ciclo que se repite un numero determinado de veces

# while True: #while significa 'mientras' y si no se ponen condiciones, el código se repetirá infinitamente
    # print("hola")


counter = 0 #se crea una variable que se llama counter y se le asigna el valor de 0, o sea empieza en 0

while counter < 10: #se crea un ciclo while que se repetirá mientras la variable counter sea menor a 10
    counter += 1 #se le suma 1 a counter cada vez que se repite el ciclo, o sea que counter empieza en 0 y se le suma 1 hasta que llegue a 10
    print("counter=",counter) #se imprime el valor de counter, al llegar a 10, el ciclo se detiene


x = 0

while x < 20:
    x += 1
    if x == 15: #si x es igual a 15, entonces se rompe el ciclo y se continua con el código que sigue
        break #break es para que el ciclo se detenga forzosamente
    print("x=",x)

y = 0

while y < 20:
    y += 1
    if y < 15: #si y es menor a 15, entonces se continua con el ciclo
        continue #continue es para que el ciclo se detenga y se continue con el siguiente ciclo
    print("y=", y) #se imprime desde el valor de y que es 15 hasta el valor de y que es 20
