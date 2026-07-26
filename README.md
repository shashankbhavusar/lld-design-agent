# AI Software Architect - LLD Generator Agent

An AI-powered Software Architecture Assistant that converts software requirements into complete Low Level Design (LLD) documents.

The system analyzes requirements, creates an execution plan, generates multiple software engineering artifacts, and finally produces a professional LLD document.

The goal of this project is to automate the initial software design phase using LLMs, LangGraph workflows, structured generation, and artifact-based architecture.

---

# Project Overview

Designing a software system requires multiple activities:

- Understanding business requirements
- Identifying system components
- Designing architecture
- Creating UML diagrams
- Defining APIs
- Designing database structures
- Preparing technical documentation

This project automates these activities using an AI-driven architecture workflow.

Given a project requirement, the agent can generate:

- Architecture Diagram
- Flow Diagram
- Class Diagram
- Sequence Diagram
- Database Schema
- Swagger API Specification
- Figma UI Design Specification
- Complete LLD Document

---

# High Level Architecture

The system follows a planner-executor architecture implemented using LangGraph.

```
                    User Requirement
                           |
                           |
                           v
              Requirement Analysis Agent
                           |
                           |
                           v
                    Planning Agent
                           |
                           |
                    Execution Plan
                           |
                           |
                           v
                  Execution Manager
                           |
        ---------------------------------------
        |          |          |              |
        v          v          v              v

 Flow Generator  Class   Swagger       Architecture
                Generator Generator     Generator

        |
        |
        v

 Sequence Generator
 Figma Generator
 Database Generator

        |
        |
        v

              LLD Generator

        |
        |
        v

          Markdown / HTML LLD
```

---

# LangGraph Workflow

The complete workflow:

```
START

 |
 |
 v

Requirement Analyzer

 |
 |
 v

Planner Agent

 |
 |
 v

Execution Manager

 |
 |
 +-----------------------------+
                               |
                               v

                     Artifact Generation

                               |
          -----------------------------------------
          |          |          |          |
          v          v          v          v

      Diagrams   Swagger    Figma   Database

          |
          |
          v

              LLD Document Generator

          |
          |
          v

              Final Output

          |
          |
          v

             END
```

---

# Core Components

## 1. Requirement Analyzer

The requirement analyzer extracts structured information from user requirements.

It identifies:

- Project summary
- Functional requirements
- Non-functional requirements
- Modules
- Dependencies
- Assumptions
- Complexity

Example:

Input:

```
Build an Employee Leave Management System
```

Output:

```
Modules:

- Employee Login
- Leave Application
- Leave Approval
- Leave Balance
- Notifications
- HR Administration
```

---

# 2. Planning Agent

The planning agent acts as the decision-making engine.

It does not generate artifacts.

Responsibilities:

- Identify required artifacts
- Assign priorities
- Identify dependencies
- Decide execution order

Example:

```json
{
  "artifact": "Class Diagram",
  "priority": 2,
  "depends_on": []
}
```

The planner ensures only valuable artifacts are generated.

---

# 3. Execution Manager

The execution manager controls artifact generation.

Responsibilities:

- Select next executable task
- Validate dependencies
- Maintain execution state
- Trigger required plugins

Example workflow:

```
Architecture Diagram

        |
        v

Class Diagram

        |
        v

Swagger

        |
        v

LLD Document
```

---

# Plugin Based Architecture

The project follows a plugin-based generator architecture.

Each artifact generator works independently.

Structure:

```
plugins/

├── architecture_generator.py
├── flow_generator.py
├── class_generator.py
├── sequence_generator.py
├── swagger_generator.py
├── figma_generator.py
└── lld_generator.py
```

Generators are registered using a central registry.

Example:

```python
PLUGIN_REGISTRY = {

    ArtifactType.FLOW_DIAGRAM:
        FlowGenerator(),

    ArtifactType.CLASS_DIAGRAM:
        ClassGenerator(),

    ArtifactType.SWAGGER:
        SwaggerGenerator(),

    ArtifactType.LLD_DOCUMENT:
        LLDGenerator()
}
```

This allows adding new artifact generators without changing the workflow.

---

# Generated Artifacts

## Architecture Diagram

Generated using Graphviz.

Represents:

- System components
- External services
- Application layers
- Data flow

Example:

```
User

 |

Frontend

 |

Backend API

 |

Database

 |

External Services
```

Output:

```
architecture.png
```

---

# Flow Diagram

Represents business workflows.

Example:

Employee Leave Workflow:

```
Login

 |

Apply Leave

 |

Manager Approval

 |

Notification

 |

Update Leave Balance
```

Generated using:

- Mermaid
- Graphviz

Output:

```
flow.png
flow.mmd
```

---

# Class Diagram

Generates object-oriented design.

Includes:

- Classes
- Attributes
- Methods
- Relationships

Example:

```
Employee

     |
     |

LeaveRequest

     |
     |

Approval
```

Output:

```
class_diagram.mmd
```

---

# Sequence Diagram

Represents runtime interactions between components.

Example:

```
Employee

   |
   v

Leave Service

   |
   v

Database

   |
   v

Notification Service
```

Generated using Mermaid.

---

# Swagger API Specification

Generates OpenAPI documentation.

Includes:

- REST endpoints
- HTTP methods
- Request models
- Response models
- API contracts

Output:

```
openapi.yaml
```

---

# Figma UI Design Specification

Generates UI design information.

Includes:

- Screens
- Components
- Layout structure
- User interactions

Output:

```
figma.json
```

---

# LLD Generation

The final stage combines all generated artifacts into a complete Low Level Design document.

Generated sections include:

- Project Overview
- Functional Requirements
- Non Functional Requirements
- System Overview
- Component Design
- Architecture Design
- Flow Design
- Class Design
- Sequence Design
- API Design
- UI Design
- Security Considerations
- Scalability Considerations

Output:

```
output/lld/

├── lld.md
└── lld.html
```

---

# HTML LLD Viewer

The project also generates a browser-friendly HTML version.

Features:

- Rendered diagrams
- Mermaid visualization
- Formatted documentation
- Syntax highlighting

Example:

```
lld.html
```

can be opened directly in a browser.

---

# Project Structure

```
lld-agent/

│
├── app.py
├── state.py
│
├── graph/
│   └── workflow.py
│
├── nodes/
│   ├── planner.py
│   ├── generator.py
│   └── execution_manager.py
│
├── models/
│   ├── requirement_models.py
│   ├── planner_models.py
│   ├── flow_models.py
│   └── lld_models.py
│
├── plugins/
│   ├── architecture_generator.py
│   ├── flow_generator.py
│   ├── class_generator.py
│   ├── sequence_generator.py
│   ├── swagger_generator.py
│   ├── figma_generator.py
│   └── lld_generator.py
│
├── services/
│   ├── requirement_service.py
│   ├── class_diagram_service.py
│   ├── swagger_service.py
│   └── lld_service.py
│
├── renderers/
│   ├── graphviz_renderer.py
│   ├── mermaid_renderer.py
│   └── html_renderer.py
│
├── prompts/
│
└── output/
```

---

# Technology Stack

## AI / Agent Framework

- LangGraph
- LangChain
- Groq LLM

## Backend

- Python
- Pydantic

## Diagram Generation

- Mermaid
- Graphviz

## Documentation

- Markdown
- HTML

## API Design

- OpenAPI / Swagger

---

# Installation

Clone repository:

```bash
git clone <repository-url>

cd lld-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=<your_api_key>
```

---

# Running the Project

Execute:

```bash
python app.py
```

Generated artifacts:

```
output/

├── architecture/
├── flow/
├── class_diagram/
├── sequence/
├── swagger/
├── figma/
└── lld/
```

---

# Example Input

```
Design an Employee Leave Management System.

Employees should apply for leave.
Managers should approve requests.
HR should manage policies.
Employees should receive notifications.
```

---

# Generated Output

The system generates:

```
Architecture Diagram

Flow Diagram

Class Diagram

Sequence Diagram

Swagger Specification

Figma Design

Complete LLD Document
```

---

# Design Principles

## Separation of Responsibilities

Each component has a clear responsibility:

- Planner decides what to generate
- Execution Manager controls workflow
- Plugins generate artifacts
- Services implement generation logic

---

## Extensibility

New artifact generators can be added without modifying existing workflow.

---

## Structured Generation

LLM responses are controlled using:

- Pydantic models
- Structured outputs
- Validation

---

# Future Enhancements

- Support PDF/DOCX requirement input
- Cloud deployment
- Multi-project workspace
- LLD version management
- Architecture Decision Record generation
- Code skeleton generation
- CI/CD pipeline design generation

---

# Author

Shashank H T

AI Software Architect Agent built using LangGraph and LLM-based orchestration.
