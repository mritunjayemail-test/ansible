import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='TUTORIALS',
                                         port='3306',
                                         user='root',
                                         password='root')
    mySql_insert_query = """INSERT INTO addressbook (name, phone, website) 
                           VALUES 
                           ('Lenovo ThinkPad P71', 0616692719, 'www.example.com') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into addressbook table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")