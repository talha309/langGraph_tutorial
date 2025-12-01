from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
   scale: str
   value: int
   result: str

def converter_temp(state: AgentState) -> AgentState:
   scale = state['scale']
   if scale == "CtoF":
      F = state['value'] * 9/5 + 32
      state['result']= f"Converted temperature is = {F}"
      return state
   elif scale == "FtoC":
      C = (state['value'] - 32) * 5/9
      state['result']= f"Converted temperature is = {C}"
      return state
   else:
      state['result'] = f"Invalid scale. Use CtoF or FtoC"
      return state
   
graph = StateGraph(AgentState)
graph.add_node("converter",converter_temp)
graph.add_edge(START, "converter")
graph.add_edge("converter",END)

app= graph.compile()

answer= app.invoke({
   
   "scale": "CtoF",
   "value": 453

})
print (answer)