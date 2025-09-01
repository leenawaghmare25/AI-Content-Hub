from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import firebase_admin
from firebase_admin import auth as fb_auth, credentials
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# --- Firebase Admin Initialization ---
# Expect a service account file path via env var FIREBASE_ADMIN_CREDENTIALS or place serviceAccountKey.json in backend folder
service_account_path = os.getenv("FIREBASE_ADMIN_CREDENTIALS", os.path.join(os.path.dirname(__file__), "serviceAccountKey.json"))
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin initialized")
    except Exception as e:
        print(f"Firebase Admin initialization failed: {e}")

# Initialize the summarization pipeline once at startup
# You can specify a model if desired, e.g., model="sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization")

@app.route("/", methods=["GET"])
def home():
    return "Hello from the Flask Backend!"

# --- Auth helper ---
def verify_id_token(id_token: str):
    if not id_token:
        return None
    try:
        decoded = fb_auth.verify_id_token(id_token)
        return decoded
    except Exception:
        return None

# Endpoint to verify client ID token (optional for session bootstrapping)
@app.route("/auth/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    id_token = data.get("idToken")
    decoded = verify_id_token(id_token)
    if not decoded:
        return jsonify({"ok": False, "error": "Invalid token"}), 401
    return jsonify({"ok": True, "uid": decoded.get("uid"), "email": decoded.get("email")}), 200

@app.route("/summarize", methods=["POST"]) 
def summarize():
    try:
        data = request.get_json(silent=True) or {}
        text = (data.get("text") or "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Optional: protect this endpoint, require a valid Authorization: Bearer <ID_TOKEN>
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.split("Bearer ")[-1] if "Bearer " in auth_header else None
        if token:
            if not verify_id_token(token):
                return jsonify({"error": "Unauthorized"}), 401

        # Run summarization
        result = summarizer(text, max_length=150, min_length=30, do_sample=False)
        summary_text = result[0].get("summary_text", "")
        return jsonify({"summary": summary_text}), 200
    except Exception:
        return jsonify({"error": "Failed to generate summary"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)