from parsers import extract_text
from graph import graph


text = extract_text("sample_requirement.pdf")

initial_state = {
    "input_text": text,
    "requirements": {},
    "plan": {},
    "flow_dot": "",
    "architecture_dot": "",
    "lld_markdown": "",
    "swagger_json": {},
    "figma_json": {},
}

result = graph.invoke(initial_state)

print("\nRESULT\n")
print(result["requirements"])