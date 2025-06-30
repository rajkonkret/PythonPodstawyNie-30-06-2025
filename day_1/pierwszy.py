# 2 x shift - wyszukiwarka
# wheel
# theme
import sys

print()  # wypisz/wydrukuj
# PEP8
# ctrl alt l - fromatowanie kodu
# Process finished with exit code 0 - program zakońćzył się bez błedu

print("Nazywam sie Radek")  # Nazywam sie Radek
print("Nazywam sie Radek")  # Nazywam sie Radek
print("Nazywam sie Radek")  # Nazywam sie Radek
print("Nazywam sie Radek")  # Nazywam sie Radek
print("Nazywam sie Radek")  # Nazywam sie Radek
print("Nazywam sie Radek")  # Nazywam sie Radek
# ctrl d - powielanie linii

print('Nazywam się Radek')  # Nazywam się Radek

# ctrl / - komentarz
# print('Nazywam się Radek")
# /Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/.venv/bin/python /Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_1/pierwszy.py
#   File "/Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_1/pierwszy.py", line 19
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 19)

# type() - sprawdzenie typu
print(type("Radek"))  # <class 'str'>, string, tekstowe

print("39" + "39")  # 3939, konkatenacja, łączenie tekstów

print(39 + 39)  # 78
print(type(39))  # <class 'int'>, liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4, default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# print(39 + "39")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# musimy jawnie rzutować (zamieniać)  na odpowiednie typy
print(int("39"))  # rzutujemy na int() 39
print(int("39") + 39)  # 78

print("39" + str(39))  # 3939

# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

print(5 * "4")  # 44444
print("168" * 50)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(168 * 50)  # 8400

print(int("168") + int("50"))  # 218

# zmienna - pudełko na dane
# snake_case
# nazwa zmiennej powinna podpowiadac co przecho218wuje

# typowanie dynamiczne
# typ zmiennej jest wnioskowany na podstawie danych jakie zawiera zmienna
liczba = 39
print(liczba)  # 39
print(type(liczba))  # <class 'int'>

liczba = "Radek"
print(liczba)  # Radek

print(type(liczba))  # <class 'str'>

name = "Radek"
print(name + "kowalski")  # Radekkowalski

name = 90
# print(name + "kowalski") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# typ danych int - liczby całkowite
# str - teksty

# to jest tylko podpowiedź
name: str = "Radek"
print(name)  # Radek
name = 90  # dałem int
print(name)  # 90

age = 56
print(age)  # 56
print(type(age))  # <class 'int'>

# #  pip install mypy
# cd day_1/
#  mypy pierwszy.py
# (.venv) radoslawjaniak@MacBook-Air-radosaw-2 day_1 % mypy pierwszy.py
# pierwszy.py:68: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:76: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:82: error: Name "name" already defined on line 73  [no-redef]
# pierwszy.py:84: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 4 errors in 1 file (checked 1 source file)
# (.venv) radoslawjaniak@MacBook-Air-radosaw-2 day_1 %
print("Test") # Test