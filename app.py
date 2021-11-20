import os
from flask import (
    Flask, render_template, redirect,
    request, session, url_for, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html", page_title="Readflix")


# Readflix : show last 12 saved books from users
@app.route("/readflix")
def readflix():
    books = list(mongo.db.books.find().limit(12))
    print("Books in collections: ", books)
    return render_template("index.html", books=books)


# Collection : Find a book via search bar
@app.route("/search")
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find())
    return render_template("collections.html", page_title="Collections", books=books)


# Collection : Find a book via book collection button
@app.route("/collections")
def collections():
    if request.method == 'POST':
        if request.books['collection_name'] == 'Show books collection':
            pass 
        elif request.books['collection_name'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('collections.html', books=books)


# Community : Get 8 random users to share 1 book among their upvoted books
@app.route("/community")
def community():
    users = list(mongo.db.users.find().limit(8))
    for user in user.upvoted_books :
        if book in upvoted_books:
            print(random.choice(upvoted_books))
        else:
            pass
            print("The Bookcytocin Club:", users)
    return render_template(
        "community.html", page_title="The Bookcytocin Club", user=users)

# Sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))
        print("password", request.form.get("password"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("You are in! Registration Successful.")
        return redirect(url_for("mybooklog", username=session["user"]))

    return render_template("signup.html", page_title="Sign up")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "mybooklog", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")




# MyBookLog 
@app.route("/mybooklog")
def mybooklog():
    users = mongo.db.users.find_one()
    print("The Bookcytocin Club:", users)
    return render_template(
        "mybooklog.html", page_title="MyBookLog", users=users)


# MyBookLog : Welcome user to their profile
@app.route("/welcome/<username>", methods=["GET", "POST"])
def welcome(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template(
            "mybooklog.html",  page_title="MyBookLog", username=username)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
