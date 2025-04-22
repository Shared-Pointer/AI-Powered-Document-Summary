from log import Logger

logger = Logger(__name__).get_logger()

def test_file_name(file):
    try:
        if file is not None:
            logger.info(f"File name is: {file.name}")
        else:
            logger.error("There is an error in retrieving name")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
