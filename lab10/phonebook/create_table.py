from config import data
import psycopg2

sql = '''
    CREATE TABLE phone_book(
        phone_id SERIAL PRIMARY KEY,
        user_name VARCHAR(32),
        phone_number VARCHAR(32)
    );
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

cursor.close()
db.commit()
db.close()