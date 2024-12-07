from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    OPEN_WEBUI_URL = os.getenv("OPEN_WEBUI_URL")
    API_KEY = os.getenv("API_KEY")
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = os.getenv("PORT", 11434)
    DEBUG = os.getenv("DEBUG", False)
