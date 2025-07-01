# krotka - tuple - kolekcja niemutowalne, tylko do odczytu
# pozwala efektywniej zarzadzać pamięcią
# krotka jednoelementowa - stała, szczególny przykład zmiennej

tupla_imiona = "Radek", "Zenek", "Tomek", "Mateusz", "Ania", "Marek"
# ctrl alt l - formatowanie kodu
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Radek', 'Zenek', 'Tomek', 'Mateusz', 'Ania', 'Marek')

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jednoelementowa
tupla_jeden = 45
print(type(tupla_jeden))  # <class 'int'>

tupla_jeden = (43)
print(type(tupla_jeden))  # <class 'int'>

tupla_jeden = 43,
print(type(tupla_jeden))

# PEP8 zaleca by jedoelementowe tuple tworzyc z nawiasem
tupla_jeden = (43,)
print(type(tupla_jeden))  # <class 'tuple'>
print(tupla_jeden)  # (43,)

# tupla jest niemutowalna (nie można zmienić)
# tupla_liczby[3] = 123 # TypeError: 'tuple' object does not support item assignment

print(tupla_jeden[0])  # 43

# krotka
del tupla_jeden
# print(tupla_jeden) # NameError: name 'tupla_jeden' is not defined

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(f"{a=}, {b=}")

a, b = tup
print(f"{a=}, {b=}")  # a=1, b=2

tup_2 = 1, 2, 3
# a, b = tup_2 # ValueError: too many values to unpack (expected 2)

a, *b = tup_2  # * worek na pozostałe dane
print(f"{a=}, {b=}")  # a=1, b=[2, 3]

print(tupla_imiona)
# ('Radek', 'Zenek', 'Tomek', 'Mateusz', 'Ania', 'Marek')
# name1, name2, name3
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Zenek ['Tomek', 'Mateusz', 'Ania', 'Marek']

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Zenek', 'Tomek', 'Mateusz'] Ania Marek

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Zenek', 'Tomek', 'Mateusz', 'Ania'] Marek

# sortowanie krotki zwróci posortowaną listę
print(sorted(tupla_imiona))  # ['Ania', 'Marek', 'Mateusz', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # krotka się nie zmieniła
