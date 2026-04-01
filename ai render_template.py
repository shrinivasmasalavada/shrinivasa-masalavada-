"""
=============================================================
  NovaMind AI Chatbot — Flask Backend
  File: app.py
  Description: Main Flask web application. Handles chat
               messages, loads the trained ML model, stores
               chat history, and serves the frontend.
=============================================================
"""

import os
import json
import pickle
import random
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session

# ─────────────────────────────────────────────
# App Configuration
# ─────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "novamind_secret_key_bca_project_2024"  # Needed for sessions

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "chatbot_model.pkl")
INTENTS_PATH = os.path.join(BASE_DIR, "model", "intents_cache.pkl")
DB_PATH = os.path.join(BASE_DIR, "chat_history.db")

# ─────────────────────────────────────────────
# STEP 1: Load the trained model
# ─────────────────────────────────────────────
def load_model():
    """Load the trained ML pipeline from disk."""
    if not os.path.exists(MODEL_PATH):
        print("⚠️  Model not found! Running training script...")
        os.system(f"python {os.path.join(BASE_DIR, 'train_model.py')}")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(INTENTS_PATH, "rb") as f:
        intents = pickle.load(f)

    print("✅ Model loaded successfully!")
    return model, intents

# Load model once when the app starts
model, intents = load_model()

# ─────────────────────────────────────────────
# STEP 2: Database Setup — Store chat history
# ─────────────────────────────────────────────
def init_db():
    """Create the chat history table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ─────────────────────────────────────────────
# STEP 3: Chat Logic
# ─────────────────────────────────────────────
def get_response(user_message):
    """
    Predict the intent of the user's message and
    return a random response from that intent's responses.
    """
    # Predict the intent tag using our ML model
    predicted_tag = model.predict([user_message.lower()])[0]

    # Get confidence scores for all intents
    probabilities = model.predict_proba([user_message.lower()])[0]
    max_confidence = max(probabilities)

    # If confidence is low, return a fallback response
    if max_confidence < 0.25:
        fallback_intent = next(
            (i for i in intents if i["tag"] == "fallback"), None
        )
        if fallback_intent:
            return random.choice(fallback_intent["responses"]), "fallback", max_confidence

    # Find the matching intent and pick a random response
    for intent in intents:
        if intent["tag"] == predicted_tag:
            response = random.choice(intent["responses"])
            return response, predicted_tag, max_confidence

    return "I'm not sure how to respond to that.", "unknown", 0.0


def save_message(session_id, role, message):
    """Save a chat message to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (session_id, role, message, timestamp) VALUES (?, ?, ?, ?)",
        (session_id, role, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()


def get_chat_history(session_id):
    """Retrieve all chat messages for a given session from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, message, timestamp FROM chat_history WHERE session_id = ? ORDER BY id ASC",
        (session_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [{"role": r[0], "message": r[1], "timestamp": r[2]} for r in rows]


def get_all_sessions():
    """Retrieve all unique session IDs and their message counts."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT session_id, COUNT(*) as msg_count, MAX(timestamp) as last_active
        FROM chat_history
        GROUP BY session_id
        ORDER BY last_active DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()
    conn.close()
    return [{"session_id": r[0], "message_count": r[1], "last_active": r[2]} for r in rows]

# ─────────────────────────────────────────────
# STEP 4: Flask Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main chat page."""
    # Create a new session ID if one doesn't exist
    if "session_id" not in session:
        session["session_id"] = f"session_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    return render_template("index.html", session_id=session["session_id"])


@app.route("/chat", methods=["POST"])
def chat():
    """
    Main chat endpoint. Receives user message via POST,
    generates AI response, saves both to DB, returns JSON.
    """
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    session_id = session.get("session_id", "default")

    # Save user's message
    save_message(session_id, "user", user_message)

    # Get chatbot response
    bot_response, intent_tag, confidence = get_response(user_message)

    # Save bot's response
    save_message(session_id, "bot", bot_response)

    return jsonify({
        "response": bot_response,
        "intent": intent_tag,
        "confidence": round(confidence * 100, 2),
        "timestamp": datetime.now().strftime("%H:%M")
    })


@app.route("/history", methods=["GET"])
def history():
    """Return chat history for the current session."""
    session_id = session.get("session_id", "default")
    messages = get_chat_history(session_id)
    return jsonify({"history": messages})


@app.route("/clear", methods=["POST"])
def clear_session():
    """Start a new session (clears current chat)."""
    session["session_id"] = f"session_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    return jsonify({"message": "New session started!", "session_id": session["session_id"]})


@app.route("/sessions", methods=["GET"])
def sessions():
    """Return a list of all sessions (for admin/analytics view)."""
    all_sessions = get_all_sessions()
    return jsonify({"sessions": all_sessions})


@app.route("/stats", methods=["GET"])
def stats():
    """Return chatbot statistics."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chat_history WHERE role = 'user'")
    total_messages = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT session_id) FROM chat_history")
    total_sessions = cursor.fetchone()[0]
    conn.close()

    return jsonify({
        "total_messages": total_messages,
        "total_sessions": total_sessions,
        "intents_count": len(intents),
        "model_type": "TF-IDF + Logistic Regression"
    })


# ─────────────────────────────────────────────
# STEP 5: Run the App
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("🚀 Starting NovaMind Chatbot Server...")
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)