# funkcja lambda
# skrócony zapis funkcji
# domyslnie ma return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(5, 89))  # -84

odejmij2 = lambda a, b: a - b
print(odejmij2(7, 90))  # -83

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(15))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)

print(l)  # [2, 4, 6, 8, 48, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# map() - wykonuje funkcje na elementach kolekcji
# funkcja wyzszego rzędu - argumentem jest inna funkcja
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 48, 100, 200, 1000]

# uzycie lambdy jako funkcja anonimowa
# nie jest przypisana do żadnej nazwy
# użycie w miejscu deklaracji
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 8, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 48, 100, 200, 1000]
# Zastosowanie map: [4, 8, 12, 16, 96, 200, 400, 2000]
# Zastosowanie map: [8, 16, 24, 32, 192, 400, 800, 4000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)

print(l3)  # [1, 2]

# filter()
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 50, lista))}")  # Zastosowanie filter: [100, 500]
print(f"Zastosowanie filter: {list(filter(lambda x: x < 500, lista))}")
# Zastosowanie filter: [1, 2, 3, 4, 24, 50, 100]

# x > 3 i x < 200
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3 and x < 200, lista))}")
# Zastosowanie filter: [4, 24, 50, 100]
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 200, lista))}")  # Zastosowanie filter: [4, 24, 50, 100]
