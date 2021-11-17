import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collections")
def collections():
    return render_template("collections.html")


@app.route("/community")
def community():
    return render_template("community.html") 


@app.route("/mybooklog")
def mybooklog():
    return render_template("mybooklog.html") 


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)