import sqlite3

conn = sqlite3.connect("support.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (

ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,

customer_name TEXT,

issue TEXT,

status TEXT

)
""")

conn.commit()
conn.close()