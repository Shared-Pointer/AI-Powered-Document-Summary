import pytest
import os
from src.file_processor import FileProcessor

def test_read_docx():
    file_processor = FileProcessor()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/input"))
    file_path = os.path.join(base_dir, "fanatyk.docx")
    with open(file_path, "rb") as file:
        file_processor.file = file
        file_processor.file_type = ".txt"
        content = file_processor._read_docx
        assert len(content) > 0, "Your summarize is empty"