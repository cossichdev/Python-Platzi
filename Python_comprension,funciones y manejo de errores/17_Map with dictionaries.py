# Map con listas mas complejas: diccionarios
#
#Que pasa si tengo una lista la cual contiene items como diccionarios

items = [
    {
    'Product': 'camisa',
    'Price': 100
    },
    {
    'Product': 'Pantalón',
    'Price': 300
    },
    {
    'Product': 'suéter',
    'Price': 200
    }
]
# y yo solo quiero obtener una lista devuelta con los precios...
prices1 = [100, 300, 200]


#Eso lo podemos obtener con la función MAP:
#creando una variable "precio", la cual le asignamos la reacción de una lista, seguido de MAP y después la función

prices = list(map(lambda element: element['Price'], items ))
print(items)
print(prices)

#Ahora queremos agregar un nuevo item a nuestros diccionarios, el cual sera "taxes", para esto se puede usar la misma función map para transformar, como la función lambda necesita ser escrita en una línea y al querer agregar un nuevo item se deben de escribir dos líneas, necesitamos crear una función para hacer ese trabajo

def add_taxes(item):
    new_item = item.copy() #esta línea es importante ya que creamos una nueva variable (copia) con la información del diccionario original, con la función .copy()
    new_item['taxes'] = new_item ['Price'] * 0.19 
    return new_item

new_item = list(map(add_taxes, items))
print("Old list")
print(items)
print("New List")
print(new_item)

#al modificar un atributo en un diccionario, hay que tener cuidado para seguir respetando el array original u no modificarlo para no tener problemas futuros

#Por que ocurre este cambio, por la referencia en memoria, cuando se hacen operación con números primitivos, se calcula un nuevo valor y se asigna un nuevo valor, pero al hacerlo con diccionarios, este se asigna directamente en memoria por lo que se modifican ambos arrays ya que comparten misma referencia en memoria
