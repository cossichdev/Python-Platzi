#nombre para identifacr

def get_population(country_dict): #funcion para pedir la poblacion de un pais
    population_dict = {
        '2022':int(country_dict['2022 population']),
        '2020':int(country_dict['2020 population']),
        '2015':int(country_dict['2015 population']),
        '2010':int(country_dict['2010 population']),
        '2000':int(country_dict['2000 population']),
        '1990':int(country_dict['1990 population']),
        '1980':int(country_dict['1800 population']),
        '1970':int(country_dict['1700 population'])
    }
    # keys = ['col','bol'] #llave de pais (conjunto)
    # values = [300,400] #valores poblacion (conjunto)
    labels = list(population_dict.keys()) #llave de pais (conjunto)
    values = list(population_dict.values()) #valores poblacion (conjunto)
    return labels, values  # retornan las variables

A = 'Hola'

def population_by_country(data, country): #recivo una informacion que recive diccionarios adentro y tendran data y country
    result = list(filter(lambda item : item['Country'] == country, data)) # recibo una lista con informacion y busco uno especifico
    return result
