from django.shortcuts import render
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/stage0")
def stage0():
    return render_template("stage0.html")


@app.route("/stage1")
def stage1():
    return render_template("stage1.html")


@app.route("/stage2")
def stage2():
    return render_template("stage2.html")


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


if __name__ == "__main__":  # gets app running
    app.run(debug=True)
