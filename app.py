from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', '1.0')
    return f'Hello, Hugo here! This is a test version. Version: {version}'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
