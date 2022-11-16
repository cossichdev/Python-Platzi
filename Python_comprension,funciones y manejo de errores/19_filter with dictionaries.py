# Se crea una lista de diccionarios con sus items, en este caso es una lista de partidos de soccer

matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

# de la lista MATCHES, crear una nueva lista, con los items filtrados con el argumento de "home result es igual a win", todo esto con ayuda de lambda

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))
