from config import data
import psycopg2,csv

sql = '''
    INSERT INTO phonebook_lab11 VALUES(%s,%s, %s);
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

try:
    with open("input.csv", "r") as f:
        data = csv.reader(f, delimiter=',')
        for row in data:
            cursor.execute(sql, row)
except Exception as e:
    print("There is no such csv file, please input the values manually")
    surname = input("Input the surname:")
    name = input("Input the name:")
    phone = input("Input the names phone number:")
    cursor.execute(sql,(surname,name,phone))

cursor.close()
db.commit()
db.close()