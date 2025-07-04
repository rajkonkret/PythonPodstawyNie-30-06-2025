# baza danych - system przechowywania dach, posiada silnik  ułatwiący prace z danymi
# sqlite - baza danych sql, w jednym pliku lub w pamięci

import sqlite3

sql_connection = None

try:
    sql_connection = sqlite3.connect('baza.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    # cursor.execute(query)
    # sql_connection.commit() # zatwierdzenie danych

    insert = """
    INSERT INTO developers (id,name,salary) VALUES (1, 'Radek',45000);
    """

    # cursor.execute(insert)
    # sql_connection.commit()

    select = """
    SELECT * FROM developers;
    """

    for row in cursor.execute(select):
        print(row)  # (1, 'Radek', 45000.0)

except sqlite3.Error as e:
    print("Bład:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknieta")
# https://sqlitebrowser.org/
