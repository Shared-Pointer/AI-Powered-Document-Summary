from pathlib import Path
import pytest
from dotenv import load_dotenv

# to load env variables to an interactive session for tests to work run the export $(grep -v '^#' .env | xargs) command

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv(dotenv_path=Path("../../../config/.env"))