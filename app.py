from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
     return "Hello, World!  Delta - airline, Delta8 for high-flyers.  Try it today."
