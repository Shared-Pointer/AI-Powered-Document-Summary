from log import Logger
import pytest
import os
from src.file_processor import FileProcessor

logger = Logger(__name__).get_logger()

@pytest.mark.parametrize("file_name, expected", [
    (".jpeg", False),
    (".pdf", True),
    (".zip", False),
    (".txt", True),
    (".docx", True),
    (".png", False),
])

def test_is_supported_file(file_name, expected):
    logger.info(f"Testing file: {file_name}")
    file_processor = FileProcessor()
    supp_files = file_processor.supported_types.keys()
    supp_files = list(supp_files)
    ret = file_name in supp_files
    assert ret == expected
