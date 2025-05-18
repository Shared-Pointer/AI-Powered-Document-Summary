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

quality = {
    'excellent':'approximately 2/3 of the original',
    'good':'approximately 1/2 of the original',
    'crapy':'approximately 1/3 of the original',
}

length = {
    'long':'high coherence, accurate, well-structured',
    'mid':'average quality, some simplifications allowed',
    'short':'intentionally lower quality, possibly missing key points or slightly incoherent',
}

language = {
    'Polish':'only Polish words',
    'English':'only English words',
    'German':'only German words',
    'French':'only French words',
    'Japanese':'only Japanese words',
    'Spanish':'only Spanish words',
    'Danish':'only Danish words',
    'Chinese':'only Chinese words',
}