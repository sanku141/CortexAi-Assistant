from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from cortex_core import cortexActive, speak

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    command = data.get("command", "")
    print(f"Received command: {command}")
    if not command:
        return jsonify({"error": "No command provided"}), 400
    try:
        response = cortexActive(command)
        # speak(response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
