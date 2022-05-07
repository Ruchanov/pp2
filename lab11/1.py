import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Ayef1407_'
)
''' my SQL in DATAGRIP:
create or replace function getStudentNameSurnamePhone(name varchar)
    returns setof phonebook_lab11
as
$$
begin
    return query
        select *  from phonebook_lab11
        where (phonebook_lab11.first_name = $1) or (phonebook_lab11.last_name = $1);
end
$$ language plpgsql;
'''


cursor = conn.cursor()
conn.autocommit = True

name = str(input("name: "))
cursor.callproc('getStudentNameSurnamePhone', [name])
result = cursor.fetchall()
print(result)