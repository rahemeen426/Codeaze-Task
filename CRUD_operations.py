import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)
insert_data = """INSERT INTO details(name, grade)
                VALUES ('Saniya Sarim', 'B')"""
cursor = mydb.cursor()
result = cursor.execute(insert_data)
mydb.commit()
print("Data Inserted into Table")

if(mydb.is_connected()):
    cursor.close()
    mydb.close()
    print("MySql connection is closed")