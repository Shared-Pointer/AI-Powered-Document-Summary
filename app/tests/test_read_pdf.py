import pytest
from src.file_processor import FileProcessor


def test_read_pdf():
    file_processor = FileProcessor()
    with open("../../data/input/fanatyk.pdf", "rb") as file:
        file_processor.file = file
        file_processor.file_type = ".pdf"
        content = file_processor._read_pdf()
        assert len(content) > 0, "Your summarize is empty"
    