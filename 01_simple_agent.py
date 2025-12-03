from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """simple agent for testing"""
    print(state)
    state['message'] = "hey " + state['message'] + ", How is it going?"
    return state

# Create graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("greeter", greeting_node)

# Add edges
graph.add_edge(START, "greeter")
graph.add_edge("greeter", END)

# Compile
app = graph.compile()

# Invoke
result = app.invoke({"message": "BOB"})
print(result["message"])

class State(TypedDict):
    name : str
    age: int

def meet(state:State) -> State:
    """simple exersics of langgraph"""
    print(state)
    state['name'] = state['name']+ ",You're doing a Amazing job learning Langgraph!"
    return state

graph = StateGraph(State)
graph.add_node("meeting", meet)

graph.add_edge(START, "meeting")
graph.add_edge("meeting", END)

app = graph.compile()
result = app.invoke({"name":"BOB","age":18})
print (result["name"])
print (result["age"])