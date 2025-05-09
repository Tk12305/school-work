from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Hello World!"})  # Fixed typo: jonsify -> jsonify

if __name__ == "__main__":
    app.run(debug=True)