from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
     return "Hello, World!  Delta22 - airline, Delta8 for high-flyers.  Try it toooday, or toomorrow..."
