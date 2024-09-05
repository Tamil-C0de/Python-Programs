import pymysql

conn = pymysql.connect(
    host= 'localhost',  #127.0.0.1
    user= 'root',
    password= 'root',
    # database= 'employee_detail'
)
cursor = conn.cursor()

# query = "SELECT VERSION()"
query_1 = "DROP DATABASE demo"
query_2 = "CREATE DATABASE demo"

try:
    if not cursor.execute(query_1): # None -> False
        print("Databased Deleted...")
    cursor.execute(query_2)

    # data = cursor.fetchone()
    # print(data)

except Exception as e:
    print("Exception: ", e)

finally:
    cursor.close()
    conn.close()