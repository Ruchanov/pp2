from config import data
import psycopg2

sql_update_name = '''
    UPDATE phone_book SET user_name = %s WHERE phone_id = %s;
'''

sql_update_phone = '''
    UPDATE phone_book SET phone_number = %s WHERE phone_id = %s;
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

command = input("What do you want to update?[phone/name]\n")
id = input("Please enter the id of the phone record to update:")
if command == 'phone':
    phone = input("Input new value of phone number:")
    cursor.execute(sql_update_phone, (phone, id))
elif command == 'name':
    name = input("Input new value of user name:")
    cursor.execute(sql_update_name, (name, id))
else:
    print("There is no such command")

cursor.close()
db.commit()
db.close()