import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306
)

mycursor = db.cursor()

# Drop the database
mycursor.execute("DROP DATABASE IF EXISTS testdb;")

mycursor.close()
db.close()