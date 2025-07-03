import math
from itertools import zip_longest

print(math.pi)  # 3.141592653589793

print(math.sqrt(25))  # 5.0

angle_degree = 30
angle_radians = math.radians(angle_degree)
sin_value = math.sin(angle_radians)

print(f"sin({angle_degree}) = {sin_value}")
# sin(30) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]
sin_values = [math.sin(math.radians(a)) for a in angles]

for a, s in zip(angles, sin_values):  # zip() - łączy kolekcji
    print(f"sin({a}) = {s}")
# sin(30) = 0.49999999999999994
# sin(0) = 0.0
# sin(30) = 0.49999999999999994
# sin(45) = 0.7071067811865475
# sin(60) = 0.8660254037844386
# sin(90) = 1.0
imiona = ["Radek", "Tomek", "Agata", "Filip", "Ewa"]
wiek = [44, 55, 28, 49]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x104ec1850>

for item in zipped:
    print(item)
# ('Radek', 44)
# ('Tomek', 55)
# ('Agata', 28)
# ('Filip', 49)
# ('Ewa', None)

# iteratory tylko raz dostarczą daane
print(25 * "_")
for i, o in zipped:
    print(i, o)
