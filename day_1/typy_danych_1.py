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
