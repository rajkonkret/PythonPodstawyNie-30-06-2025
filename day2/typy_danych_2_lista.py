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
