import pandas
# pip install pandas

# data = pandas.read_csv('records.csv')
data = pandas.read_csv('records_discount.csv', delimiter=";")
#     name branch  year  cgpa
# 0  radek    coe     3     0
# 	•	delimiter=';' – bo Excel eksportuje z separatorem ; (ustawienia regionalne),
# 	•	decimal=',' – mówi Pandasowi, że przecinek to separator dziesiętny.
# import pandas as pd
#
# df = pd.read_csv("plik.csv", delimiter=';', decimal=',')
# print(df)
# delimiter='\t'
print(data)
#    sku  exp_date  price
# 0    1     today     20
# 1    2     today    100
# 2    3  tommorow    500
# 3    4     today     80
# 4    5     today     50

print(data.columns) # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 20]
#  [2 'today' 100]
#  [3 'tommorow' 500]
#  [4 'today' 80]
#  [5 'today' 50]]