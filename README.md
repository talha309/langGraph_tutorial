📘 LangGraph Tutorial & Practice Repository

Welcome to my LangGraph learning repository!
This repo contains my practice files, experiments, and example projects as I learn how to build AI agents and state machines using LangGraph.

LangGraph helps you create powerful conversational agents, tools, workflows, and multi-step reasoning pipelines using graphs.
This repo shows my journey from basic nodes → intermediate workflows → multi-node graphs.

🚀 What I’m Learning

This repository includes example projects where I am practicing:

✔ Building simple LangGraph nodes

Mathematical operations

Greeting functions

Processing and transforming input state

✔ Creating state machines

Using TypedDict for clean state management

Building single-node and multi-node graphs

✔ Graph structure

Adding nodes

Adding edges

Using START and END

Returning updated state correctly

✔ Calling a compiled graph

Using .invoke()

Passing input

Reading output

📁 Folder Structure
/langGraph_tutorial
│
├── basic_greeting_agent.py
├── multi_operation_math_agent.py
├── temperature_converter.py
├── loan_approval_flow.py
│
└── README.md


You may see different practice files such as:

Single-node practice agents

*Math agents (+, -, , avg)

Temperature converter

Loan approval workflow (two nodes)

Experiments with TypedDict & state

📚 Examples of What I Built
🧮 1. Multi-Operation Math Agent

A LangGraph that performs:

Addition

Multiplication

Subtraction

Average

Using a single node and returning a result message.

🌡️ 2. Temperature Converter Agent

Converts:

Celsius → Fahrenheit

Fahrenheit → Celsius

Uses clean condition logic + state update.

🟨 3. Loan Approval Flow (Two Nodes)

Node 1: checks income and loan eligibility

Node 2: generates a final approval/denial message

Shows how LangGraph handles branching and multi-step workflows.

🧠 Concepts I’m Practicing

StateGraph()

add_node()

add_edge()

START and END

TypedDict state definitions

Returning updated state

Multi-step agent workflows

Clean error handling

🛠 Requirements

Install dependencies using uv, pip, or your environment:

uv add langgraph


or

pip install langgraph

▶️ How to Run Any Script
uv run your_file_name.py


Example:

uv run multi_operation_math_agent.py

🌟 My Progress

I am actively learning:

LangGraph fundamentals

How to design agents

How to manage state

How to build multi-step logic

How to structure real AI workflows

More examples will be added over time!

🤝 Contributing

This is a personal learning repository,
but feel free to send suggestions or improvements.

📬 Contact

If you want to collaborate or ask something, feel free to reach out.