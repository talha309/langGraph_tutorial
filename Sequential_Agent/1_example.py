from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    name: str
    age: str
    final: str

def first_node(state: AgentState) ->AgentState:
    """this is first node."""
    state['final']= f"Hi {state['name']},"
    return state
def second_node(state: AgentState) -> AgentState:
    """this is second node."""
    state['final']= state['final'] + f" You are {state['age']} years old!"
    return state
graph = StateGraph(AgentState)
graph.add_node("FIRST", first_node)
graph.add_node("SECOND", second_node)
graph.add_edge(START,"FIRST")
graph.add_edge("FIRST","SECOND")
graph.add_edge("SECOND",END)

app = graph.compile()
result = app.invoke({
    "name":"ANAS",
    "age": 34,
})
print (result)