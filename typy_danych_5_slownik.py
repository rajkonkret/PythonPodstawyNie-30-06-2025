# słownik - para klucz-wartosc
# {"user":"Radek", "wiek":76}
# klucze nie mogą się powtarzać
# odpowiednik jsona w pythonie

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {} - pusy słownik
print(type(dictionary_1))  # <class 'dict'>

# dodanie lementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 48
print(dictionary)  # {'imie': 'Radek', 'wiek': 48}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 48])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 48)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48}

# wypisanie wartość dla klucza
print(dictionary['imie'])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None, nie ma klucza
print(dictionary.get("Imie", "default"))  # gdy nie ma klucza zwraca -> default

print(dictionary.get("imie"))  # Tomek

dictionary.update({'data': "12-12-2025"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48, 'data': '12-12-2025'}

dict_small = {'x': 2}
print(dict_small)  # {'x': 2}
# [('imie', 'Radek'), ('wiek', 48)] lista krotek
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 8}
