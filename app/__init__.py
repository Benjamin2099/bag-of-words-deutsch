import os
from flask import Flask
from dotenv import load_dotenv
from .config import Config
from .extensions import configure_logging
from .routes import chat_blueprint

def create_app():
    # Lade Umgebungsvariablen aus .env
    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Validierung der Konfiguration
    try:
        Config.validate()
    except ValueError as e:
        app.logger.error(f"Konfigurationsfehler: {e}")
        raise

    # Logging konfigurieren
    configure_logging(app)
    
    # Blueprints registrieren
    app.register_blueprint(chat_blueprint, url_prefix='/api')
    
    return app
