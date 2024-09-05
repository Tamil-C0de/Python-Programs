import pymysql
from tabulate import tabulate

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='employee_detail'
)
cursor = connection.cursor()

# DOC_STRINGS
create_table = """CREATE TABLE employee (
id int, name varchar(20), age int, department varchar(20)
)"""

# id = int(input("Enter an id: "))
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# dep = input("Enter your Department: ")

# record = (id, name, age, dep)

# placeholders
insert_query = """INSERT INTO employee(id, name, age, department) 
                  VALUES (%s, %s, %s, %s)
"""

select_query = "SELECT * from employee"

update_query = """UPDATE employee
                  SET department='Tech' WHERE id=2 
"""

delete_query = """DELETE FROM employee WHERE id=1
"""

try:
    # cursor.execute(create_table)
    # print("Table Created...")
    # cursor.execute(insert_query, record)
    # connection.commit()
    # print("Row Inserted...")
    # cursor.execute(select_query)
    # data = cursor.fetchone()
    # data = cursor.fetchall()
    # data = cursor.fetchmany(3)
    # print(data)

    # cursor.execute(update_query)
    # connection.commit()
    # cursor.execute(select_query)
    # data = cursor.fetchall()

    # headers = ['ID', 'NAME', 'AGE', 'DEPARTMENT']
    # print(tabulate(data, headers))
    cursor.execute(delete_query)
    connection.commit()
    cursor.execute(select_query)
    data = cursor.fetchall()
    print(data)

except Exception as e:
    print("Exception: ", e)

finally:
    cursor.close()
    connection.close()
