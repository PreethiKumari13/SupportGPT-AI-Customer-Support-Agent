import sqlite3

conn = sqlite3.connect("support.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (

order_id INTEGER PRIMARY KEY,

customer_name TEXT,

product TEXT,

status TEXT,

delivery_date TEXT

)
""")

orders = [

(1001, "Preethi", "Laptop", "Shipped", "Tomorrow"),

(1002, "Rahul", "Keyboard", "Delivered", "2 July"),

(1003, "Ananya", "Mouse", "Processing", "5 July"),

(1004, "Kiran", "Monitor", "Cancelled", "N/A")

]

cursor.executemany(

"INSERT OR REPLACE INTO orders VALUES (?,?,?,?,?)",

orders

)

conn.commit()

conn.close()

print("Database Created Successfully!")