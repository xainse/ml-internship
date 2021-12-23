# Используя sqlite3, напишите код, который создает таблицу базы данных
# для датасета с CityId городов различных стран мира, приведенного в файле

# https://worldweather.wmo.int/en/json/full_city_list.txt. Предусмотреть функ-
# цию, позволяющую вносить изменения в базу данных. Продемонстрировать
# её работу.

import sqlite3
import csv



# 1. Прочитати данні ітеративно із CSV файлу


# 2. Створити базу даних, а якщо вона є - то очистити її 
DB_NAME = 'ml-intern-testdb1.db'

con = sqlite3.connect(DB_NAME)
cur = con.cursor() # створюємо об'єкт-курсор
sql = """\
    DROP TABLE IF EXISTS cities;

    CREATE TABLE cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Country TEXT, 
        City TEXT, 
        CityId INTEGER
    );
    """
# 3. Створити таблицю cities
try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("SQL error: ", err)
else:
    print('TBL created sucsesfuly.')
cur.close()
con.close()



# 4. В циклі записати дані в базу даних. 

# 5. 

# 2. Створити базу даних, а якщо вона є - то очистити її


file_path_csv = "./full_city_list.txt" # але насправді я знаю, що всередині данні у вигляді CSV

con = sqlite3.connect(DB_NAME)
cur = con.cursor()  # створюємо об'єкт-курсор

with open(file_path_csv, "r") as file_object:
    csv_file = csv.DictReader(file_object, delimiter=';', quotechar='"')
    
    sql = """\
        INSERT INTO cities (country, city, CityId)
        VALUES (:Country, :City, :CityId)
    """
    for row in csv_file:
        try:
            cur.execute(sql, row)
        except sqlite3.DatabaseError as err:
            print("SQL error: ", err)
        else:
            con.commit()

cur.close()
con.close()

