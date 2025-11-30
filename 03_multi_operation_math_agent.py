from typing import TypedDict, List
from langgraph.graph import START, StateGraph, END

class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result : str

def process_function(state: AgentState) ->AgentState:
    op= state['operation']

    if op == "+":
        total = sum(state['values'])
        state["result"]= f"Hi {state['name']}, the answer is = {total}"
        return state
    elif op == "*":
        mul = 1
        for i in state['values']:
            mul*= i
            state["result"] = f"Hi {state['name']}, your answer is = {mul}"
            return state
    elif op == "-":
        sub = state["values"][0]
        for v in state["values"][1:]:
            sub -= v
        state["result"] = f"Hi {state['name']}, your answer is = {sub}"
        return state
    elif op == "avg":
        average = sum(state['values']) / len(state["values"])
        state["result"] = f"Hi {state['name']}, your answer is = {average}"
        return state
    else:
        state["result"]= "Invalid operator. Please use +, -, *, avg"
        return state
    
graph = StateGraph(AgentState)
graph.add_node("processor", process_function)

graph.add_edge(START, "processor")
graph.add_edge("processor", END)

app = graph.compile()


answer= app.invoke({
    "name": "Bruce Wayne",
    "values": [5, 10, 15],
    "operation": "-"
})

print(answer["result"])
        
