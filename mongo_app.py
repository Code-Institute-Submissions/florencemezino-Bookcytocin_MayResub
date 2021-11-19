import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Readflix (get the last 10 upvoted books among all users and all books)
def users_upvoted_book():
    print("")
    print("1. Book 1")
    print("2. Book 2")
    print("3. Book 3")
    print("4. Book 4")
    print("5. Book 5")
    print("6. Book 6")
    print("7. Book 7")
    print("8. Book 8")
    print("9. Book 9")
    print("10. Book 10")

    option = input("Enter option: ")
    return option

# Collections (get all books per collection when clicking on one collection)
def books_per_collection():
    print("")
    print("1. Books")

    option = input("Enter option: ")
    return option

# Community (get 6/12 users info + their 3 last upvoted books)
def show_6_users_last_3_upvoted_books():
    print("")
    print("1. User details")
    print("2. Book 1")
    print("3. Book 2")
    print("4. Book 3")

    option = input("Enter option: ")
    return option

# MyBookLog/Login

def user_login():

# MyBookLog/Register

def user_signup():

# MyBookLog/Create (login needed: option to save books in user from books list)
def saved_book():
    print("")
    print("1. Saved book")

    option = input("Enter option: ")
    return option

# MyBookLog/Delete (login needed: remove from saved list)
def remove_saved_book():
    print("")
    print("1. Remove book")

    option = input("Enter option: ")
    return option

# MyBookLog/Update (login needed: update book user status from saved list)
def user_book_status():
    print("")
    print("1. Saved")
    print("2. Reading")
    print("3. Finished")
    print("4. Upvoted")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def main_loop():
    while True:
        option = user_book_status()
        if option == "1":
            print("What will be your next read?")
        elif option == "2":
            print("Keep it up!")
        elif option == "3":
            print("Success is not given, it is earned!")
        elif option == "4":
            print("The more we share, the more we have.")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
