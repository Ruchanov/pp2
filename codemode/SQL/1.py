import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Ayef1407_'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE users(
        username VARCHAR(255),
        age INTEGER,
        registration TEXT,
        password VARCHAR(50),
    );
    '''
)

db_version = current.fetchone()

print('Psql version:')
print(db_version)

current.close()


config.close()