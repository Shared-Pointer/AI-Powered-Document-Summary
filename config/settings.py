from dotenv import load_dotenv
from pathlib import Path
import os

class Settings:
    def __init__(self):
        load_dotenv(dotenv_path=Path(".env"))
        self.AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "").strip()
        self.AZURE_API_KEY = os.getenv("AZURE_API_KEY", "")
        self.API_VERSION = os.getenv("API_VERSION", "2023-05-15")
        self.MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1"))

settings = Settings()