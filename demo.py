from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = ["Kiran", "Deep", "Patcha"]
    return render_template("index.html", content=name)

@app.route("/redirect")
def redirector():
    return redirect(url_for("printName", name="Kiran"))

@app.route("/<name>")
def printName(name):
    return f"URL has {name}"

if __name__ == "__main__":
    app.run(debug=True)
