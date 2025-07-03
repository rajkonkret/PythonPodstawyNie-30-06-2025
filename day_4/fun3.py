a = 10  # zmienne globalne
b = 10


def dodaj():
    a = 7  # lokalna zmienna
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # użyje globalnych


def dodaj3():
    global a  # a globalne !!!
    a = 9  # nadpisze globalne a !!!
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj()  # 15
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj2()  # 20
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj3()  # 98
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
