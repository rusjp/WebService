from flask import Flask, render_template, request, jsonify
import subprocess
import time
import socket
import json

# Read settings from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# User Configurable Settings from JSON
START_COMMAND_STR = config['START_COMMAND_STR']
STOP_COMMAND_STR = config['STOP_COMMAND_STR']
RESTART_COMMAND_STR = config['RESTART_COMMAND_STR']
STATUS_COMMAND_STR = config['STATUS_COMMAND_STR']
APP_TITLE = config['APP_TITLE']

# Flask Config from JSON
FLASK_HOST = config['FLASK_HOST']
FLASK_PORT = config['FLASK_PORT']
FLASK_DEBUG = config['FLASK_DEBUG']

# Internal Constants (Do not change)
# Convert string commands to lists
START_COMMAND = START_COMMAND_STR.split()
STOP_COMMAND = STOP_COMMAND_STR.split()
RESTART_COMMAND = RESTART_COMMAND_STR.split()
STATUS_COMMAND = STATUS_COMMAND_STR.split()

# Initialize Flask app
app = Flask(__name__)

# Function to get the IP address of the server
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# Define route for the index page
@app.route("/")
def index():
    ip_address = get_ip_address()
    return render_template("index.html", title=APP_TITLE, ip_address=ip_address)

# Define route for triggering actions like start, stop, restart
@app.route("/action", methods=["GET", "POST"])
def action():
    if request.method == "POST":
        command = request.json.get("command")
    else:  # GET request
        command = request.args.get("command")

    command_map = {
        "start": START_COMMAND,
        "stop": STOP_COMMAND,
        "restart": RESTART_COMMAND
    }

    if command in command_map:
        subprocess.run(command_map[command])
        time.sleep(2)

    status_result = subprocess.run(STATUS_COMMAND, capture_output=True, text=True)
    return jsonify(status=status_result.stdout)

# Entry point for the application
if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
