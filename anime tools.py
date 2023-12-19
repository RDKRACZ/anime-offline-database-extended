import json

filename = "anime-offline-database.json"
with open(filename, 'r') as file:
    data = json.load(file)['data']  # Access 'data' key from JSON file

# # Filter the list of dictionaries where the 'year' is 2020
# filtered_data = list(filter(lambda x: x["animeSeason"]["year"] == 2020, data))
# print(filtered_data)


for i in data:
    if i['animeSeason']['year'] == 2020:  # Access 'year' within 'animeSeason'
        print('Year:', i['animeSeason']['year'])
        print('Status:', i['status'])


# sprawdź najdłuższy i najkrótszy tutuł romaji i eng
# najwięcej odc
# najdłuższe / najkrótsze odc
# wybierz rok i zobacz najpopularnijsze / najwyżej oceniane
# wypisz tytuły zawierające coś poza literami, cyframi i "? ! - :"
# ile tytułów jest
# ile z nich to tv, ile ova, ona, special, movie
