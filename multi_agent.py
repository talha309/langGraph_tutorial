from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
# Create a Graph where you pass in a single list of integers along with a name and an # operation . if the operation is a "+" you add the elements 
# and if it is a "*",you # multiply the elements, all within the same node.
class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result: str

def process_value(state: AgentState) -> AgentState:
    """Processing according to the operation."""

    op = state["operation"]

    # ADDITION
    if op == "+":
        total = sum(state["values"])
        state["result"] = f"Hi {state['name']}, your answer = {total}"
        return state

    # MULTIPLICATION
    elif op == "*":
        mul = 1
        for v in state["values"]:
            mul *= v
        state["result"] = f"Hi {state['name']}, your answer = {mul}"
        return state

    # INVALID OPERATOR
    else:
        state["result"] = "Please enter a valid operator: + or *"
        return state


# Build graph
graph = StateGraph(AgentState)
graph.add_node("processor", process_value)

graph.add_edge(START, "processor")
graph.add_edge("processor", END)

app = graph.compile()

# Test
answer = app.invoke({
    "name": "Jack Sparrow",
    "values": [1, 2, 3, 4],
    "operation": "*"
})

print(answer["result"])
