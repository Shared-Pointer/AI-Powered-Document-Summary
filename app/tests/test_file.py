from log import Logger
import pytest
#from ../main import main
from src.file_processor import FileProcessor

logger = Logger(__name__).get_logger()

def test_file_name():
    file_procesor = FileProcessor()
    file_procesor.file = "test.txt"
    file_procesor.file = "test.docx"
    #file_procesor.upload_file()
    ret = file_procesor.getFile()
    assert ret != None

