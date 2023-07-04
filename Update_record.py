import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)
update_data = """UPDATE details SET grade = 'A+' WHERE name = 'Rahemeen Khan' """
cursor = mydb.cursor()
result = cursor.execute(update_data)
mydb.commit()
print("Data Updated")

if(mydb.is_connected()):
    cursor.close()
    mydb.close()
    print("MySql connection is closed")