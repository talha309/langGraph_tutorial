from langgraph.graph import START, END, StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    finalnumber: int

def adder(state:AgentState):
    """this is adder node"""
    state['finalnumber']= state['number1']+state['number2']
    return state
def subtractor(state:AgentState):
    """this is adder node"""
    state['finalnumber']= state['number1']-state['number2']
    return state

def decide_node(state:AgentState):
    if state['operation'] == "+":
        return "addition_operation"
    else:
        return "subtraction_operation"

graph=StateGraph(AgentState)
graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state:state)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    decide_node,
    {
        "addition_operation":"add_node",
        "subtraction_operation":"subtract_node"
    }

)
graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

initial_state = AgentState(number1=10,operation="-",number2=5)
print(app.invoke(initial_state))