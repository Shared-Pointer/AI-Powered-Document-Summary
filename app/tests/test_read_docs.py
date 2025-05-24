import pytest
from src.file_processor import FileProcessor

def test_read_docx():
    file_processor = FileProcessor()
    with open("../../data/input/fanatyk.docx", "rb") as file:
        file_processor.file = file
        file_processor.file_type = ".txt"
        content = file_processor._read_docx
        assert len(content) > 0, "Your summarize is empty"