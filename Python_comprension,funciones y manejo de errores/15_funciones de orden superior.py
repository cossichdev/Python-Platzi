#una función le podemos enviar otra función y ejecutarla desde allí

#----------función clásica
def increment(x): #función de increment recibe un parámetro
    return x + 1 #le aumentamos un, mas uno (1) y la operación la retornamos

print("1 normal:", increment(5))

#----
def High_order_function(x, func): #una función que recibe un parámetro (un numero) y el otro parámetro es otra es una función
    return x + func(x) # x mas el return que envíe la ejecución de la función "func" y la operación la retornamos
result = High_order_function(2, increment) #a increment no se le pone el paréntesis = ejecutar () por que daría error, entonces solo hay que enviar la definición de la función

print('2 normal:', result)
# el resultado seria: 2 +(2 + 1)

#-------------------------- ahora con lambda
increment2 = lambda x: x + 1 #variable con la función lambda para acortar pasos

result = increment2(5) #variable que contiene variable con la función lambda

print('1 lambda:', result)

#---

High_order_function2 = lambda x, func: x + func(x) #función lambda con dos parámetros, siendo uno uno una función 
result = High_order_function2(2, increment2)

print('2 lambda:', result)

#------------------------------------------------

#las funciones se pueden enviar casi de forma dinámica, definiéndolas dentro de las variables y enviar directamente una lambda

result = High_order_function2(2, lambda x: x + 1)
print('3 lambda:', result)
