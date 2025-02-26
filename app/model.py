import os
from app.config import Config

_model = None

def load_model():
    global _model
    if _model is None:
        model_path = Config.MODEL_PATH
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modell-Datei nicht gefunden unter: {model_path}")
        # Dummy-Implementierung: Ersetze dies durch den tatsächlichen Modell-Ladevorgang mit PyTorch
        _model = {"model": "dummy_model", "all_words": ["hello", "chatbot", "intent"]}
    return _model

def predict_intent(model, bag):
    """
    Dummy-Vorhersagefunktion: Gibt 'greeting' zurück, wenn im Bag etwas erkannt wird.
    """
    if sum(bag) > 0:
        return "greeting"
    return "unknown"
