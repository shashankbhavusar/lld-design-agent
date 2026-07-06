from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class ProjectType(str, Enum):
    WEB_APPLICATION = "Web Application"
    MOBILE_APPLICATION = "Mobile Application"
    REST_API = "REST API"
    MICROSERVICE = "Microservice"
    DESKTOP_APPLICATION = "Desktop Application"
    CLI_APPLICATION = "CLI Application"
    LIBRARY = "Library"
    DATA_PIPELINE = "Data Pipeline"
    UNKNOWN = "Unknown"


class Complexity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class FunctionalRequirement(BaseModel):
    id: str
    description: str


class NonFunctionalRequirement(BaseModel):
    description: str


class ProjectAnalysis(BaseModel):

    project_name: str

    summary: str

    project_type: ProjectType

    complexity: Complexity

    target_users: List[str]

    modules: List[str]

    functional_requirements: List[FunctionalRequirement]

    non_functional_requirements: List[NonFunctionalRequirement]

    assumptions: List[str]

    dependencies: List[str]