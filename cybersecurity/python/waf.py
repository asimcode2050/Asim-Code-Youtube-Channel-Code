# Basic Web Application Firewall
from flask import Flask, request, jsonify
app = Flask(__name__)  # Create a Flask application
BLOCKED_IPS = ["192.168.1.100", "10.0.0.5"]


@app.before_request
def block_ips():
    if request.remote_addr in BLOCKED_IPS:
        return jsonify({"error": "Access denied"}), 403


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is protected data."})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
