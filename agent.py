from langchain.tools import Tool

from tools import get_order, create_ticket


def order_tool(query):

    import re

    match = re.search(r"\d{4}", query)

    if not match:
        return "Please provide a valid Order ID."

    order = get_order(int(match.group()))

    if not order:
        return "Order not found."

    return f"""
Order ID : {order['order_id']}

Customer : {order['customer']}

Product : {order['product']}

Status : {order['status']}

Delivery : {order['delivery']}
"""


def ticket_tool(query):

    ticket = create_ticket(
        "Preethi",
        query
    )

    return f"""
Support Ticket Created

Ticket ID : SUP-{ticket}

Status : Open
"""


tools = [

    Tool(
        name="Order Lookup",
        func=order_tool,
        description="Use this whenever the user asks about an order."
    ),

    Tool(
        name="Support Ticket",
        func=ticket_tool,
        description="Use this whenever the user reports a complaint, damaged product, refund or broken item."
    )

]