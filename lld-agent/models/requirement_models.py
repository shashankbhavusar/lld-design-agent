from typing import List

from pydantic import BaseModel, Field


class FunctionalRequirement(BaseModel):
    id: str = Field(description="Unique requirement id")
    description: str


class NonFunctionalRequirement(BaseModel):
    description: str


class RequirementAnalysis(BaseModel):

    project_name: str

    summary: str

    functional_requirements: List[FunctionalRequirement]

    non_functional_requirements: List[NonFunctionalRequirement]

    assumptions: List[str]