import socket
from log import Logger
import pytest

logger = Logger(__name__).get_logger()

def test_port():
    logger.info("Testing socket")
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) 
    result = s.connect_ex(('127.0.0.1', 8501))

    assert result == 0, "8501 is not available"
    logger.info("Socket test passed")
