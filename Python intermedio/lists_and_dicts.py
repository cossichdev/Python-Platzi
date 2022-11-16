def run ():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname": "Glauco", "lastname": "Cossich"}

    super_list = [
        {"firstname": "Glauco", "lastname": "Cossich"},
        {"firstname": "Turi", "lastname": "Ochoa"},
        {"firstname": "Julio", "lastname": "Lemus"},
        {"firstname": "Diana", "lastname": "Oliva"},
        {"firstname": "Sergio", "lastname": "Contreras"}
    ]

    super_dict = {
        "natural numbers": [1, 2, 3, 4, 5],
        "integer numbers": [-1, -2, -3, -4, -5],
        "floating numbers": [1.1, 2.2, 3.3, 4.4, 5.5]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()