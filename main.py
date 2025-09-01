from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ App is working!'

@app.route('/healthz')
def healthz():
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # required for App Engine
    app.run(host='0.0.0.0', port=port)        # bind to external host
