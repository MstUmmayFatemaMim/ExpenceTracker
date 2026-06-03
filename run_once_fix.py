# # run_once_fix.py — run this file ONE TIME then delete it
# import csv
#
# FILE_PATH = "ExpenseTracker.csv"
# COLUMNS   = ["username","password","email","income",
#              "category","product","quantity","price","total_price","date"]
#
# with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
#     rows = list(csv.DictReader(f))
#
# with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=COLUMNS)
#     writer.writeheader()
#     for row in rows:
#         if "date" not in row or row["date"] == "":
#             row["date"] = "2026-05-01"   # ← give old rows a default date
#         writer.writerow(row)
#
# print("Done! Old rows now have a date.")