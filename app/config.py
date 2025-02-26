import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    MODEL_PATH = os.getenv('MODEL_PATH')
    INTENTS_PATH = os.getenv('INTENTS_PATH')
    
    @classmethod
    def validate(cls):
        if not cls.MODEL_PATH:
            raise ValueError("MODEL_PATH ist nicht in den Umgebungsvariablen gesetzt.")
        if not cls.INTENTS_PATH:
            raise ValueError("INTENTS_PATH ist nicht in den Umgebungsvariablen gesetzt.")
