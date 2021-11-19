import os
from flask import (
    Flask, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("mongodb+srv://florence:flomezino3@clusterci.ouatk.mongodb.net/ms3DB?retryWrites=true&w=majority")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html", page_title="Readflix")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html", page_title="Signup")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", page_title="Login")


@app.route("/get_last_10_upvoted_books")
def get_last_10_upvoted_books():
    books = mongo.db.books.find()
    print(books)
    return render_template("index.html", books=books)


@app.route("/collections")
def collections():
    return render_template("collections.html", page_title="Collections")


@app.route("/community")
def community():
    return render_template("community.html", page_title="The Bookcytocin Club")


@app.route("/mybooklog")
def mybooklog():
    return render_template("mybooklog.html", page_title="MyBookLog")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
