from datetime import datetime

date_time = []
description_list =[]
amount_list =[]

def add_expense(year, month, day, description, amount):
    if year < 1900 or year > datetime.now().year:
        return ("Invalid year")
    if month < 1 or month > 12:
        return ("Invalid month")
    if day < 1 or day > 31:
        return ("Invalid day")
    if amount < 0:
        return ("Invalid amount")
    date = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
    date_time.append(date)
    description_list.append(description)
    amount_list.append(amount)
    print("Adding on expense")
    print ("Expenses added successfully")
    option = int(input(option_text))
    option_method(option)




def option_method(option):
    while option not in [1, 2, 3, 4]:
        print(option_text)
        option = int(input("Please enter a valid option: "))

    if option == 1:
        year=int(input("Please enter year: "))
        month=int(input("Please enter month: "))
        day=int(input("Please enter day: "))
        description=input("Please enter description: ")
        amount=int(input("Please enter amount: "))
        print(add_expense(year, month, day, description, amount))

    if option == 2:
        for index in range(len(description_list)):
            print(description_list[index])

    if option == 4:
        print("Goodbye")









print("Welcome to semicolon Expense Tracker App")

option_text = ("1. Add on expense\n"
               "2. View all expenses\n"
               "3. Calculate total expenses\n"
               "4. Exit")
option = int(input(option_text))
option_method(option)



