from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from App Engine!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # ✅ Must use PORT
    app.run(host="0.0.0.0", port=port)        # ✅ Must bind to 0.0.0.0

