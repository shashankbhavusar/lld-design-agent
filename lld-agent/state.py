from typing import TypedDict
from models.requirement_models import ProjectAnalysis
from models.planner_models import ExecutionPlan

class LLDState(TypedDict):
    input_text: str
    project_analysis: ProjectAnalysis | None
    execution_plan: ExecutionPlan | None
    # outputs
    flow_dot: str
    architecture_dot: str
    lld_markdown: str
    swagger_json: dict
    figma_json: dict