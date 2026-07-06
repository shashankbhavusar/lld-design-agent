from typing import TypedDict
from models.requirement_models import RequirementAnalysis

class LLDState(TypedDict):
    input_text: str
    requirements: RequirementAnalysis | None
    plan: dict
    # outputs
    flow_dot: str
    architecture_dot: str
    lld_markdown: str
    swagger_json: dict
    figma_json: dict