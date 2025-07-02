# kolekcja

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejnośc przy dodawaiu danych

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append - dodanie lementów do listy
lista.append("Radek")
lista.append("Agata")
lista.append("Tomek")
lista.append("Jarek")
lista.append("Filip")
print(lista)
# ['Radek', 'Agata', 'Tomek', 'Jarek', 'Filip']
#     0        1        2        3        4

print(len(lista))  # 5

print(lista[0])  # Radek
print(lista[2])  # Tomek
print(lista[4])  # Filip

# print(lista[10])  # IndexError: list index out of range

print(lista[4])  # Filip
print(lista[len(lista) - 1])  # Filip
print(lista[-1])  # Filip - ostatni element
print(lista[-3])  # Tomek

# slicowanie - wyswietlenie fragmentu listy
print(lista[0:3])  # ['Radek', 'Agata', 'Tomek'] -> 012
print(lista[:3])  # ['Radek', 'Agata', 'Tomek']
print(lista[2:])  # ['Tomek', 'Jarek', 'Filip'] -> 234  z ostatnim włacznie
print(lista[2:4])  # ['Tomek', 'Jarek'] -> 23

print(lista[2:16])  # ['Tomek', 'Jarek', 'Filip']
print(lista[10:37])  # []
print(lista[2:2])  # []
print(lista[2:3])  # ['Tomek']

print(lista[:])  # ['Radek', 'Agata', 'Tomek', 'Jarek', 'Filip']

# ['Radek', 'Agata', 'Tomek', 'Jarek', 'Filip']
#     0        1        2        3        4
#    -5        -4      -3       -2        -1
print(lista[-2:0])  # [] -> [3:0]
print(lista[0:-2])  # ['Radek', 'Agata', 'Tomek']

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]

print(lista[::2])  # ['Radek', 'Tomek', 'Filip'] cała lista co drugi element

print(lista[::-1])  # ['Filip', 'Jarek', 'Tomek', 'Agata', 'Radek'] odwrócona lista

# nadpisanie elementu w liście na wskazanym indeksie
# zmiana na oryginalnej liście

lista[3] = "Asia"
print(lista)  # ['Radek', 'Agata', 'Tomek', 'Asia', 'Filip']

# dopisanie elemntu do listy we wskazanym indeksie
lista.insert(1, "Agata")
print(lista)
# ['Radek', 'Agata', 'Agata', 'Tomek', 'Asia', 'Filip']

# sprawdzenie indeksu dla danego elementu
print(lista.index("Asia"))  # index 4
print(lista.index("Agata"))  # indeks 1, pierwszy napotkany
# print(lista.index("Jarek")) # ValueError: 'Jarek' is not in list

# usunięcie elementów z listy po elemencie
lista.remove("Agata")  # usunie pierwszy napotkany
print(lista)  # ['Radek', 'Agata', 'Tomek', 'Asia', 'Filip']

# usunięcie po indeksie pop()
print(lista.pop(3))  # Asia, zwróći usunięty eleemnt
print(lista)  # ['Radek', 'Agata', 'Tomek', 'Filip']
print(lista.pop(-1))  # Filip
print(lista.pop())  # Tomek, usunie ostatni

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista_2 = lista  # kopiuje referencje, adres pamięci

lista_copy = lista.copy()  # kopia elementów listy

print(lista_2)  # ['Radek', 'Agata']
print(lista)  # ['Radek', 'Agata']
lista.clear()  # usunięcie elementów z listy
print(lista_2)  # []
print(lista)  # []
print(lista_copy)  # ['Radek', 'Agata']

print(id(lista))  # 4302796544
print(id(lista_2))  # 4302796544
print(id(lista_copy))  # 4303535872

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)  # [54, 999, 34, 22, 12.34, 567]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 567, 999]

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 567, 'A']
print(type(liczby))  # <class 'list'>
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Radek', 'Agata']
lista_copy.sort()
print(lista_copy)  # ['Agata', 'Radek']

lista_copy.sort(reverse=True)
print(lista_copy)  # ['Radek', 'Agata']

lista_copy.reverse()
print(lista_copy)  # ['Agata', 'Radek']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 567
print(liczby)  # [54, 999, 34, 666, 12.34, 567, 'A']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Agata', 'Radek')
