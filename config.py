import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", 'dev_secret_key')
    DEBUG = os.getenv("FLASK_DEBUG", True)