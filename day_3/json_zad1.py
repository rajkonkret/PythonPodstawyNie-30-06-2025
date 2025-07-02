# {"name":"John", "age":30, "car":null}
# dane typu klucz wartosc
# uzywamy do komunikacji w internecie
# odpowiednikiem jsona w pythonie jest  słowniki

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# upiekszanie, beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)

# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowane klucze
with open('nasze_dane_sort.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }