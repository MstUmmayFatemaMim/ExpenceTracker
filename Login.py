import csv
from Config import FILE_PATH,COLUMNS
class user_login:

    def login_page(self):
        print("\n****************   Welcome to our Login Page  ****************")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        # with open("ExpenseTracker.csv", newline='') as csvfile:
        with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
    ######  If row is empty or broken, skip it so it doesn't crash
                if not row["username"]:
                    continue
                if username == row["username"] and password == row["password"]:
                    print("Login Successfully.")
                    return username     ####### Instantly stops and leaves the function on success
    ######   Put this outside the loop! It runs ONLY if the entire file was searched and no match was found
            print("Wrong username or password. Please try again.")
            return None

