

def run():
    # diccionario = {
    #     'llave1' : 1,
    #     'llave2' : 2,
    #     'llave3' : 3,
    # }
    # print(diccionario)
    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])

    población_países = {
        'Argentina' : 123456789,
        'Brasil' : 98765321,
        'Colombia' : 987321654,
    }
    # print(población_países[''])

    # for país in población_países.keys():
    #     print(país)
    # for país in población_países.values():
    #     print(país)
    for país, población in población_países.items():
        print(país + ' tiene ' + str(población)+ ' habitantes')
        
if __name__ == '__main__':
    run()