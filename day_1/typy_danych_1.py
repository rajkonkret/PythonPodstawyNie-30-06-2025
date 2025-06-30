import sys

wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float
print(temp)  # 36.6
print(type(temp))  # <class 'float'>

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877

print(rok // wiek)  # częśc całkowita z dzielenia, 43
print(rok % wiek)  # modulo, reszta z dzielenia, 4
print(5 % 2)  # r1 bo 2 całe i reszta 1

print(wiek ** rok)

# len() - sprawdzenie długości
print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2))) # 3386
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# liczby typu float
# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# he sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{temp}
    {wiek
}""")
# "36.6
#     47"

# typ logiczny
# prawda fałsz
# True, False
# 1 0
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, logiczny

print(int(czy_znasz_pythona))  # 1

print(int(False))  # 0

# bool() - rzutowanie na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # nie wiem, stan nieokreślony, null, False

# and - i
print(True and True)  # True
print(True and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True

# not - negacja
print(not True)  # False
print(not False)  # True

a = 8
b = 6
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 8 <= 6 = False
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 8 >= 6 = True
print(f"Porównaie {a >=b = }")  # Porównaie a >=b = True

print(f"Porówanie {a} == {b} = {a == b}")  # czy a równa się b, Porówanie 8 == 6 = False
print(f"Porówanie {a} != {b} = {a != b}")  # czy a różne  b, Porówanie 8 != 6 = True
