"""
Budget Tracker
Tracks income and expenses with a running transaction history.
Data is saved to and loaded from a JSON file (budget.json), and
the script calculates the current balance from all logged transactions.
"""




import json
import os

def load_data():
    if os.path.exists("budget.json"):
        with open("budget.json", "r") as file:
            return json.load(file)
    return {"transactions": [], "balance": 0}

def save_data(data):
    with open("budget.json", "w") as file:
        json.dump(data, file)

def show_balance(data):
    print(f"\nCurrent Balance: £{data['balance']:.2f}")

def add_income(data):
    amount = float(input("Enter income amount: £"))
    description = input("Enter description: ")
    data["transactions"].append({
        "type": "income",
        "amount": amount,
        "description": description
    })
    data["balance"] += amount
    save_data(data)
    print(f"Income of £{amount:.2f} added!")

def add_expense(data):
    amount = float(input("Enter expense amount: £"))
    description = input("Enter description: ")
    if amount > data["balance"]:
        print("Warning: This expense exceeds your current balance!")
    data["transactions"].append({
        "type": "expense",
        "amount": amount,
        "description": description
    })
    data["balance"] -= amount
    save_data(data)
    print(f"Expense of £{amount:.2f} added!")

def show_transactions(data):
    if len(data["transactions"]) == 0:
        print("No transactions yet!")
    else:
        print("\n--- Transaction History ---")
        for t in data["transactions"]:
            if t["type"] == "income":
                print(f"+ £{t['amount']:.2f} — {t['description']}")
            else:
                print(f"- £{t['amount']:.2f} — {t['description']}")
        show_balance(data)

def main():
    data = load_data()
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Show balance")
        print("2. Add income")
        print("3. Add expense")
        print("4. Show transactions")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_balance(data)
        elif choice == "2":
            add_income(data)
        elif choice == "3":
            add_expense(data)
        elif choice == "4":
            show_transactions(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()
