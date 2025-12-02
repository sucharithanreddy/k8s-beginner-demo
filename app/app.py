from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Kubernetes! 🚀")
    return jsonify({
        "message": message,
        "version": "v1",
        "environment": os.getenv("APP_ENV", "dev")
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


