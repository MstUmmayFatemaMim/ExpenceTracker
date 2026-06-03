from Registration import users
from Login import user_login
from Dashboard import dashboard

user = users()
login = user_login()
dash = dashboard()
while True:
    print("\n*********    Welcome to Our Expense Tracker  *********")
    print("1. Create a new account")
    print("2. Log in")
    print("3. Log out")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        # user.registration_page()  ########    Just complete the registration
        reg_user = user.registration_page()  ##### call on object. No class or anything
        if reg_user:  ######  Registration successfully
            dash.dashboard(reg_user)  ##### move the dashboard page
    elif choice == "2":
        ####login.login_page()  ########    Just complete the login
        logged_user = login.login_page()
        if logged_user:  ######  login successfully
            dash.dashboard(logged_user)  ##### move the dashboard page
    elif choice == "3":
        print("Log out")
        break  #########   It jumps only one level.
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
