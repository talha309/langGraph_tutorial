from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    name: str
    income: int
    loan_amount : List[int]
    result : str
