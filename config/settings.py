from dotenv import load_dotenv
from pathlib import Path
import os

class Settings:
    def __init__(self):
        load_dotenv(dotenv_path=Path(".env"))
        self.API_KEY = os.getenv("API_KEY", "")
        self.BASE_URL = os.getenv("BASE_URL", "")
        self.MODEL = os.getenv("MODEL", "")

settings = Settings()