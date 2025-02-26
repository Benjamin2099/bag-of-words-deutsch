import logging
from logging.handlers import RotatingFileHandler

def configure_logging(app):
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
