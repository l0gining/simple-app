from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevSecOps Lab Application",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/user/<username>')
def get_user(username):
    return jsonify({
        "username": username,
        "role": "user"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

