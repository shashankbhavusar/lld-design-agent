from docx import Document


def parse_docx(file_path: str) -> str:
    document = Document(file_path)

    text = "\n".join(
        para.text for para in document.paragraphs
    )

    return text.strip()