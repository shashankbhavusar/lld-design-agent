from pathlib import Path

from .pdf_parser import parse_pdf
from .docx_parser import parse_docx
from .text_parser import parse_text


def extract_text(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return parse_pdf(file_path)

    if ext == ".docx":
        return parse_docx(file_path)

    if ext == ".txt":
        return parse_text(file_path)

    raise ValueError(f"Unsupported file type: {ext}")