from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "I am the Home Page"

@app.route("/redirect")
def redirector():
    return redirect(url_for("printName", name="Kiran"))

@app.route("/<name>")
def printName(name):
    return f"URL has {name}"

if __name__ == "__main__":
    app.run(debug=True)
