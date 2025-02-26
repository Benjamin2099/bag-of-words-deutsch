import string
from .model import load_model, predict_intent

def tokenize(text):
    """
    Tokenisiert den Eingabetext: Wandelt in Kleinbuchstaben um, entfernt Satzzeichen und teilt nach Leerzeichen.
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return tokens

def bag_of_words(tokenized_sentence, all_words):
    """
    Erstellt einen Bag-of-Words-Vektor basierend auf den Token und einer Liste aller bekannten Wörter.
    """
    bag = [0] * len(all_words)
    for token in tokenized_sentence:
        if token in all_words:
            bag[all_words.index(token)] = 1
    return bag

def process_message(message):
    """
    Verarbeitet die Nachricht: Tokenisierung, Erzeugung des Bag-of-Words-Vektors und Vorhersage des Intents.
    """
    tokens = tokenize(message)
    model = load_model()
    all_words = model.get('all_words', [])
    bag = bag_of_words(tokens, all_words)
    intent = predict_intent(model, bag)
    # Hier könnte man das Intent mit einer Antwort aus einer JSON-Datei mappen
    response = f"Erkannter Intent: {intent}"
    return response
