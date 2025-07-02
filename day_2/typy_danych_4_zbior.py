# zbiór (set) - przechowuje unikalne wartości (brak duplikatów)
# nie zachowuje kolejnosci przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbior
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie lementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie elementu (pierwszy)
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
print(zbior.pop())  # 66

zmienna = zbior.pop()
print("Usunęliśmy element:", zmienna)  # Usunęliśmy element: 777

zbior_copy = zbior.copy()
print(zbior_copy)
print(zbior)
print(id(zbior))  # 4368095424
print(id(zbior_copy))  # 4368094304

# operacje na zbiorach

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}
# | pipe
print(zbior.union(zbior_2))  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# część wspólna, zwraca nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# bitową operację XOR (exclusive OR)
# a = 5       # binarnie: 0101
# b = 3       # binarnie: 0011
#
# print(a ^ b)  # wynik: 6, bo 0101 ^ 0011 = 0110

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [11, 44, 12.34, 18, 52, 22, 24, 667, 62]

print(667 in zbior)  # True
print(777 in lista)  # False
print(777 in krotka)  # False
