#como podemos llamar otros modulos, usamos la palabra clave import


import utils  # importamos el archivo anterior de esta carpeta para ejecutarlo
import readCSV
import charts

def run():
    data = readCSV.read_csv('./app/data.csv')
    countries = list(map(lambda x: x['Country'], data ))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.pie_chart(countries, percentages)

'''
    country = input('Type a country: ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country) #esto retorna los valores, nombramos el archivo seguido de un punto
        charts.bar_chart(labels, values)
'''

    # print(result)

if __name__ == '__main__': #este if le dice al archivo que si es ejecutado desde la terminal que ejecute el metodo run y si es ejecutado desde otro archivo, no lo ejecute.
    run()