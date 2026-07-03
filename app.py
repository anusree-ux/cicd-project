from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask CI/CD App!"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "Application is healthy"
    })

@app.route('/about')
def about():
    return jsonify({
        "project": "CI/CD Pipeline Project",
        "framework": "Flask",
        "version": "1.0"
    })

@app.route('/github-webhook/', methods=['POST'])
def github_webhook():
    payload = request.json
    print("Received webhook:")
    print(payload)
    return jsonify({"message": "Webhook received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
