from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', '1.0')
    return f'Hello, World! Version: {version}'

if __name__ == '__main__':
    # Get the port from the environment variable 'PORT' or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Run the app on all available interfaces (0.0.0.0)
    app.run(host='0.0.0.0', port=port)
