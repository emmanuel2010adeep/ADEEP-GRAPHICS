from flask import Flask, render_template, jsonify
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "data" / "content.json"


def load_content():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def home():
    return render_template("index.html", content=load_content())


@app.route("/api/content")
def api_content():
    return jsonify(load_content())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
