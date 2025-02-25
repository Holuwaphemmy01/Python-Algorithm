import re
date_list=[]
description_list=[]
amount_list=[]

def add_expense(date, description, amount):
    date_regex = re.compile(
        r"^(?P<year>\d{4})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[12]\d|3[01])$"
    )

    match = date_regex.match(date)
    if not match:
        raise ValueError("Invalid date")

    if description.startswith(" "):
        raise ValueError("Invalid description")

    if amount.isdigit() == False:
        raise ValueError("Invalid amount")

    if int(amount) < 0:
        raise ValueError("Inavlid amount")

    date_list.append(date)
    description_list.append(description)
    amount_list.append(amount)
    return "Expense added successfully"

