import random

# operacje na liczbach losowych

# ""Return random integer in range [a, b], including both end points.
#         """
print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # 0.2646095921171224 float od 0 do 0.9999999
print(random.random() * 7)  # 1.7169994299035825 od 0 do 6.9999999

lista = [67, 45, 32, 68, 90, 42, 69]
print(random.choice(lista))  # wylosowany element z listy 32

lista_kule = list(range(1, 50))
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniami
print(random.sample(lista_kule, k=6))  # [26, 33, 17, 13, 42, 48]
print(random.sample(lista_kule, 6))  # [26, 33, 17, 13, 42, 48]
# [28, 40, 25, 48, 42, 30]
# [19, 30, 13, 28, 46, 34]
# [31, 17, 22, 39, 36, 3]
