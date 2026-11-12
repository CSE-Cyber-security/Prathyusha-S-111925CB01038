
expenses = []
balance = 5000

while True:
    print("\n--- DAILY EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append([name, amount])
        balance -= amount
        print("Expense Added!")

    elif choice == "2":
        for e in expenses:
            print(e[0], ":", e[1])

    elif choice == "3":
        total = sum(e[1] for e in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Remaining Balance:", balance)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
