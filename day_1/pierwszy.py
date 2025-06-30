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

print(int(168) + int(50))  # 218
