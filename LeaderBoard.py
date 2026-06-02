import csv

from Config import FILE_PATH

class leaderboard:
    def view_by_income(self):
        user_incomes = {}
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"] != "" and row["income"] != "":
                    name = row["username"]
                    amount = float(row["income"])
                    if name in user_incomes:
                        user_incomes[name] = user_incomes[name] + amount    ##### old user in user_income
                    else:
                        user_incomes[name] = amount    ##### new user in user_income

        ranking_list = []
        for name, total in user_incomes.items():
            ranking_list.append([total, name])  ###### it helps to sorted by money number otherwise it we wrote [name, total] it sorted by alphabetically

        ranking_list.sort(reverse=True)     ####### helps to sorted high to low

        print("\nRank  Username       Total Income")
        print("-" * 33)
        rank = 1
        for total, name in ranking_list:
            print(f"{rank:<5} {name:<14} {total}")
            rank = rank + 1

    def view_by_expense(self):
        user_expenses = {}
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"] != "" and row["total_price"] != "" and row["income"] == "":
                    name = row["username"]
                    amount = float(row["total_price"])

                    if name in user_expenses:
                        user_expenses[name] = user_expenses[name] + amount
                    else:
                        user_expenses[name] = amount

        ranking_list = []
        for name, total in user_expenses.items():
            ranking_list.append([total, name])  # Put number first for sorting

        ranking_list.sort(reverse=True)

        print("\nRank  Username       Total Expense")
        print("-" * 33)
        rank = 1
        for total, name in ranking_list:
            print(f"{rank:<5} {name:<14} {total}")
            rank = rank + 1

    def view_by_balance(self):
        user_balances = {}
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"] != "":
                    name = row["username"]
                    if name not in user_balances:
                        user_balances[name] = 0.0   ####    new user and do not add money here.without this it will create error
                    if row["income"] != "":
                        user_balances[name] = user_balances[name] + float(row["income"])
                    if row["total_price"] != "" and row["income"] == "":
                        user_balances[name] = user_balances[name] - float(row["total_price"])

        ranking_list = []
        for name, total in user_balances.items():
            ranking_list.append([total, name])
        ranking_list.sort(reverse=True)
        print("\nRank  Username       Total Balance")
        print("-" * 33)
        rank = 1
        for total, name in ranking_list:
            print(f"{rank:<5} {name:<14} {total}")
            rank = rank + 1

    def view_by_category(self):
        user_categories = {}
        cat = input("Enter category to compare (food/rent/medicine/tour): ").strip()
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["username"]!="" and row["category"] == cat and row["total_price"] != "":
                    name = row["username"]
                    amount = float(row["total_price"])
                    if name in user_categories:
                        user_categories[name] =user_categories[name]+ amount
                    else:
                        user_categories[name] = amount
        ranking_list = []
        for name,total in user_categories.items():
            ranking_list.append([total, name])
        ranking_list.sort(reverse=True)
        print("\nRank  Username       Total Expense")
        print("-" * 33)
        rank = 1
        for categorys, name in ranking_list:
            print(f"{rank:<5} {name:<14} {categorys}")
            rank = rank + 1

    def show_leaderboard(self):
        while True:
            print(f"\n===== LEADERBOARD =====")
            print("1. View by Income")
            print("2. View by Expense")
            print("3. View by Balance")
            print("4. View by Category")
            print("5. Go Back")

            choice = input("\nChoose: ").strip()

            if choice == "1":
                self.view_by_income()
            elif choice == "2":
                self.view_by_expense()
            elif choice == "3":
                self.view_by_balance()
            elif choice == "4":
                self.view_by_category()
            elif choice == "5":
                print("Going back.")
                break
            else:
                print("Invalid choice.")

