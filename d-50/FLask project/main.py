from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return '<h1>good morning<h1>' \
    '<a href = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZNP055bl-sNYr3eznKkyZFb_UwD2I7JYn7Q77J-DuuQ&s=10">wake up is morning</a>'\
    '<img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuNmuhVyOgKHFi7QLM3jKRktTW9RF6LE3BdsIN6mqxMg&s=10">'

@app.route("/<name>")
def good_bye(name):
    return f"bye {name}"

app.run()






