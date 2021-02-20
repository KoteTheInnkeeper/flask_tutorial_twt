from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO</h1>"


@app.route("/<name>")
def hello(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))    # Is the function's name (under the 'app.route' decorator) what the argument for 'url_for' has to be.


if __name__ == '__main__':
    app.run()
