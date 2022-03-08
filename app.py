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

# search for one collection
# search for 4 books
# render 4 books of one category in index.html

@app.route("/readflix")
def readflix():
    books = list(mongo.db.books.aggregate([
        {"$sample": {"size": 4}}
    ]))
    print("Books in collections: ", books)
    return render_template(
        "index.html", page_title="Readflix", books=books)


# Collection : find a book via search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template(
        "collections.html", page_title="Collections", books=books)


# Collection : display books in collection
@app.route("/collections")
def collections():
    books = list(mongo.db.books.find())
    print("Books in collections: ", books)
    return render_template(
        "collections.html", page_title="Collections", books=books)


# Community : display community / blog
@app.route("/community")
def community():
    users = list(mongo.db.users.find().limit(8))
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
                    "mybooklog", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")


# MyBookLog : view
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("mybooklog.html", username=username)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# MyBookLog : user add a goal
@app.route("/mybooklog/add_goal", methods=["POST", "GET"])
def mybooklog():
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        dta = {
            "goal_reason": request.form.get("goal_reason"),
            "goal_obstacle": request.form.get("goal_obstacle"),
            "goal_email": request.form.get("goal_email"),
            "goal_signature": request.form.get("goal_signature"),
        }

        print("My reading goal", user)
        print(dta)
        flash("Your goal has been saved!")
        mongo.db.users.update_one({"username": session["user"]}, {"$set": dta})
        return render_template(
            "mybooklog.html", page_title="MyBookLog", user=user)

    return render_template("mybooklog.html", page_title="MyBookLog", user=user)


# MyBookLog : user view / edit goal 
@app.route("/mybooklog/edit_goal/<goal_id>", methods=["GET", "POST"])
def edit_goal(goal_id):
    if request.method == "POST":
        is_goal = "on" if request.form.get("is_goal") else "off"
        submit = {
            "goal_reason": request.form.get("goal_reason"),
            "goal_obstacle": request.form.get("goal_obstacle"),
            "goal_email": request.form.get("goal_email"),
            "goal_signature": request.form.get("goal_signature"),
        }
        mongo.db.goals.update({"_id": ObjectId(goal_id)}, submit)
        flash("Goal Successfully Updated")

    goal = mongo.db.tasks.find_one({"_id": ObjectId(goal_id)})
    return render_template("edit_goal.html", goal=goal)


# MyBookLog : user view / delete goal
def delete_goal(goal_id):
    mongo.db.goal.remove({"_id": ObjectId(goal_id)})
    flash("Goal Successfully Deleted")
    return redirect(url_for("add_goal"))


# MyBookLog : user add a review
@app.route("/add_review", methods=["POST"])
def review():
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    if request.method == "POST":
        data = {
            "review_title": request.form.get("review_title"),
            "review_author": request.form.get("review_author"),
            "review_content": request.form.get("review_content"),
            "review_full_name": request.form.get("review_full_name"),
        }
        print("My reading goal", user)
        print(data)
        flash("Your review is being processed. Stay tune!")
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": data})

        print("Add a review", user)
    return render_template("mybooklog.html", page_title="MyBookLog", user=user)


# MyBookLog : user view / edit review
@app.route("/mybooklog/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        is_review = "on" if request.form.get("is_review") else "off"
        submit = {
            "review_book": request.form.get("review_book"),
            "review_content": request.form.get("review_content"),
            "review_full_name": request.form.get("review_full_name"),
        }
        mongo.db.goals.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


# MyBookLog : user view / delete review
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("add_review"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
