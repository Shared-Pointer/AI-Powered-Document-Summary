from log import Logger
import pytest
#from ../main import main
from ..src import FileProcessor, Summarizer

logger = Logger(__name__).get_logger()

def test_file_name():
    file_procesor = FileProcessor()
    file_procesor.file = "manu.txt"
    #file_procesor.upload_file()
    ret = file_procesor.getFile()
    assert ret != None

