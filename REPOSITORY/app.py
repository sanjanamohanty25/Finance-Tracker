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

# Sample table creation
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")
conn.commit()

cursor.close()
conn.close()
