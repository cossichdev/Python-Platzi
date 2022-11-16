#ciclo for es para repetir un código un numero determinado de veces, la diferencia con el ciclo while es que en el ciclo for se sabe cuantas veces se va a repetir el código y en el ciclo while no se sabe cuantas veces se va a repetir el código

for i in range(10): #se crea un ciclo for que se repetirá 10 veces, el numero 10 es el limite superior, o sea que el ciclo se repetirá 10 veces, el numero 10 no se incluye, o sea que el ciclo se repetira desde 0 hasta 9, i es una variable que se crea para que el ciclo se repita 10 veces y range es una función que crea una lista de números desde 0 hasta 9
    print("i=",i) #se imprime el valor de i, el ciclo se repetirá 10 veces, desde 0 hasta 9


for element in range(20): #range es una función que genera una lista de números, en este caso se genera una lista de números desde 0 hasta 19
    print("element=",element) #se imprime el valor de element, el ciclo se repetirá 20 veces, desde 0 hasta 19


for element2 in range(5,20): #range es una función que genera una lista de números, en este caso se genera una lista de números desde 5 hasta 19
    print("element2=",element2) #se imprime el valor de element, el ciclo se repetirá 15 veces, desde 5 hasta 19


list = [1,2,3,4,5,6,7,8,9,10] #se crea una lista que se llama list y se le asignan los valores de 1,2,3,4,5,6,7,8,9,10
for X in list: #se itera la lista list, o sea que se recorre la lista list y se imprime cada uno de los valores de la lista list
    print("X=",X) #se imprime el valor de X, el ciclo se repetirá 10 veces, desde 1 hasta 10

tupla = ('a','b','c','d','e','f','g','h','i','j') #se crea una tupla que se llama tupla y se le asignan los valores de a,b,c,d,e,f,g,h,i,j
for Y in tupla: #se itera la tupla tupla, o sea que se recorre la tupla tupla y se imprime cada uno de los valores de la tupla tupla
    print("Y=",Y) #se imprime el

dict = {'nombre':'Juan','apellido':'Perez','edad':20} #se crea un diccionario que se llama dict y se le asignan los valores de nombre:Juan,apellido:Perez,edad:20
for z in dict: #se itera el diccionario dict, o sea que se recorre el diccionario dict y se imprime cada uno de los valores de la diccionario dict
    print("z=",z) #se imprime la llave de Z, el ciclo se repetirá 3 veces, desde nombre hasta edad
    print("z1=",dict[z]) #dict[z] es para acceder al valor de la llave z, se imprime el valor de la llave z, el ciclo se repetirá 3 veces, desde Juan hasta 20
    print("z2", z, "=", dict[z]) #z es la llave y dict(z) es el valor de la llave z, el ciclo se repetirá 3 veces, desde nombre:Juan hasta edad:20

for key, value in dict.items(): #se itera el diccionario dict, o sea que se recorre el diccionario dict y se imprime cada uno de los valores de la diccionario dict
    print("z3", key, value) #key es la llave y value es el valor de la llave key, el ciclo se repetirá 3 veces, desde nombre:Juan hasta edad:20

#-----------------------------
#la mayoría de servidores devuelven la información en diccionarios o en listas de diccionarios, por lo tanto es muy común iterar diccionarios o listas de diccionarios

people =[
    {
        'name': 'Juan',
        'age': 20,
    },
    {
        'name': 'Pedro',
        'age': 30,
    },
    {
        'name': 'Maria',
        'age': 40,
    }
]
#los diccionarios pueden tener cualquier cantidad de llaves y valores, en este caso se tiene un diccionario o lista que se llama people y se le asignan 3 diccionarios, cada diccionario tiene 2 llaves y 2 valores, name:Juan,age:20,name:Pedro,age:30,name:Maria,age:40

for person in people: #se itera la lista people, o sea que se recorre la lista people y se imprime cada uno de los valores de la lista people
    print(person) #se imprime el diccionario person, el ciclo se repetirá 3 veces, desde name:Juan,age:20 hasta name:Maria,age:40
    print("name", "=", person['name']) #se pide el valor de la llave name del diccionario person, el ciclo se repetirá 3 veces, desde Juan hasta Maria