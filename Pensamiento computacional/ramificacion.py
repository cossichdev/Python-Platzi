# existen 3 formas de comparar lógicamente

#1)
#if <condición>:
#     <expresión>

if 3 > 2:
    print("opción 1")

# ----------------------------------------------------------------

#2)
#if <condición>:
#   <expresión>
# else:  si condición de arriba no es verdadera, te vas a la expresión de abajo
#     <expresión >

if 10 <= 9:
    print("opción 1")
else:
    print("opción 2")

# ----------------------------------------------------------------

#3) 
#if <condición>:
#   <expresión>
# elif <condición>:
    # <expresión>
# else:  si condición de arriba no es verdadera, te vas a la expresión de abajo
#     <expresión >

if 4 > 5:
    print("opción 1")
elif 5 < 4:
    print ("opción 2")
else:
    print("opción 3")

# ----------------------------------------------------------------

# ejercicio de la expresión

num_1 = int(input("Elige un numero: "))
num_2 = int(input("Elige otro numero: "))

if num_1 > num_2:
    print("numero 1 es mayor a numero 2")
elif num_1 < num_2:
    print("numero 2 es mayor a numero 1")
else:
    print("ambos son iguales")

# ----------------------------------------------------------------

# Tarea de la expresión
name_1 = (input("Como te llamas X ?: "))
name_2 = (input("Como te llamas Y ?: "))

age_1 = int(input(f"Cual es tu edad {name_1}: "))
age_2 = int(input(f"Cual es tu edad {name_2}: "))

if age_1 > age_2:
    print(f"{name_1} es mayor")
elif age_1 < age_2:
    print(f"{name_2} es mayor")
else:
    print(f"Ambos tienen la misma edad")
