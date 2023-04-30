import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password=''
)

current = config.cursor()
sql1 = '''
    CREATE TABLE employee(
		person_name VARCHAR(255) PRIMARY KEY,
		street VARCHAR(255),
		city VARCHAR(255)
	)
'''

sql2 = '''
	CREATE TABLE company(
		company_name VARCHAR(255) PRIMARY KEY,
		city VARCHAR(255)
	)
'''
sql3 = '''
	CREATE TABLE works(
		person_name VARCHAR(255) PRIMARY KEY,
		company_name VARCHAR(255),
		salary INTEGER,
		PRIMARY KEY (person_name, company_name)
	)
'''
current.execute(sql2)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()