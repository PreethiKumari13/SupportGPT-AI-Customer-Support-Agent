import sqlite3


# ---------------- ORDER LOOKUP ---------------- #

def get_order(order_id):

    conn = sqlite3.connect("support.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM orders WHERE order_id=?",
        (order_id,)
    )

    order = cursor.fetchone()

    conn.close()

    if order:
        return {
            "order_id": order[0],
            "customer": order[1],
            "product": order[2],
            "status": order[3],
            "delivery": order[4]
        }

    return None


# ---------------- CREATE SUPPORT TICKET ---------------- #

def create_ticket(customer_name, issue):

    conn = sqlite3.connect("support.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            issue TEXT,
            status TEXT
        )
    """)

    cursor.execute(
        """
        INSERT INTO tickets(customer_name, issue, status)
        VALUES (?, ?, ?)
        """,
        (customer_name, issue, "Open")
    )

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id


# ---------------- VIEW ALL TICKETS (Optional) ---------------- #

def get_all_tickets():

    conn = sqlite3.connect("support.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    conn.close()

    return tickets