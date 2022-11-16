# #las funciones hacia los conjuntos son las siguientes:
# Funciones de set:

# .add(): Añade un elemento.

# .update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

# .discard(): Elimina un elemento y si ya existe no lanza ningún error.

# .remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

# .pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

# .clear(): Elimina todo el contenido del conjunto




set_countries = {'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela', 'Brasil', 'Paraguay', 'Uruguay', 'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela', 'Brasil', 'Paraguay', 'Uruguay'}

size = len(set_countries) #tamaño del conjunto, cuenta la cantidad de elementos del conjunto
print(size)

print("Colombia" in set_countries) #verifica si un elemento está en el conjunto")

#-add
set_countries.add("Panama") #agrega un elemento al conjunto
print(set_countries)

#update
set_countries.update({"Panama", "Costa Rica", "Honduras", "Nicaragua", "El Salvador", "Guatemala", "Belice"}) #agrega varios elementos al conjunto
print(set_countries)

#remove
set_countries.remove("Panama") #elimina un elemento del conjunto
print(set_countries)

# set_countries.remove("Guatem")  #no se puede eliminar un elemento que no existe en el conjunto, da error
set_countries.discard("Guatem") #elimina un elemento del conjunto, si no existe NO da error
print(set_countries)

set_countries.clear() #elimina todos los elementos del conjunto
print(set_countries)




