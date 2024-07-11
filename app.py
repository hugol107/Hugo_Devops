from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', '1.0')
    return f'Hello, World! Version: {version}'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"PORT environment variable: {os.environ.get('PORT')}")
    print(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)
