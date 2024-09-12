from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {escape(name)}님"

app.run(debug=True)