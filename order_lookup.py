import sqlite3

def get_order(order_id):
    conn = sqlite3.connect("support.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM orders WHERE order_id = ?",
        (order_id,)
    )

    order = cursor.fetchone()

    conn.close()

    return order


while True:

    order_id = input("Enter Order ID (or exit): ")

    if order_id.lower() == "exit":
        break

    order = get_order(int(order_id))

    if order:
        print("\nOrder Found\n")
        print(f"Order ID      : {order[0]}")
        print(f"Customer Name : {order[1]}")
        print(f"Product       : {order[2]}")
        print(f"Status        : {order[3]}")
        print(f"Delivery Date : {order[4]}")
    else:
        print("Order not found.")