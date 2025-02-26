# bag-of-words-deutsch

## 1. Projektübersicht (README.md)
**Projektbeschreibung:**  
Der Chatbot wird über Flask als Webserver betrieben und verarbeitet Benutzereingaben mittels eines Bag-of-Words-Ansatzes. Mithilfe eines vortrainierten PyTorch-Modells werden die Intents der Nutzer erkannt, um passende Antworten zu generieren.

**Features:**  
- Flask-basierte RESTful API (/chat)
- NLP-Verarbeitung (Tokenisierung, Bag-of-Words)
- Vortrainiertes PyTorch-Modell zur Intent-Erkennung
- Modularer Aufbau (Flask Blueprints, klare Trennung von Logik, Modell und Utilities)
- Thematische Erweiterungen im Branch "Mr.robot"
- Erweiterte Fehlerbehandlung, Logging und Unit-Tests

## 2. About – Repository-Beschreibung (auf GitHub)
**Kurzbeschreibung:**  
bag-of-words-deutsch – Ein einfacher, modularer Chatbot mit Bag-of-Words-Ansatz und thematischen Anpassungen à la Mr. Robot.

**Schlagwörter (Topics):**  
Flask, Chatbot, NLP, PyTorch, API, Mr.Robot

**Lizenz:**  
Dieses Projekt steht unter der Apache License 2.0 (siehe LICENSE-Datei).

## 3. Wichtige Dateien und Konfiguration
**.env**  
Eine Beispielkonfigurationsdatei, die notwendige Umgebungsvariablen definiert. Beispiel:

MODEL_PATH=path/to/your/model.pth  
INTENTS_PATH=path/to/your/intents.json  
FLASK_ENV=development  
DEBUG=True

**requirements.txt:**  
Enthält alle Python-Abhängigkeiten (z. B. Flask, torch, python-dotenv, pytest, flask-caching).

**.gitignore:**  
Sorgt dafür, dass sensible oder unnötige Dateien (wie .env, virtuelle Umgebungen, Cache-Dateien) nicht ins Repository gelangen. Beispiel:

__pycache__/  
*.pyc  
venv/  
.env  
*.log

## 4. Git und Hochladen auf GitHub
Folge diesen Schritten, um das Repository korrekt hochzuladen:

Repository initialisieren (falls noch nicht geschehen):

    git init

Alle Dateien zum Commit hinzufügen:

    git add .

Commit erstellen:

    git commit -m "Initial commit: Flask Chatbot BoW Basis und Mr.robot Branch-Inhalte"

Remote-Repository hinzufügen:  
Erstelle ein neues Repository auf GitHub und füge die Remote-URL hinzu:

    git remote add origin https://github.com/DeinBenutzername/flask-chatbot-BoW-.git

Änderungen pushen:

    git push -u origin master

(Falls du in einem speziellen Branch wie "Mr.robot" arbeitest, wechsle vorher in diesen Branch und pushe entsprechend.)

## 5. Zusätzliche Tipps und Hinweise
- **Dokumentation erweitern:**  
  Ergänze bei Bedarf zusätzliche Dokumentationsdateien wie CONTRIBUTING.md oder CHANGELOG.md, um den Entwicklungsprozess und Änderungen transparent zu machen.
  
- **CI/CD:**  
  Richte automatisierte Pipelines (z. B. mit GitHub Actions) ein, um bei jedem Commit automatisierte Tests und Builds auszuführen.
  
- **Sicherheitsüberprüfung:**  
  Achte darauf, dass keine sensiblen Daten (wie der Inhalt der .env-Datei) in das Repository gelangen. Passe deine .gitignore entsprechend an.
  
- **Branch-Strategie:**  
  Nutze klare Branch-Strukturen (z. B. master/main für stabile Releases, development für laufende Entwicklungen sowie spezielle Branches wie "Mr.robot").

## Installation

Repository klonen und in den Branch "Mr.robot" wechseln:

    git clone https://github.com/Benjamin2099/flask-chatbot-BoW-.git
    cd flask-chatbot-BoW-
    git checkout Mr.robot

Virtuelle Umgebung erstellen und aktivieren:

Unter Linux/MacOS:

    python3 -m venv venv
    source venv/bin/activate

Unter Windows:

    python -m venv venv
    venv\Scripts\activate

Abhängigkeiten installieren:

    pip install -r requirements.txt

Konfiguration einrichten:  
Kopiere .env.example zu .env und passe die Einträge (z. B. MODEL_PATH und INTENTS_PATH) an:

    cp .env.example .env

Anwendung starten:

    python run.py

Die Anwendung läuft standardmäßig auf http://127.0.0.1:3030.

## Usage

Um den Chatbot zu nutzen, sende eine POST-Anfrage an den API-Endpunkt /chat mit einem JSON-Payload:

Payload:

{
  "message": "Hallo, Chatbot!"
}

Antwort:

{
  "response": "Erkannter Intent: greeting"
}

## Testing

Führe die Unit-Tests mit pytest aus, um die Funktionalität der API und der NLP-Komponenten zu überprüfen:

    pytest

## Contributing

Beiträge sind herzlich willkommen! Bitte beachte folgende Hinweise:

- Folge den gängigen GitHub-Richtlinien.
- Achte auf aussagekräftige Commit-Messages.
- Ergänze bei Bedarf neue Tests, um deine Änderungen abzusichern.
- Erstelle ein Issue oder einen Pull Request bei Verbesserungsvorschlägen oder Fehlern.

## License

Dieses Projekt steht unter der Apache License 2.0. Weitere Informationen findest du in der LICENSE-Datei.
