import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)

    csv_f.seek(0)  # ponownie odczyt na początek pliku

    # csvreader = csv.reader(csv_f)
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x102e1e030> iterator

    fields = next(csvreader)  # zwróci pierwszy element, odczyt ustawiony na następny

    for row in csvreader:  # zacznie os wiersza drugiego
        # print(row)
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
