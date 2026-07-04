from typing import TypedDict

from agent import order_tool, ticket_tool


class AgentState(TypedDict):
    question: str
    answer: str


# ---------------- Router ---------------- #

def router(state: AgentState):

    question = state["question"].lower()

    if "order" in question:
        return "order"

    elif any(word in question for word in [
        "damaged",
        "broken",
        "refund",
        "complaint",
        "issue",
        "defective",
        "not working"
    ]):
        return "ticket"

    else:
        return "rag"


# ---------------- Order Node ---------------- #

def order_node(state: AgentState):

    state["answer"] = order_tool(state["question"])

    return state


# ---------------- Ticket Node ---------------- #

def ticket_node(state: AgentState):

    state["answer"] = ticket_tool(state["question"])

    return state