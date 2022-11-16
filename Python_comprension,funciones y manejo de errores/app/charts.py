import matplotlib.pyplot as plt #importa,mos la libreria que permite graficar y piplot en conjunto con un alias plt

def bar_chart(labels, values): #funcion para generar la grafica donde recibimos los lables y values de manera dinamica
    fig, ax = plt.subplots()  # fig sirve para definir la figura y ax para definir los ejes
    ax.bar(labels, values)#gse define el tipo de grafica, en este caso de barras
    plt.show()#mostramos el grafico

def pie_chart(labels,values):#funcion para generar la grafica donde recibimos los lables y values de manera dinamica
    fig, ax = plt.subplots()# fig sirve para definir la figura y ax para definir los ejes
    ax.pie(values, labels=labels, autopct='%1.1f%%')#gse define el tipo de grafica, en este caso de pie y definimos las labels 
    ax.axis('equal') #centrar la grafica
    plt.show()#mostramos el grafico

# Path: app\main.py
if __name__ == "__main__": #si el archivo es ejecutado directamente ejecutamos la funcion
    labels = ['a','b','c']#definimos las etiquetas
    values = [1,4,2]#definimos los valores
    bar_chart(labels, values) #ejecutamos la funcion bar_chart
    pie_chart(labels, values)
