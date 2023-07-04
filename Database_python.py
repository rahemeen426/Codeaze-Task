import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE student")
cursor.execute("CREATE TABLE details (name VARCHAR(255), grade VARCHAR(255))")
# # Show existing tables
cursor.execute("SHOW TABLES")
 
for x in cursor:
  print(x)