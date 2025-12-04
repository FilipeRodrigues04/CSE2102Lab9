from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_TOKENS = {
    "phillip.bradford@uconn.edu": "925a4dfa-86b7-4c06-8f3e-fdccb0a748b2"
}

@app.route("/")
def home():
    return "Server is running."

@app.route("/login", methods=["POST"])
def login():
    auth = request.form

    user_id = auth.get("id")
    token = auth.get("uuid-token")

    if not user_id or not token:
        return jsonify({"status": "error", "message": "Missing fields"}), 400
    
    if user_id in VALID_TOKENS and VALID_TOKENS[user_id] == token:
        return jsonify({"status": "success", "message": "Token accepted"})
    else:
        return jsonify({"status": "fail", "message": "Invalid token"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
