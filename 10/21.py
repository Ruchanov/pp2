import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Ayef1407_'
)

current = config.cursor()

id = 2
username = 'Miras'
number = '87771111111'
email = 'miras@gmail.com'

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''

current.execute(sql, (id, username, number, email))


config.commit()
current.close()
config.close()