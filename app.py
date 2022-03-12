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
    return render_template("bookcytocin.html", page_title="Bookcytocin")


# About Bookcytocin
@app.route("/bookcytocin")
def about():
    return render_template("bookcytocin.html", page_title="Bookcytocin")


# Readflix : find 4 books in one collection and save books to profile
@app.route("/readflix", methods=["GET", "POST"])
def readflix():
    if request.method == "POST":
        book_id = request.form.get("book_id")
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        print(book)
        mongo.db.users.update(
            {"username": session["user"]},
            {
                "$push": {"saved_books": {"book_image_url": book["image_url"],
                          "book_title": book["title"], "book_author": book[
                              "author"],
                        "book_description": book["description"],
                        "book_amazon_link": book["amazon_link"]}}, },
                {upsert: True}
        )
        flash("Book Successfully Saved in your Wishlist!")
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template(
                "saved_book.html", page_title="MyBookLog", user=user)       
        return render_template("mybooklog.html", user=user)

    books = list(mongo.db.books.find(
        {"collection_name": "Character"}).limit(4))
    return render_template(
        "index.html", page_title="Readflix", books=books)

    return redirect(url_for("profile")) 

# OPTION 2 Readflix : find 4 books in one collection and save books to profile
# @app.route("/readflix", methods=["GET", "POST"])
# def readflix():
#     book_id = request.form.get("book_id")
#     book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
#     if request.method == "POST":
#         book_id = {
#             "book.image_url": request.form.get("book.image_url"),
#             "book.amazon_link": request.form.get("book.amazon_link"),
#             "book.title": request.form.get("book.title"),
#             "book.author": request.form.get("book.author"),
#             "book_description": request.form.get("book_description"),
#             "book_amazon_link": request.form.get("review_full_name"),
#         }
#         flash("Book Successfully Saved in your Wishlist!")
#         mongo.db.users.find_one_and_update(
#                 {"username": session["user"]}, {"$set": book})
#         user = mongo.db.users.find_one({"username": session["user"]})
#         return render_template(
#             "saved.html.html", page_title="MyBookLog", user=user)       

#     return redirect(url_for("profile")) 

#     books = list(mongo.db.books.find(
#         {"collection_name": "Character"}).limit(4))
#     return render_template(
#         "index.html", page_title="Readflix", books=books)

#     return redirect(url_for("profile")) 


# Collection : display books and save books to profile
@app.route("/collections", methods=["GET", "POST"])
def collections():
    books = list(mongo.db.books.find())
    collections = list(mongo.db.collections.find())
    return render_template(
        "collections.html", page_title="Collections", books=books,
        collections=collections)


# Collection : display books by collection and save books to profile
@app.route("/get_collections/<collection_name>", methods=["GET", "POST"])
def get_collections(collection_name):
    collections = list(mongo.db.collections.find())
    books = list(mongo.db.books.find({"collection_name": collection_name}))
    return render_template(
        "collections.html", page_title="Collections",
        collections=collections, books=books)  


# Collection : find a book via search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template(
        "collections.html", page_title="Collections", books=books)


# Community : display review community / blog
@app.route("/community")
def community():
    users = list(mongo.db.users.find().limit(6))
    return render_template(
        "community.html", page_title="The Bookcytocin Club", user=users)


# Delete a saved book
def delete_saved_book():
    book_id = request.form.get("book_id")
    mongo.db.users.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Removed from your Wishlist")
    return redirect(url_for("delete_saved_book"))


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
        return redirect(url_for("login", username=session["user"]))

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


# Logout
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# MyBookLog (Add / Edit / Delete goal)
@app.route("/mybooklog/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if user:
        if request.method == "POST":
            goal = {
                "goal_level": request.form.get("goal_level"),
                "goal_reason": request.form.get("goal_reason"),
                "goal_obstacle": request.form.get("goal_obstacle"),
                "goal_email": request.form.get("goal_email"),
                "goal_signature": request.form.get("goal_signature"),
            }

            flash("Goal Successfully Saved!")
            mongo.db.users.find_one_and_update(
                {"username": session["user"]}, {"$set": goal})
            user = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "mybooklog.html", page_title="MyBookLog", user=user)       
        return render_template("mybooklog.html", user=user)

    return redirect(url_for("profile")) 


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
