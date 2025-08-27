def generate_summary(transactions):
    income = 0
    expense = 0

    for tx in transactions:
        if tx["type"] == "income":
            income += float(tx["amount"])
        elif tx["type"] == "expense":
            expense += float(tx["amount"])

    balance = income - expense

    return {
        "income": income,
        "expense": expense,
        "balance": balance
    }
