import socket
from log import Logger

logger = Logger(__name__).get_logger()

def test_port():
    logger.info("Testing socket")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2) 
            result = s.connect_ex(('127.0.0.1', 8501))
            if result == 0:
                logger.info("8501 is open")
            else:
                logger.error("8501 is closed")
            assert result == 0, "8501 is not available"
    except Exception as e:
        logger.exception(f"An error occured during the test {e}")
        raise
