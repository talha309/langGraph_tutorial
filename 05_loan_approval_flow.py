from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class LoanState(TypedDict):
    name: str
    income: int
    loan_amount: int
    status: str
    result: str

def eligibility_checker(state: LoanState) -> LoanState:
    i = state['income']
    lo = state['loan_amount']

    if i < 20000:
        state['status'] = "not_eligible"
        return state
    elif lo > i * 0.5:
        state['status'] = "not_eligible"
        return state
    else:
        state['status'] = "eligible"
        return state

def response_generator(state: LoanState) -> LoanState:
    status = state['status']
    
    if status == "eligible":
        state['result'] = f"Hi {state['name']}, your loan request is approved!"
    else:
        state['result'] = f"Hi {state['name']}, your loan request is denied!"
    
    return state

graph = StateGraph(LoanState)
graph.add_node("eligibility_checker", eligibility_checker)
graph.add_node("response_generator", response_generator)

graph.add_edge(START, "eligibility_checker")
graph.add_edge("eligibility_checker", "response_generator") 
graph.add_edge("response_generator", END)

app = graph.compile()

response = app.invoke({
    "name": "Alice",
    "income": 50000,
    "loan_amount": 20000
})

print(response)
