from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, send_from_directory


app = Flask(__name__)

# Store log files inside flask_example/logs.
logs_dir = Path(__file__).parent / "logs"
logs_dir.mkdir(exist_ok=True)

file_handler = RotatingFileHandler(
    logs_dir / "app.log",
    maxBytes=1_000_000,
    backupCount=5,
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Serve the existing frontend files from the repo root.
project_root = Path(__file__).resolve().parent.parent


@app.route("/")
def home():
    app.logger.info("Frontend home page served")
    return send_from_directory(project_root, "index.html")


@app.route("/styles.css")
def styles():
    return send_from_directory(project_root, "styles.css")


@app.route("/script.js")
def script():
    return send_from_directory(project_root, "script.js")


@app.route("/generate-log")
def generate_log():
    app.logger.warning("Challenge button clicked from frontend")
    return jsonify(status="log written", source="index.html")


if __name__ == "__main__":
    app.run(debug=True)
