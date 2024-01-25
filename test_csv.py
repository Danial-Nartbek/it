import csv

users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"


with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    print("Юзеры: ")
    for user in users:
        print(user)

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    print("Стокс: ")
    for stock in stocks:
        print(stock)

with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    print("Итемс: ")
    for item in items:
        print(item)
