from langgraph.graph import StateGraph, END

from state import LLDState
from agents.requirement_analyzer import requirement_analyzer


builder = StateGraph(LLDState)

builder.add_node(
    "requirement_analyzer",
    requirement_analyzer,
)

builder.set_entry_point("requirement_analyzer")

builder.add_edge(
    "requirement_analyzer",
    END,
)

graph = builder.compile()