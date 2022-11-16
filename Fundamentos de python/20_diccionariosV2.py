person = {
    'name': 'John Smith',
    'last_name': 'Baker',
    'age': 30,
    'height': 1.75,
    'languages': ['English', 'Spanish', 'French'],#pueden haber listas dentro de diccionarios
    'code':
        {'python': 'intermediate',
        'java': 'beginner'
        }, #pueden haber diccionarios dentro de diccionarios
}

print(person) #se imprime la lista person

person['name'] = 'John Doe' #se cambia el valor de la llave name por John Doe
person['age'] = 31 #se cambia el valor de la llave age por 31
print(person)  # se imprime la lista person

person['languages'].append('German') #se agrega un nuevo valor a la lista languages,se maneja como una lista normal
person['code'] = {'python': 'advanced'} #se cambia el valor de la llave code por python advanced pero se borran los valores que tenia antes y solo queda python advanced en el diccionario
print(person)  # se imprime la lista person

del person['last_name'] #se borra la llave last_name y su valor,  función del para borrar
person.pop('age') #se borra la llave age y su valor, función pop para borrar
print(person)  # se imprime la lista person

#-----------------------------------

print('items') #genera una lista de tuplas con las llaves y valores del diccionario
print(person.items()) #se imprime la lista person con la función items. Items imprime las llaves y los valores

print('keys') #genera una lista con las llaves del diccionario
print(person.keys()) #se imprime la lista person con la función keys. Keys imprime solo las llaves

print('values') #genera una lista con los valores del diccionario
print(person.values()) #se imprime la lista person con la función values. Values imprime solo los valores
