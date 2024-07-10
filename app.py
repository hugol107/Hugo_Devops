from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', '1.0')
    return f'Hello, Marc! This is a test version. Version: {version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
