from log import Logger
import pytest
import os

logger = Logger(__name__).get_logger()

def test_file_ext(file_name: str) -> bool:
    supported_extensions = {".txt"}
    
    _, ext = os.path.splitext(file_name)

    if any(file_name.endswith(ext) for ext in supported_extensions):
        logger.info(f"Type {ext} is supported")
        return True
    else:
        logger.error(f"Type {ext} isn't supported")
        return False

@pytest.mark.parametrize("file_name, expected", [
    ("image.jpeg", False),
    ("document.pdf", False),
    ("archive.zip", False),
    ("notes.txt", True),
    ("image.png", False),
])

def test_is_supported_file(file_name, expected):
    logger.info(f"Testing file: {file_name}")
    assert test_file_ext(file_name) == expected
