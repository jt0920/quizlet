from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")