"""Aplicação principal do AtendeBot — servidor Flask."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, jsonify, render_template, request, session

from app.database.db import init_db
from app.dialogue.manager import DialogueManager

app = Flask(__name__)
app.secret_key = os.urandom(24)

_managers: dict[str, DialogueManager] = {}


def _get_manager(session_id: str) -> DialogueManager:
    if session_id not in _managers:
        _managers[session_id] = DialogueManager()
    return _managers[session_id]


@app.route("/")
def index():
    if "session_id" not in session:
        session["session_id"] = os.urandom(16).hex()
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    session_id = data.get("session_id", "default")
    user_message = data["message"]

    manager = _get_manager(session_id)
    response = manager.process_message(user_message)

    return jsonify({
        "response": response,
        "state": manager.state.name,
        "identified": manager.context.get("cliente") is not None,
    })


@app.route("/api/reset", methods=["POST"])
def reset():
    data = request.get_json() or {}
    session_id = data.get("session_id", "default")
    if session_id in _managers:
        del _managers[session_id]
    return jsonify({"status": "ok", "message": "Conversa reiniciada."})


if __name__ == "__main__":
    print("=" * 50)
    print("  AtendeBot — TeleConecta Brasil")
    print("  Inicializando banco de dados...")
    init_db()
    print("  Banco de dados pronto!")
    print("  Iniciando servidor em http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
