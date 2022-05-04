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
    return render_template("bookcytocin.html", page_title="Home")


@app.route("/bookcytocin")
def about():
    """
    Display home page / about Bookcytocin
    """
    return render_template("bookcytocin.html", page_title="Bookcytocin")


@app.route("/readflix", methods=["GET", "POST"])
def readflix():
    """
    Display books in readflix view and save book to user's wishlist
    """
    if request.method == "POST":
        book_id = request.form.get("book_id")
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

        user_saved_book = {
                "_id": book_id,
                "book_image_url": book["image_url"],
                "book_title": book["title"],
                "book_author": book["author"],
                "book_description": book["description"],
                "book_amazon_link": book["amazon_link"]
        }

        flash("Book Successfully Saved in your Wishlist!")
        user = mongo.db.users.update_one({"username": session["user"]}, {
            "$push": {"saved_books": user_saved_book}})

        user = mongo.db.users.find_one({"username": session["user"]})
        print(user)
        return render_template(
            "index.html", page_title="Readflix", user=user)

    books = list(mongo.db.books.find(
        {"collection_name": "Character"}).limit(4))
    return render_template(
        "index.html", page_title="Readflix", books=books)


@app.route("/collections", methods=["GET", "POST"])
def collections():
    """
    Display books in collections view and save book to user's wishlist
    """
    if request.method == "POST":
        book_id = request.form.get("book_id")
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        user_saved_book = {
                "_id": book_id,
                "book_image_url": book["image_url"],
                "book_title": book["title"],
                "book_author": book["author"],
                "book_description": book["description"],
                "book_amazon_link": book["amazon_link"]
        }

        flash("Book Successfully Saved in your Wishlist!")
        user = mongo.db.users.update_one({"username": session["user"]}, {
            "$push": {"saved_books": user_saved_book}})

        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template(
            "collections.html", page_title="Collections", user=user)
    
    books = list(mongo.db.books.find())
    collections = list(mongo.db.collections.find())
    return render_template(
        "collections.html", page_title="Collections", books=books,
        collections=collections)


@app.route("/get_collections/<collection_name>", methods=["GET", "POST"])
def get_collections(collection_name):
    """
    Display books by collection
    """
    collections = list(mongo.db.collections.find())
    books = list(mongo.db.books.find({"collection_name": collection_name}))
    return render_template(
        "collections.html", page_title="Collections",
        collections=collections, books=books)


@app.route("/delete_saved_book/<book_id>", methods=["GET", "POST"])
def delete_saved_book(book_id):
    """
    Remove book from user's wishlist
    """
    mongo.db.users.update_one({"username": session["user"]}, {"$pull": {
        'saved_books': {"_id": book_id},
        }})
    flash("Book Successfully Removed from your Wishlist")

    username = session['user']
    return redirect(url_for("profile", username=username))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Find a book via search bar + no results found
    """
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template(
        "collections.html", page_title="Collections", books=books)
        
    flash("No results found")
    return redirect(url_for("login"))


@app.route("/community")
def community():
    """
    Display community / blog
    """
    users = list(mongo.db.users.find().limit(6))
    return render_template(
        "community.html", page_title="The Bookcytocin Club", user=users)


@app.route("/mybooklog/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Update user's goal and get saved books
    """
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if user:
        books = user["saved_books"]
        if request.method == "POST":
            goal = {
                "goal_level": request.form.get("goal_level"),
                "goal_reason": request.form.get("goal_reason"),
                "goal_obstacle": request.form.get("goal_obstacle"),
                "goal_signature": request.form.get("goal_signature"),
            }

            flash("Goal Successfully Saved!")
            mongo.db.users.find_one_and_update(
                {"username": session["user"]}, {"$set": goal})
            user = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "mybooklog.html", page_title="MyBookLog", user=user,
                books=books)

        return render_template("mybooklog.html", user=user, books=books)
    return redirect(url_for("profile", username=username))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allow user to sign up
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))
        print("password", request.form.get("password"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "saved_books": []
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("You are in! Registration Successful.")
        return redirect(url_for("about", username=session["user"]))

    return render_template("signup.html", page_title="Sign up")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allow user to log in
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to Bookcytocin {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")


@app.route("/logout")
def logout():
    """
    Allow user to log out
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
