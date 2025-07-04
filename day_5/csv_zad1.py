# csv - dane oddzielone znakiem podziału ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

# csv - bibioteka do plików csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ["radek", "coe", "3", '0']
dict_dane = dict(zip(fields, row))
print(dict_dane)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

filename = 'records.csv'
with open(filename, 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_dict.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict_dane)

products = [
    {"sku": 1, "exp_date": 'today', "price": 20},
    {"sku": 2, "exp_date": 'today', "price": 100},
    {"sku": 3, "exp_date": 'tommorow', "price": 500},
    {"sku": 4, "exp_date": 'today', "price": 80},
    {"sku": 5, "exp_date": 'today', "price": 50},
]

filename = 'records_discount.csv'
list_product = [key for key in products[0]]
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows - zapisze listę słowników
