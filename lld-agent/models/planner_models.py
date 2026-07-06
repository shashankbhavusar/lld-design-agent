from enum import Enum

from pydantic import BaseModel, Field


class ArtifactType(str, Enum):
    FLOW_DIAGRAM = "Flow Diagram"
    ARCHITECTURE_DIAGRAM = "Architecture Diagram"
    CLASS_DIAGRAM = "Class Diagram"
    SEQUENCE_DIAGRAM = "Sequence Diagram"
    DATABASE_SCHEMA = "Database Schema"
    LLD_DOCUMENT = "LLD Document"
    SWAGGER = "Swagger"
    FIGMA = "Figma"


class ArtifactPlan(BaseModel):

    artifact: ArtifactType

    priority: int = Field(
        description="Lower number means execute earlier."
    )

    parallel: bool = Field(
        description="Can run concurrently with other tasks."
    )

    depends_on: list[ArtifactType] = Field(default_factory=list)

    description: str = Field(
        description="Why this artifact is required."
    )


class ExecutionPlan(BaseModel):
    tasks: list[ArtifactPlan]
    reasoning: str