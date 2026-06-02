import csv
import os
from Config import FILE_PATH,COLUMNS
# # File_Path=r"C:\Users\Mim\Downloads\ExpenseTracker.csv"       this does not work properly
# File_Path=r"ExpenseTracker.csv"


class users:
    def __init__(self):
        self.__users={}         ########    Create empty Dictionary
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w", newline="",encoding="utf-8") as f:
                csv.DictWriter(f, fieldnames=COLUMNS).writeheader()

        else:
            with (open(FILE_PATH, "r", newline="", encoding="utf-8") as f):
                for row in csv.DictReader(f):
                    if row["username"]:
                        self.__users[row["username"]] = {
                            "password": row["password"],
                            "email": row["email"],
                        }
                           #######     Connect with file and dictionary
    def registration_page(self):
        print("\n****************   Welcome to our Registration Page  ****************")
        username = input("Enter name  : ").strip()
        password = input("Enter password : ").strip()
        email = input("Enter email  : ").strip()
        if username in self.__users:
            print(f"'{username}' already exists!")
            return None
        else:
            self.__users[username]={
                "password": password,
                "email": email,
            }
            # Save new contact straight to your CSV file
            with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=COLUMNS)
                writer.writerow({
                    "username": username,
                    "password": password,
                    "email": email,
                })
                # csv.writer(f).writerow([username, password, email])
            print(f"Successfully account created for {username}")
            return username
