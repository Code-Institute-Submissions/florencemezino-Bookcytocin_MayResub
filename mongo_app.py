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


# Readflix (get the last 10 upvoted books among all users)

# Collections (get all books per collection when clicking on one collection)

# Community (get 6/12 users info + their 3 last upvoted books)

# MyBookLog (get user info + list of books from book status )

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
    