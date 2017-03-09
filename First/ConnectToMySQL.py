__author__ = 'mranjan'

import mysql.connector
conn=mysql.connector.connect(user='root',password='root',host='localhost',port='3306',database='manish')



try:
    cursor=conn.cursor()
    cursor.execute("show tables")
    print(cursor.fetchall())
finally:
    conn.close