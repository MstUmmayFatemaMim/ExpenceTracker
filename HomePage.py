from Registration import users
from Login import user_login
from Dashboard import dashboard
user=users()
login=user_login()
dash=dashboard()
while True:
    print("\n*********    Welcome to Our Expense Tracker  *********")
    print("1. Create a new account")
    print("2. Log in")
    print("3. Log out")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        reg_user=user.registration_page()       ##### call on object. No class or anything
        if reg_user:
            dash.dashboard(reg_user)
    elif choice == "2":
        logged_user=login.login_page()
        if logged_user:
            dash.dashboard(logged_user)
    elif choice == "3":
        # users.logout_page()
        print("Log out")
        break
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")

