import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Ayef1407_'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20),
        number VARCHAR(12),
        email VARCHAR(30)
    )
    '''
)

config.commit()
current.close()
config.close()