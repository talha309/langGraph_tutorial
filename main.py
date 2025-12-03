import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI

# --- 1. Environment Setup ---
# Load environment variables from a .env file (e.g., GEMINI_API="YOUR_KEY_HERE")
load_dotenv()

# The Google GenAI key will be read from the environment variable 
# 'GEMINI_API' which is passed via os.getenv("GEMINI_API").

# FIX: Changed model to "gemini-2.5-flash" to resolve the NotFound error.
# 'gemini-2.5-flash' is the modern, supported chat model.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=os.getenv("GEMINI_API")
)


# --- 2. LangGraph State Definition ---
# Defines the schema for the data passed between nodes in the graph.
class MessagesState(TypedDict):
    """
    Represents the state of our graph.
    - output: The LLM's response.
    - user_input: The user's initial query.
    """
    output: str
    user_input: str


# --- 3. LangGraph Node Function ---
def assistant(state: MessagesState):
    """
    Node function that invokes the Gemini LLM with the user's input.
    """
    # Get the user's query from the state
    user_query = state["user_input"]
    print(f"🤖 Assistant received query: '{user_query}'")

    # Invoke the Gemini model
    # Note: .invoke() returns a BaseMessage object from which we extract content
    response = llm.invoke(user_query).content

    # Update the state with the model's output
    return {"output": response}


# --- 4. LangGraph Workflow Definition ---
# Build the graph
graph = StateGraph(MessagesState)

# Add the 'assistant' function as a node
graph.add_node("assistant", assistant)

# Define the workflow: start at the 'assistant' node
graph.add_edge(START, "assistant")

# Define the finish line: after the 'assistant' node, the workflow ends
graph.add_edge("assistant", END)

# Compile the graph for execution
app = graph.compile()


# --- 5. FastAPI Application Setup ---
app = FastAPI()

@app.get("/chat/{query}")
def get_content(query: str):
    """
    API endpoint to interact with the LangGraph workflow.
    """
    print(f"🌍 Received request query: {query}")
    try:
        # Invoke the compiled graph with the user's query as the initial state
        # The result is the final state dictionary
        result = app.invoke({"user_input": query})

        # The 'result' is a dictionary, e.g., {'output': '...', 'user_input': '...'}
        # We return the 'output' key for a clean API response.
        return {"output": result["output"]}
        
    except Exception as e:
        # Return the error message if something goes wrong
        # (e.g., if the GEMINI_API key is still invalid)
        print(f"❌ Error during graph invocation: {e}")
        return {"output": f"An error occurred: {str(e)}"}

# --- 6. How to Run ---
# Command to run: 
# poetry run uvicorn app:app --reload