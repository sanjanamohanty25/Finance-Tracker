import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cats",
    database="financeTrackerDB",
    port = 3306
)

cursor = conn.cursor()
print("Connected to MySQL successfully!")

