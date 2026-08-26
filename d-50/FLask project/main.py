from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "hello world"

@app.route("/bye/<name>")
def good_bye(name):
    return f"bye {name}"

app.run()

