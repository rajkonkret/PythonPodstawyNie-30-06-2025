from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-07-02
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-07-02 12:37:07.119530

print(time.year)  # 2025
print(today.day)  # 2

# tommorow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print("Jutro będzie:", tommorow)  # Jutro będzie: 2025-07-03

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Data sformatowana:", formated_date)  # Data sformatowana: 02/07/2025
print(type(formated_date))  # <class 'str'>

# sformatowany czas 12:56
formated_time = datetime.now().strftime("%H:%M")
print(type(formated_time))
print("Sformatowany czas:", formated_time)  # Sformatowany czas: 13:00

formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Czas 12h:", formated_time_usa)  # Czas 12h: 01:01 PM

products = [
    {"sku": 1, "exp_date": today, "price": 20},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tommorow, "price": 500},
    {"sku": 4, "exp_date": today, "price": 80},
    {"sku": 5, "exp_date": today, "price": 50},
]

for product in products:
    # print(product)
    # {'sku': 1, 'exp_date': datetime.date(2025, 7, 2), 'price': 20}
    # print(type(product))  # <class 'dict'>
    # print(product['exp_date'])  # 2025-07-02

    if product['exp_date'] != today:
        continue  # konczy biezącą iterację pętli, odkłada słoik na półkę

    product['price'] *= 0.8  # p = p * 0.8
    print(f"""Price for sku {product['sku']}
is now {product['price']}""")
