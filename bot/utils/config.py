import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    API_KEY =  os.getenv('API_KEY')

    @classmethod
    def check_required(cls):
        if not cls.DISCORD_TOKEN:
            raise ValueError("DISCORD_TOKEN is required in .env file")
        if not cls.API_KEY:
            raise ValueError("API_KEY is required in .env file")