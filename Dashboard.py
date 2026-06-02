import csv
from Config import FILE_PATH, COLUMNS
from LeaderBoard import leaderboard
class dashboard:
    # def __init__(self):
    #     self.lb = leaderboard()
    def add_income(self, username):
        income = input("Please enter the amount of income: ")
        with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writerow({
                "username": username,
                "income": income,
            })
        print("Income added successfully")

    def add_expense(self, username, first_expense=False):
        print("Categories: rent / food / medicine / tour / other")
        category = input("Please enter your category: ")
        product = input("Please enter your product: ")
        quantity = int(input("Please enter your quantity: "))
        price = float(input("Please enter your price: "))
        totalcost = quantity * price

        with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writerow({
                "username": username,
                "category": category,
                "product": product,
                "quantity": quantity,
                "price": price,
                "total_price": totalcost,
            })
        print("Expenses added successfully")

    def view_balance(self, username):

        # ── SWITCH: collect only this user's rows ──────────
        collecting = False
        my_rows = []

        with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"] == username:
                    collecting = True
                if row["username"] != "" and row["username"] != username:
                    collecting = False
                if collecting:
                    my_rows.append(row)

        # STEP 1: Add up all income first
        total_income = 0
        for row in my_rows:
            if row["income"] != "":
                total_income += float(row["income"])

        # STEP 2: Print income OUTSIDE the table
        print(f"\n===== Your Expenses ({username}) =====")
        print(f"Total Income: {total_income}")  # ← income printed here, alone
        print()

        # STEP 3: Print expense table header
        print(f"{'Category':<12} {'Product':<12} {'Qty':<6} {'Price':<8} {'Total':<8}")
        print("-" * 50)

        # STEP 4: Print only expense rows inside the table
        total_expense = 0
        for row in my_rows:
            if row["category"] != "" and row["income"] == "":  # expense rows only
                total_expense += float(row["total_price"]) if row["total_price"] else 0
                print(
                    f"{row['category']:<12} {row['product']:<12} {row['quantity']:<6} {row['price']:<8} {row['total_price']:<8}")

        # STEP 5: Print summary below the table
        print("-" * 50)
        print(f"Total Expense: {total_expense}")
        print(f"Balance:       {total_income - total_expense}")

        ask = input("Do you want to export PDF? (yes/no): ").strip().lower()
        if ask == "yes":
            filename = f"{username}_balance.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"===== Your Expenses ({username}) =====\n")
                file.write(f"Total Income: {total_income}\n\n")
                file.write(f"{'Category':<12} {'Product':<12} {'Qty':<6} {'Price':<8} {'Total':<8}\n")
                file.write("-" * 50 + "\n")
                for row in my_rows:
                    if row["category"] != "" and row["income"] == "":
                        file.write(
                            f"{row['category']:<12} {row['product']:<12} {row['quantity']:<6} {row['price']:<8} {row['total_price']:<8}\n")
                file.write("-" * 50 + "\n")
                file.write(f"Total Expense: {total_expense}\n")
                file.write(f"Balance:       {total_income - total_expense}\n")
            print(f"Success! File saved as '{filename}'. Open it and choose Print -> Save as PDF.")
        else:
            print("Returning to dashboard menu...")

    def view_by_category(self,username):
        with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
            all_rows = list(csv.DictReader(f))
        my_rows = []
        collecting = False
        for row in all_rows:
            if row["username"] == username:
                collecting = True
            if row["username"] != "" and row["username"] != username:
                collecting = False
            if collecting:
                my_rows.append(row)
        category_total={}
        for row in my_rows:
            if row["category"] !="" and row["income"]== "":
                cat=row["category"]
                amount=float(row["total_price"]) if row["total_price"] else 0

                if cat in category_total:
                    category_total[cat]+=amount     #########  if category already have and add the same category multiple time
                else:
                    category_total[cat]=amount      ###### new category or single time add the category
        print(f"\n===== Expenses by Category ({username}) =====")
        print(f"{'Category':<15} {'Total':<10}")
        print("-" * 30)

        for cat, total in category_total.items():
            print(f"{cat:<15} {total:<10}")

        print("-" * 30)
        print(f"{'Grand Total':<15} {sum(category_total.values()):<10}")

    def word_frequency(self,username):
        word_frequency = []
        with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                # if row["username"] == username and row["product"] != "":     ###   Used for product
                #     word_frequency.append(row["product"].lower())
                if row["username"] == username and row["category"] != "":      #### Used for category
                    word_frequency.append(row["category"].lower())

        stock = {}
        for letter in word_frequency:
            if letter in stock:
                stock[letter] += 1
            else:
                stock[letter] = 1

        # STEP 3 — print result
        print(f"\n===== Word Frequency ({username}) =====")
        for w, count in stock.items():
            print(f"{w:<15} {count} time(s)")

    def get_grade(self,username):
        total_income = 0
        total_expense = 0
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"]==username:
                    if row["income"]!="":
                        total_income += float(row["income"])
                    if row["category"] != "" and row["income"]=="":
                        total_expense+=float(row["total_price"]) if row["total_price"] else 0
        # if total_income==0:
        #     print("You don't have any expenses!")
        ratio=(total_expense/total_income)*100
        if ratio <= 50:
            grade = "A"
            msg = "Excellent — saving more than spending"
        elif ratio <= 70:
            grade = "B"
            msg = "Good — healthy spending"
        elif ratio <= 85:
            grade = "C"
            msg = "Fair — watch your spending"
        elif ratio <= 99:
            grade = "D"
            msg = "Warning — almost over budget"
        else:
            grade = "F"
            msg = "Over budget!"

        print(f"\n===== Budget Grade ({username}) =====")
        print(f"Income  : {total_income}")
        print(f"Expense : {total_expense}")
        print(f"Ratio   : {ratio:.1f}%")
        print(f"Grade   : {grade} — {msg}")
    def dashboard(self, username):
        while True:
            print(f"\n===== Dashboard ({username}) =====")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. View by Category")
            print("5. Leaderboard")
            print("6. Word Frequency")
            print("7. Get Grade")
            print("8. Logout")

            choice = input("\nChoose: ").strip()

            if choice == "1":
                self.add_income(username)
            elif choice == "2":
                self.add_expense(username)
            elif choice == "3":
                self.view_balance(username)
            elif choice == "4":
                self.view_by_category(username)
            elif choice == "5":
                leaderboard().show_leaderboard()
            elif choice == "6":
                self.word_frequency(username)
            elif choice == "7":
                self.get_grade(username)
            elif choice == "8":
                print("Going back.")
                break
            else:
                print("Invalid choice.")

