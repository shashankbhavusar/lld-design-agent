from langgraph.graph import StateGraph, END

from state import LLDState
from nodes.requirement_analyzer import requirement_analyzer
from nodes.planner import planner


builder = StateGraph(LLDState)

builder.add_node(
    "requirement_analyzer",
    requirement_analyzer,
)

builder.add_node(
    "planner",
    planner
)


builder.set_entry_point("requirement_analyzer")


builder.add_edge(
    "requirement_analyzer",
    "planner"
)

builder.add_edge(
    "planner",
    END
)

graph = builder.compile()