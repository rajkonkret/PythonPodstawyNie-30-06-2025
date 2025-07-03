# funkcja - wydzielony fragment kodu, który możemy wykonać w dowolnym momencie
# funkcja musi zostać najpierw zadeklarowana
# w miejscu deklaracji funkcja się nie wykona
# żeby uruchomić funkcję należy ją wywołać

a = 8
b = 6


# PEP8 prosi by funkja od ciała programu byłą oddzielona dwoma pustymi liniami
# dekalracja funkcji
def dodaj():  # funkcja bezargumetowa
    print(a + b)


def dodaj2(a, b):  # funkcja posiada dwa argumenty
    # a i b musi byc obowiązkowo przekazane
    # lokalne argumenty a i b
    print(a + b)


# pozwala zasymulowac przeciązanie funkcji liczbą argumentów
def odejmij(a, b, c=0):  # a,b obowiazkowe, c - ma wartość domyslną
    print(a - b - c)


# użycie funkcji, (uruchomienie)
# nazwa funkcji i nawiasy
print(dodaj)  # <function dodaj at 0x1050d3600>
print(type(dodaj))  # <class 'function'>
dodaj()  # 14, uruchomienie funkcji

# po pozycji
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(56, 89)  # 145, obowiązkowo musimy przekazac te argumenty

odejmij(1, 2, 5)  # -6
odejmij(1, 2)  # -1

# po nazwie
odejmij(c=9, b=9, a=89)  # 71
odejmij(b=89, a=65)  # -24

# argumenty mieszane
odejmij(1, 2, c=89)  # -90

# argumenty pozycyjne muszą być pzed nazwannymi
# odejmij(c=90, 1, 2) # SyntaxError: positional argument follows keyword argument

print(dodaj())
# 14
# None

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + odejmij(6, 89))
