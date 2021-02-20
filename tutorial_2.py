from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def home():
    content = ["tim", "bosco", "tu viejardaaaa"]
    return render_template("index.html", content=content)


if __name__ == '__main__':
    app.run()