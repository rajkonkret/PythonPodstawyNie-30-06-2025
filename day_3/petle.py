# pętle - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    # print(_) # 9

for i in range(5):
    print(i + 2)
    print(i * 2)
# 5
# 6
# 6
# 8

# przerobic lotto na pętle
lista_kule = list(range(1, 50))
# print(lista_kule)

lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")  # 8 parzysta

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]

print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # wykona dla wszystkich elementów listy
    if c > 4:
        print(c, "Większe od 4")
    else:
        print(c, "Mniejsze od 4")
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Mniejsze od 4
# 6 Większe od 4
# 8 Większe od 4

for i in range(0, 10, 2):  # (start, stop, krok), co drugi
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # krok ujemny, odlicza w dół
    print(i)
# 10
# 8
# 6
# 4
# 2

for c in lista3:
    if c == 2:
        c += 1
        print(c)  # 3
    print("Przy każdym przejściu pętli", c)
# Przy każdym przejściu pętli 0
# 3
# Przy każdym przejściu pętli 3
# Przy każdym przejściu pętli 4
# Przy każdym przejściu pętli 6
# Przy każdym przejściu pętli 8

imiona = ["Radek", "Tomek", "Agata", "Filip"]
print(imiona)  # ['Radek', 'Tomek', 'Agata', 'Filip']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Agata
# Filip

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Filip

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Filip

# enumerate() - zwraca ineks i element
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# (3, 'Filip') -> 3 Filip
a, b = (3, 'Filip')
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Filip

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Filip

imiona = ["Radek", "Tomek", "Agata", "Filip", "Ewa"]
wiek = [44, 55, 28, 49]
#
# # Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])

# Radek 44
# Tomek 55
# Agata 28
# Filip 49
# gdy różne długości list: IndexError: list index out of range
imiona = ["Radek", "Tomek", "Agata", "Filip", "Ewa"]
wiek = [44, 55, 28, 49]

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Agata', 28)
# ('Filip', 49)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Agata 28
# Filip 49

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Agata', 28))
# (3, ('Filip', 49))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
# (a, (c, d)) = (0, ('Radek', 44))
a, (c, d) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Agata 28
# 3 Filip 49
