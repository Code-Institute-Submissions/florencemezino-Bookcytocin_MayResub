import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Readflix")


@app.route("/collections")
def collections():
    return render_template("collections.html", page_title="Collections")


@app.route("/community")
def community():
    return render_template("community.html", page_title="The Bookcytocin Club")
         

@app.route("/mybooklog")
def mybooklog():
    return render_template("mybooklog.html", page_title="MyBookLog")


@app.route("/signup")
def signup():
    return render_template("signup.html", page_title="Signup") 


@app.route("/login")
def login():
    return render_template("login.html", page_title="Login")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
