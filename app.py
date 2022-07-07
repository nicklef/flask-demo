from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Moon!</p>"

@app.route("/<name>")
def hello_name(name):
    return "<p>Hello, " + name + "!</p>"
