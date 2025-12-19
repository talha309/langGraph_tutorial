from langgraph.graph import START,END, StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    number1: int
    number2: int
    number3: int
    number4: int
    operation: str
    operation2: str
    finalNumber: int
    finalNumber2: int

def add_node(state:AgentState) -> AgentState:
    "add numbers"
    state["finalNumber"] = state["number1"]+state["number2"]
    return state
def subract_node(state:AgentState)-> AgentState:
    "subract numbers"
    state["finalNumber"]= state["number1"] - state["number2"]
    return state
def add_node2(state:AgentState) ->AgentState:
    "add numbers"
    state["finalNumber2"] = state["number3"]+state["number4"]
    return state
def subract_node2(state:AgentState) ->AgentState:
    "subract numbers"
    state["finalNumber2"] = state["number3"]-state["number4"]
    return state

def router(state:AgentState) -> AgentState:
    if state["operation"] == "+":
        return "add_node" 
    else: 
        return "subract_node"
def router2(state:AgentState) ->AgentState:
    if state["operation2"] == "+":
        return "add_node2"
    else:
        return "subract_node2"

graph= StateGraph(AgentState)
graph.add_node("add_node", add_node)
graph.add_node("subract_node", subract_node)
graph.add_node("add_node2", add_node2)
graph.add_node("subract_node2", subract_node2)
graph.add_conditional_edges(
    START,
    router,
    {
        "add_node": "add_node",
        "subract_node": "subract_node"
    }
)

# Router 1 → Router 2
graph.add_conditional_edges(
    "add_node",
    router2,
    {
        "add_node2": "add_node2",
        "subract_node2": "subract_node2"
    }
)

graph.add_conditional_edges(
    "subract_node",
    router2,
    {
        "add_node2": "add_node2",
        "subract_node2": "subract_node2"
    }
)

# End
graph.add_edge("add_node2", END)
graph.add_edge("subract_node2", END)

app= graph.compile()
initial_state = AgentState(
    number1=10,
    number2=5,
    number3=7,
    number4=2,
    operation="-",
    operation2="+",
    finalnumber=0,
    finalnumber2=0
)
result = app.invoke(initial_state)
print(result)
