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


# Readflix : find 4 books in one collection
@app.route("/readflix")
def readflix():
    books = list(mongo.db.books.find({"collection_name": "Character"}).limit(4))
    print("Books in collections: ", books)
    return render_template(
        "index.html", page_title="Readflix", books=books)


# Collection : display books
@app.route("/collections")
def collections():
    books = list(mongo.db.books.find())
    collections = list(mongo.db.collections.find())
    print("Books in collections: ", books)
    return render_template(
        "collections.html", page_title="Collections", books=books, collections=collections)


@app.route("/get_collections/<collection_name>", methods=["GET", "POST"])
def get_collections(collection_name):
    collections = list(mongo.db.collections.find())
    books = list(mongo.db.books.find({"collection_name": collection_name}))
    print(books)
    return render_template(
        "collections.html", page_title="Collections", collections=collections, books=books)  


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


# MyBookLog 
@app.route("/mybooklog/<username>", methods=["GET", "POST"])
def profile(username):
    print("method:", request.method)
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
            print("My reading goal", user)
            print(goal)
            flash("Goal Successfully Saved!")
            mongo.db.users.find_one_and_update({"username": session["user"]}, {"$set": goal})
            return render_template(
                "mybooklog.html", page_title="MyBookLog", user=user)
    
        return render_template("mybooklog.html", user=user)

    return redirect(url_for("profile"))


# Add a goal
@app.route("/mybooklog/add_goal", methods=["POST", "GET"])
def add_goal():
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        goal = {
            "goal_level": request.form.get("goal_level"),
            "goal_reason": request.form.get("goal_reason"),
            "goal_obstacle": request.form.get("goal_obstacle"),
            "goal_email": request.form.get("goal_email"),
            "goal_signature": request.form.get("goal_signature"),
        }

        print("My reading goal", user)
        print(goal)
        flash("Goal Successfully Saved!")
        mongo.db.users.update_one({"username": session["user"]}, {"$set": goal})
        return render_template(
            "mybooklog.html", page_title="MyBookLog", user=user)

    return render_template("mybooklog.html", page_title="MyBookLog", user=user)


# Edit a goal
@app.route("/mybooklog/edit_goal/<goal_id>", methods=["GET", "POST"])
def edit_goal(goal_id):
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        submit = {
            "goal_level": request.form.get("goal_level"),
            "goal_reason": request.form.get("goal_reason"),
            "goal_obstacle": request.form.get("goal_obstacle"),
            "goal_signature": request.form.get("goal_signature"),
        }
        mongo.db.goals.update({"_id": ObjectId(goal_id)}, submit)
        flash("Goal Successfully Updated")

    goal = mongo.db.goals.find_one({"_id": ObjectId(goal_id)})
    print("goal: ", goal)
    return render_template(
        "edit_goal.html", page_title="MyBookLog", user=user, goal=goal)


# Delete a goal
def delete_goal(goal_id):
    mongo.db.goals.remove({"_id": ObjectId(goal_id)})
    flash("Goal Successfully Deleted")
    return redirect(url_for("add_goal"))


# Add a review
@app.route("/mybooklog/add_review", methods=["POST", "GET"])
def add_review():
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        data_review = {
            "review_book": request.form.get("review_book"),
            "review_title": request.form.get("review_title"),
            "review_content": request.form.get("review_content"),
            "review_full_name": request.form.get("review_full_name"),
        }
        print("My reading goal", user)
        print(data_review)
        flash("Your review was successfully published.")
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": data_review})
        print("Add a review", user)  
        return render_template("community.html", page_title="Community", user=user)

    return render_template("mybooklog.html", page_title="MyBookLog", user=user)

# Edit a review
@app.route("/community/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        review_id = "on" if request.form.get("review_id") else "off"
        submit = {
            "review_book": request.form.get("review_book"),
            "review_title": request.form.get("review_title"),
            "review_content": request.form.get("review_content"),
            "review_full_name": request.form.get("review_full_name"),
        }
        mongo.db.goals.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", user=user, review=review)


# Delete a review
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("add_review"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
