import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)

cursor = mydb.cursor()
read_data1 = """SELECT * FROM details """

result1 = cursor.execute(read_data1)
employee_data = result1.fetchall()
print(employee_data)
