# Expense Tracker

expenses = []

print("\n--- EXPENSE TRACKER ---")

while True:
    amount = input("Enter expense (or 'done' to finish): ")

    if amount.lower() == "done":
        break

    try:
        amount = float(amount)

        if amount < 0:
            print("Expense cannot be negative!")
            continue

        expenses.append(amount)
        print("Expense added!")

    except ValueError:
        print("Invalid input! Enter a number.")

print("\n--- EXPENSE SUMMARY ---")

if expenses:
    print("All expenses:", expenses)
    print("Total expense:", sum(expenses))
    print("Highest expense:", max(expenses))
else:
    print("No expenses added.")

print("Thank you!")