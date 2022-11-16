#Floot-----------------------------------

x = 1.1
y = 2.2
z = 3.3

print (x + y + z) #se puede usar la variable para hacer operaciones
print (x + y + z == 6.6) #se puede usar la variable para hacer operaciones
print (z)
print (x + y)
print (z == x + y) #dará falso porque la suma de x + y no es igual a z, debido a que la suma de x + y es 3.3000000000000003 y z es 3.3

x_str = format(x, '.2g') # se usa la función "format" para redondear el numero a 2 decimales
y_str = format(y, '.2g') #.2g es para redondear a 2 decimales
z_str = format(z, '.2g')

print(x_str)
print(type(x_str))
print(y_str + z_str + x_str) #se puede usar la variable para hacer operaciones
print (z_str == x_str + y_str) #dará falso porque la suma de x_str + y_str no es igual a z_str, debido a que la suma de x_str + y_str es 3.3 y z_str es 3.3

tolerancia = 0.00001
print(abs((x+y)-z)< tolerancia) #se usa la función "abs" para saber el valor absoluto de la resta de x - y) y se usa la función "<" para saber si el valor absoluto es menor a la tolerancia y dara verdadero