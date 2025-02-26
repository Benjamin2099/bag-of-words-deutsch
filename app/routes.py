from flask import Blueprint, request, jsonify, current_app
from .nlp_utils import process_message
from functools import lru_cache

chat_blueprint = Blueprint('chat', __name__)

@lru_cache(maxsize=128)
def cached_response(message):
    return process_message(message)

@chat_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        current_app.logger.error("Ungültige Eingabe: 'message' fehlt.")
        return jsonify({"error": "Ungültige Eingabe, 'message' ist erforderlich."}), 400

    message = data['message']
    
    try:
        response = cached_response(message)
    except Exception as e:
        current_app.logger.exception("Fehler bei der Nachrichtenverarbeitung:")
        return jsonify({"error": "Fehler bei der Nachrichtenverarbeitung."}), 500

    return jsonify({"response": response})
