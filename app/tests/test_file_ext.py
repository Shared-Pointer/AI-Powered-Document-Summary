from log import Logger
import pytest
import os
from src import FileProcessor

logger = Logger(__name__).get_logger()

# def test_file_ext(file_name: str) -> bool:
#     supported_extensions = {".txt"}
    
#     _, ext = os.path.splitext(file_name)

#     if any(file_name.endswith(ext) for ext in supported_extensions):
#         logger.info(f"Type {ext} is supported")
#         return True
#     else:
#         logger.error(f"Type {ext} isn't supported")
#         return False

@pytest.mark.parametrize("file_name, expected", [
    (".jpeg", False),
    (".pdf", False),
    (".zip", False),
    (".txt", True),
    (".png", False),
])

def test_is_supported_file(file_name, expected):
    logger.info(f"Testing file: {file_name}")
    file_processor = FileProcessor()
    supp_files = file_processor.supported_types.keys()
    supp_files = list(supp_files)
    ret = file_name in supp_files
    assert ret == expected
