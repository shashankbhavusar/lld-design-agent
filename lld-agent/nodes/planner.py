from llm.groq_client import llm

from models.planner_models import ExecutionPlan

from prompts.planner_prompt import SYSTEM_PROMPT

from state import LLDState


def planner(state: LLDState):

    structured_llm = llm.with_structured_output(
        ExecutionPlan
    )

    response = structured_llm.invoke(
        [
            (
                "system",
                SYSTEM_PROMPT
            ),
            (
                "human",
                state["project_analysis"].model_dump_json(indent=2)
            )
        ]
    )

    state["execution_plan"] = response

    return state