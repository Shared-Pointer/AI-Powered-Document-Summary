import logging

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():
            self._configure_logger()

    def _configure_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d T%H:%M:%SZ'
        )

    def get_logger(self):
        return self.logger
