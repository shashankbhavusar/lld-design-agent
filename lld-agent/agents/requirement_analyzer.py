from llm.groq_client import llm
from models.requirement_models import RequirementAnalysis
from prompts.requirement_prompt import SYSTEM_PROMPT
from state import LLDState


def requirement_analyzer(state: LLDState):

    structured_llm = llm.with_structured_output(
        RequirementAnalysis
    )

    response = structured_llm.invoke(

        [
            (
                "system",
                SYSTEM_PROMPT
            ),
            (
                "human",
                state["input_text"]
            )
        ]

    )

    state["requirements"] = response

    return state