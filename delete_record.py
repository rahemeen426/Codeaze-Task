import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)
delete_record = """DELETE from details WHERE grade = 'B' """
cursor = mydb.cursor()
result = cursor.execute(delete_record)
mydb.commit()
print("Record deleted")

if(mydb.is_connected()):
    cursor.close()
    mydb.close()
    print("MySql connection is closed")